from flask import Flask
from handlers.routes import configure_routes

app = Flask(__name__)

configure_routes(app)

# if __name__ == "__main__":
#     app.run(debug=True)

# from app import app
from werkzeug.serving import make_server

if __name__ == "__main__":
    server = make_server("127.0.0.1", 5000, app)
    print("Running on http://127.0.0.1:5000")
    server.serve_forever()