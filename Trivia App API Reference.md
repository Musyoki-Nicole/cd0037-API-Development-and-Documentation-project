API Reference:
-This section contains the endpoints contained in the application.

Base URL:
-The app is run locally and has no base URL. the backend application is hosted at        127.0.0.1:5000.

Authentication:
-This version of the app has no authentication.

Error Handling:
-The application has several endpoints to deal with errors. The errors are returned as JSON objects. An example of this is:
    {
      "error": 404,
      "message": "Resource not found",
      "success": false
    }

-The errors that are returned when requests fail are:
    1) Error Code 404: Resource not found
    2) Error Code 405: Method not allowed
    3) Error Code 422: Unprocessed

Endpoint Library:
-The endpoints included in the application all perform different functionalities. They are:
     -GET /categories
     -GET /questions
     -GET /categories/{category_id}/question
     -POST /questions
     -DELETE /questions/{question_id}

GET /categories:
-Shows the list of categories available.
-Returns json objects of categories, success value and the total number of categories.
    sample:
      curl http://127.0.0.1:5000/categories
        {
          "categories": [
          {
            "id": 1,
            "type": "Science"
          },
          {
            "id": 2,
            "type": "Art"
          },
          {
            "id": 3,
            "type": "Geography"
          },
          {
            "id": 4,
            "type": "History"
          },
          {
            "id": 5,
            "type": "Entertainment"
          },
          {
            "id": 6,
            "type": "Sports"
          }
        ],
          "success": true,
          "total_categories": 6
        }

GET /categories:
-Shows the list of questions available in groups of ten. Includes a request argument to choose page number starting from 1.
-Returns json objects of questions, success value and the total number of questions.
    sample:
      curl http://127.0.0.1:5000/questions
        {
          "questions": [
          {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
          },
          {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
          },
          {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
          },
          {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
          },
          {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
          },
          {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
          },
          {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
          },
          {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
          },
          {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
          },
          {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
          }
        ],
        "success": true,
        "total_questions": 19
        }

GET /categories/{category_id}/question:
-Shows the list of questions grouped under or based on the categories available.
-Returns json objects of questions, success value and the total number of questions.
    sample:
      curl http://127.0.0.1:5000/categories/2/questions
        {
          "questions": [
          {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
          },
          {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
          },
          {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
          },
          {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
          }
        ],
        "success": true,
        "total_questions": 4
        }

POST /questions:
-Adds a new question using question, answer, difficulty and category input from the user.
-Returns json objects of the question id, success value, the total number of questions and the question listed.
    sample:
      curl http://127.0.0.1:5000/questions?page=2 -X POST -H "Content-Type: application/json" -d '{"question": "How long is an Eon?", "answer": "A Billion years.", "difficulty": "1", "category": "1"}'
        {
          "questions": [
          {
            "answer": "A Billion years.",
            "category": 1,
            "difficulty": 1,
            "id": 24,
            "question": "How long is an Eon?"
          }
        ],
        "created": 24
        "success": true,
        "total_questions": 20
        }

DELETE /question:
-Deletes a question using the question id.
-Returns json objects of the deleted question id, success value, the total number of questions and the questions listed.
    sample:
      curl -X DELETE http://127.0.0.1:5000/questions/9?page=1
        {
          questions": [
          {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
          },
          {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
          },
          {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
          },
          {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
          },
          {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
          },
          {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
          },
          {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
          },
          {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
          },
          {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
          },
          {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
          }
        ],
        "deleted": 9
        "success": true,
        "total_questions": 19
        }
