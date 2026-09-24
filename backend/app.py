import sys
import os

from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector


# =========================================================
# PROJECT ROOT
# =========================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(
    PROJECT_ROOT
)


# =========================================================
# FLASK APP
# =========================================================

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

# =========================================================
# ALLOWED FRONTEND ORIGINS
# =========================================================

ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
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
#
# This is the important fix.
#
# Browser sends OPTIONS before POST /claim-coins
# because dashboard uses JSON + credentials.
#
# We explicitly return HTTP 204.
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
def add_cors_headers(
    response
):

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
# MYSQL CONNECTION
# =========================================================

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "3306")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    charset="utf8"
)

cursor = db.cursor()
cursor.execute("SHOW DATABASES")
print("DATABASES VISIBLE TO RENDER:")
for row in cursor.fetchall():
    print(row[0])
cursor.close()
# =========================================================
# DATABASE RECONNECT
# =========================================================

@app.before_request
def reconnect_database():

    try:

        db.ping(
            reconnect=True,
            attempts=3,
            delay=1
        )

    except Exception as error:

        print(
            "Database reconnect error:",
            error
        )


# =========================================================
# IMPORT ALL LEARNQUEST ROUTES
# =========================================================

import routes


# =========================================================
# TEST ROUTE
# =========================================================

@app.route(
    "/",
    methods=["GET"]
)
def home():

    return (
        "LearnQuest Backend + MySQL Connected!"
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