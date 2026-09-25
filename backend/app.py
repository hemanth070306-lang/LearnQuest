import sys
import os

from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2


# =========================================================
# PROJECT ROOT
# =========================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)


# =========================================================
# FLASK APP
# =========================================================

app = Flask(__name__)

# Session cookie settings for Render frontend + backend
app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True
)

app.secret_key = os.getenv(
    "SECRET_KEY"
) or "learnquest-local-secret-2026"


# =========================================================
# ALLOWED FRONTEND ORIGINS
# =========================================================

ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "https://learnquest-4wp2.onrender.com",
    "https://learnquest001.onrender.com"
]


# =========================================================
# CORS
# =========================================================

CORS(
    app,
    resources={
        r"/*": {
            "origins": ALLOWED_ORIGINS,

            "methods": [
                "GET",
                "POST",
                "PUT",
                "DELETE",
                "OPTIONS"
            ],

            "allow_headers": [
                "Content-Type",
                "Accept",
                "X-Requested-With"
            ],

            "supports_credentials": True
        }
    },

    supports_credentials=True,

    automatic_options=True
)


# =========================================================
# HANDLE PREFLIGHT REQUESTS
# =========================================================

@app.before_request
def handle_preflight():

    if request.method == "OPTIONS":

        return (
            "",
            204
        )


# =========================================================
# EXTRA CORS HEADERS
# =========================================================

@app.after_request
def add_cors_headers(response):

    origin = request.headers.get(
        "Origin"
    )

    if origin in ALLOWED_ORIGINS:

        response.headers[
            "Access-Control-Allow-Origin"
        ] = origin

        response.headers[
            "Access-Control-Allow-Credentials"
        ] = "true"

        response.headers[
            "Access-Control-Allow-Methods"
        ] = (
            "GET, POST, PUT, DELETE, OPTIONS"
        )

        response.headers[
            "Access-Control-Allow-Headers"
        ] = (
            "Content-Type, Accept, X-Requested-With"
        )

    return response


# =========================================================
# POSTGRESQL CONNECTION
# =========================================================

def connect_database():

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=int(
            os.getenv(
                "DB_PORT",
                "5432"
            )
        ),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME")
    )


# =========================================================
# CONNECT TO DATABASE
# =========================================================

db = connect_database()

cursor = db.cursor()

print(
    "PostgreSQL database connected successfully!"
)


# =========================================================
# DATABASE RECONNECT
# =========================================================

@app.before_request
def reconnect_database():

    global db
    global cursor

    try:

        if db.closed:

            db = connect_database()

            cursor = db.cursor()

    except Exception as error:

        print(
            "Database reconnect error:",
            error
        )


# =========================================================
# IMPORT ALL LEARNQUEST ROUTES
# =========================================================

if __name__ == "__main__":

    sys.modules["app"] = sys.modules[__name__]


from backend import routes


# =========================================================
# HOME ROUTE
# =========================================================

@app.route(
    "/",
    methods=["GET"]
)
def home():

    return (
        "LearnQuest Backend + PostgreSQL Connected!"
    )


# =========================================================
# OPTIONAL CORS TEST
# =========================================================

@app.route(
    "/cors-test",
    methods=[
        "GET",
        "POST",
        "OPTIONS"
    ]
)
def cors_test():

    return jsonify({

        "message":
            "LearnQuest CORS is working.",

        "origin":
            request.headers.get(
                "Origin"
            ),

        "method":
            request.method

    }), 200


# =========================================================
# START SERVER
# =========================================================

if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )