from os import environ
from FlaskExercise import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)

# from os import environ
# from FlaskExercise import app

# if __name__ == '__main__':
#     HOST = environ.get('SERVER_HOST', '0.0.0.0')
#     try:
#         PORT = int(environ.get('SERVER_PORT', '8080'))  # Changed default port to 8080
#     except ValueError:
#         PORT = 8080
#     app.run(HOST, PORT, debug=True)