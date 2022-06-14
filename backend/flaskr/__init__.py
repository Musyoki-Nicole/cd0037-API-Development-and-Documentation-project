import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r'/api/*': {'origins': '*'}})

    """
    after_request decorator to set Access-Control-Allow.
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS')
        return response

    """
    Endpoint to handle GET requests for all available categories.
    """
    @app.route('/categories')
    def retrieve_categories():
        categories = Category.query.order_by(Category.id).all()
        formatted_categories = [category.format() for category in categories]

        if len(formatted_categories) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': formatted_categories,
            'total_categories': len(categories)
            })

    """
    Endpoint to handle GET requests for questions, including pagination for every 10 questions.
    """
    @app.route('/questions')
    def retrieve_questions():
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        selection = Question.query.order_by(Question.id).all()
        formatted_questions = [question.format() for question in selection]

        if len(formatted_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': formatted_questions[start:end],
            'total_questions': len(selection)
            })

    """
    DELETE endpoint to delete a question using its question ID.
    """
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            formatted_questions = [question.format() for question in selection]

            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': formatted_questions[start:end],
                'total_questions': len(selection)
                })
        except:
            abort(422)

    """
    POST endpoint to post a new question.
    """
    @app.route('/questions', methods=['POST'])
    def add_question():
        body = request.get_json()
        search = body.get('search', None)

        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_difficulty = body.get('difficulty', None)
        new_category = body.get('category', None)

        try:
            if search:
                selection = Question.query.order_by(Question.id).filter(Question.question.ilike(f'%{search}%')).all()
                formatted_questions = [question.format() for question in selection]

                return jsonify({
                    'success': True,
                    'questions': formatted_questions[start:end],
                    'total_questions': len(selection)
                    })
            else:
                question = Question(question=new_question, answer=new_answer, difficulty=new_difficulty, category=new_category)
                question.insert()

                selection = Question.query.order_by(Question.id).all()
                formatted_questions = [question.format() for question in selection]

                return jsonify({
                    'success': True,
                    'created': question_id,
                    'questions': formatted_questions[start:end],
                    'total_questions': len(selection)
                    })
        except:
            abort(422)

    """
    POST endpoint to get questions based on a search term.
    """
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        try:
            body = request.get_json()



        except:
            abort(422)

    """
    GET endpoint to get questions based on category.
    """
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def retrieve_category_questions(category_id):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        selection = Question.query.filter(Question.category == str(category_id)).order_by(Question.id).all()
        formatted_questions = [question.format() for question in selection]

        if len(formatted_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': formatted_questions[start:end],
            'total_questions': len(selection)
            })

    """
    POST endpoint to get questions to play the quiz.
    """
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        body = request.get_json()
        category = body.get('quiz_category')
        previous_questions = body.get('previous_questions')

        try:
            if category['id'] == 0 and Question.id not in previous_questions:
                questions = Question.query.filter(Question.id).all()

            else:
                questions = Question.query.filter(Question.id, Question.category == str(category['id'])).all()

            if len(questions) > 0:
                random_number = randrange(0, len(questions)-1)
                next_question = questions[random_number].format()

            return jsonify({
                'success': True,
                'question': next_question
                })
        except:
            abort(422)

    """
    Error handlers for expected error 404, 405 and 422 errors.
    """
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
        'success': False,
        'error': 404,
        'message': 'Resource not found'
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
        'success': False,
        'error': 405,
        'message': 'Method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
        'success': False,
        'error': 422,
        'message': 'Unprocessable'
        }), 422

    return app
