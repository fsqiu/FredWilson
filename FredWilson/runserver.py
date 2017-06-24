"""
This script runs the FredWilson application using a development server.
"""

from os import environ
from FredWilson import app



if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(host='0.0.0.0',port=8000,debug=True)
