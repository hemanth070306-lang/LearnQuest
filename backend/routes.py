from flask import request, jsonify, session
from backend.app import app, db
from psycopg2.extras import RealDictCursor

from nlp.preprocessing import preprocessing
from nlp.topic_detector import detect_topic
from nlp.knowledge_gap import detect_knowledge_gap


# =========================================================
# REGISTER
# =========================================================

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json() or {}

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    language = data.get("preferred_language", "en")

    if not name or not email or not password:
        return jsonify({
            "message": "Name, email and password are required."
        }), 400

    cursor = db.cursor()

    cursor.execute(
        "SELECT id FROM users WHERE email = %s",
        (email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        cursor.close()

        return jsonify({
            "message": "Email already registered"
        }), 400

    cursor.execute(
        """
        INSERT INTO users
        (
            name,
            email,
            password,
            preferred_language,
            coins
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            name,
            email,
            password,
            language,
            20
        )
    )

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Registration successful!"
    }), 201


# =========================================================
# LOGIN
# =========================================================

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json() or {}

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and password are required."
        }), 400

    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )

    cursor.execute(
        """
        SELECT
            id,
            name,
            email,
            password,
            preferred_language,
            xp,
            coins,
            streak
        FROM users
        WHERE email = %s
        """,
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()

    if user is None:

        return jsonify({
            "message": "Invalid email or password."
        }), 401

    if user["password"] != password:

        return jsonify({
            "message": "Invalid email or password."
        }), 401

    session["user_id"] = user["id"]
    session["user_name"] = user["name"]

    return jsonify({

        "message": "Login successful!",

        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "preferred_language": user["preferred_language"],
            "xp": user["xp"],
            "coins": user["coins"],
            "streak": user["streak"]
        }

    }), 200


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard", methods=["GET"])
def dashboard():

    if "user_id" not in session:

        return jsonify({
            "message": "Please login first."
        }), 401

    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )

    cursor.execute(
        """
        SELECT
            id,
            name,
            email,
            preferred_language,
            xp,
            coins,
            streak
        FROM users
        WHERE id = %s
        """,
        (session["user_id"],)
    )

    user = cursor.fetchone()

    cursor.close()

    if user is None:

        session.clear()

        return jsonify({
            "message": "User not found."
        }), 404

    return jsonify({
        "message": "Dashboard loaded successfully.",
        "user": user
    }), 200


# =========================================================
# CLAIM COINS FROM COIN RUNNER GAME
# =========================================================

@app.route("/claim-coins", methods=["POST"])
def claim_coins():

    if "user_id" not in session:

        return jsonify({
            "message": "Please login first."
        }), 401

    data = request.get_json() or {}
    amount = data.get("amount", 0)

    try:
        amount = int(amount)
    except (TypeError, ValueError):
        amount = 0

    if amount < 0 or amount > 50:
        return jsonify({
            "message": "Invalid coin amount."
        }), 400

    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )

    cursor.execute(
        """
        SELECT coins
        FROM users
        WHERE id = %s
        """,
        (session["user_id"],)
    )

    user = cursor.fetchone()

    if user is None:

        cursor.close()

        return jsonify({
            "message": "User not found."
        }), 404

    current_coins = max(
        0,
        int(user.get("coins") or 0)
    )

    new_coins = current_coins + amount

    cursor.execute(
        """
        UPDATE users
        SET coins = %s
        WHERE id = %s
        """,
        (
            new_coins,
            session["user_id"]
        )
    )

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Coins claimed successfully.",
        "coins_earned": amount,
        "coins": new_coins
    }), 200


# =========================================================
# GET ALL SUBJECTS
# =========================================================

@app.route("/subjects", methods=["GET"])
def get_subjects():

    if "user_id" not in session:

        return jsonify({
            "message": "Please login first."
        }), 401

    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )

    cursor.execute(
        """
        SELECT
            id,
            subject_name,
            description,
            icon
        FROM subjects
        ORDER BY id
        """
    )

    subjects = cursor.fetchall()

    cursor.close()

    return jsonify({
        "message": "Subjects loaded successfully.",
        "subjects": subjects
    }), 200


# =========================================================
# COMPLETE LEVEL
# =========================================================

@app.route("/complete-level", methods=["POST"])
def complete_level():

    if "user_id" not in session:

        return jsonify({
            "message": "Please login first."
        }), 401

    data = request.get_json() or {}

    level = data.get("level")

    if level != 1:

        return jsonify({
            "message": "Invalid level."
        }), 400

    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )

    cursor.execute(
        """
        SELECT
            xp,
            coins
        FROM users
        WHERE id = %s
        """,
        (session["user_id"],)
    )

    user = cursor.fetchone()

    if user is None:

        cursor.close()

        return jsonify({
            "message": "User not found."
        }), 404

    xp_reward = 100
    coin_reward = 20

    new_xp = user["xp"] + xp_reward
    new_coins = user["coins"] + coin_reward

    cursor.execute(
        """
        UPDATE users
        SET
            xp = %s,
            coins = %s
        WHERE id = %s
        """,
        (
            new_xp,
            new_coins,
            session["user_id"]
        )
    )

    db.commit()
    cursor.close()

    return jsonify({

        "message": "Level 1 completed!",

        "reward": {
            "xp": xp_reward,
            "coins": coin_reward
        },

        "progress": {
            "xp": new_xp,
            "coins": new_coins
        }

    }), 200


# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout", methods=["POST"])
def logout():

    session.clear()

    return jsonify({
        "message": "Logged out successfully."
    }), 200


# =========================================================
# LEARNING JOURNAL + NLP
# =========================================================

@app.route("/learning-journal", methods=["POST"])
def learning_journal():

    if "user_id" not in session:

        return jsonify({
            "message": "Please login first."
        }), 401

    data = request.get_json() or {}

    journal_text = data.get("journal_text")
    subject_id = data.get("subject_id")

    if not journal_text:

        return jsonify({
            "message": "Journal text is required."
        }), 400

    if not subject_id:

        return jsonify({
            "message": "Subject ID is required."
        }), 400

    processed_words = preprocessing(
        journal_text
    )

    topic_result = detect_topic(
        journal_text
    )

    detected_topic = topic_result.get(
        "topic",
        "Unknown"
    )

    topic_confidence = topic_result.get(
        "confidence",
        0
    )

    gap_result = detect_knowledge_gap(
        journal_text
    )

    gap_detected = gap_result.get(
        "gap_detected",
        False
    )

    knowledge_gap = gap_result.get(
        "message",
        "No knowledge gap detected."
    )

    recommended_action = gap_result.get(
        "side_quest",
        "Continue learning and practice."
    )

    if gap_detected:
        understanding_status = "Weak"
    else:
        understanding_status = "Good"

    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO learning_journal
        (
            user_id,
            subject_id,
            journal_text,
            detected_topic,
            understanding_status,
            knowledge_gap,
            recommended_action
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            session["user_id"],
            subject_id,
            journal_text,
            detected_topic,
            understanding_status,
            knowledge_gap,
            recommended_action
        )
    )

    db.commit()
    cursor.close()

    return jsonify({

        "message":
            "Learning journal analyzed successfully.",

        "nlp_analysis": {

            "processed_words":
                processed_words,

            "topic":
                detected_topic,

            "topic_confidence":
                topic_confidence,

            "understanding_status":
                understanding_status,

            "knowledge_gap_detected":
                gap_detected,

            "knowledge_gap":
                knowledge_gap,

            "recommended_action":
                recommended_action
        }

    }), 201


# =========================================================
# GET LEVELS FOR A SUBJECT
# =========================================================

@app.route("/levels/<int:subject_id>", methods=["GET"])
def get_levels(subject_id):

    if "user_id" not in session:

        return jsonify({
            "message": "Please login first."
        }), 401

    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )

    cursor.execute(
        """
        SELECT
            id,
            subject_id,
            level_number,
            level_name,
            topic,
            difficulty,
            video_url_en,
            video_url_te,
            video_url_hi,
            xp_reward,
            coin_reward
        FROM levels
        WHERE subject_id = %s
        ORDER BY level_number
        """,
        (subject_id,)
    )

    levels = cursor.fetchall()

    cursor.execute(
        """
        SELECT
            l.level_number,
            p.completed
        FROM levels l
        LEFT JOIN progress p
            ON p.level_id = l.id
            AND p.user_id = %s
        WHERE l.subject_id = %s
        ORDER BY l.level_number
        """,
        (
            session["user_id"],
            subject_id
        )
    )

    progress_rows = cursor.fetchall()

    completed_levels = {
        int(row["level_number"])
        for row in progress_rows
        if row["completed"]
    }

    for level in levels:

        level_number = int(
            level["level_number"]
        )

        level["completed"] = (
            level_number in completed_levels
        )

        level["unlocked"] = (
            level_number == 1
            or
            (level_number - 1)
            in completed_levels
        )

    cursor.close()

    return jsonify({
        "message":
            "Levels loaded successfully.",

        "levels":
            levels

    }), 200


# =========================================================
# GET QUIZZES FOR A LEVEL
# =========================================================

@app.route("/quizzes/<int:level_id>", methods=["GET"])
def get_quizzes(level_id):

    if "user_id" not in session:

        return jsonify({
            "message": "Please login first."
        }), 401

    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )

    cursor.execute(
        """
        SELECT
            id,
            level_id,

            question_en,
            question_te,
            question_hi,

            option_a_en,
            option_b_en,
            option_c_en,
            option_d_en,

            option_a_te,
            option_b_te,
            option_c_te,
            option_d_te,

            option_a_hi,
            option_b_hi,
            option_c_hi,
            option_d_hi,

            explanation_en,
            xp_reward

        FROM quizzes

        WHERE level_id = %s

        ORDER BY id
        """,
        (level_id,)
    )

    quizzes = cursor.fetchall()

    cursor.close()

    if not quizzes:

        return jsonify({

            "message":
                "No quiz available for this level yet.",

            "quizzes":
                []

        }), 200

    return jsonify({

        "message":
            "Quizzes loaded successfully.",

        "quizzes":
            quizzes

    }), 200


# =========================================================
# SUBMIT QUIZ
# =========================================================

@app.route("/submit-quiz", methods=["POST"])
def submit_quiz():

    if "user_id" not in session:

        return jsonify({
            "message": "Please login first."
        }), 401

    data = request.get_json() or {}

    level_id = data.get("level_id")
    answers = data.get("answers", {})

    if not level_id:

        return jsonify({
            "message": "Level ID is required."
        }), 400

    user_id = session["user_id"]

    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )

    cursor.execute(
        """
        SELECT
            id,
            correct_answer,
            xp_reward
        FROM quizzes
        WHERE level_id = %s
        ORDER BY id
        """,
        (level_id,)
    )

    quizzes = cursor.fetchall()

    if not quizzes:

        cursor.close()

        return jsonify({
            "message":
                "No quiz available for this level."
        }), 404

    score = 0
    xp_earned = 0

    for index, quiz in enumerate(quizzes):

        user_answer = answers.get(
            str(index)
        )

        correct_answer = quiz[
            "correct_answer"
        ]

        if user_answer == correct_answer:

            score += 1

            xp_earned += quiz[
                "xp_reward"
            ]

    total = len(quizzes)

    cursor.execute(
        """
        SELECT
            xp_reward,
            coin_reward
        FROM levels
        WHERE id = %s
        """,
        (level_id,)
    )

    level = cursor.fetchone()

    if not level:

        cursor.close()

        return jsonify({
            "message":
                "Level not found."
        }), 404

    if score == total:

        xp_earned += level[
            "xp_reward"
        ]

        coins_earned = level[
            "coin_reward"
        ]

    else:

        coins_earned = 0

    cursor.execute(
        """
        SELECT
            id
        FROM progress
        WHERE user_id = %s
        AND level_id = %s
        """,
        (
            user_id,
            level_id
        )
    )

    existing_progress = cursor.fetchone()

    if existing_progress:

        cursor.execute(
            """
            UPDATE progress
            SET
                quiz_score = %s,
                xp_earned = %s,
                attempts = attempts + 1,
                completed = %s,
                completed_at = NOW()
            WHERE id = %s
            """,
            (
                score,
                xp_earned,
                1 if score == total else 0,
                existing_progress["id"]
            )
        )

    else:

        cursor.execute(
            """
            INSERT INTO progress
            (
                user_id,
                level_id,
                quiz_score,
                xp_earned,
                attempts,
                completed,
                completed_at
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                NOW()
            )
            """,
            (
                user_id,
                level_id,
                score,
                xp_earned,
                1,
                1 if score == total else 0
            )
        )

    cursor.execute(
        """
        UPDATE users
        SET
            xp = xp + %s,
            coins = coins + %s
        WHERE id = %s
        """,
        (
            xp_earned,
            coins_earned,
            user_id
        )
    )

    db.commit()

    cursor.close()

    return jsonify({

        "message":
            "Quiz submitted successfully.",

        "score":
            score,

        "total":
            total,

        "xp_earned":
            xp_earned,

        "coins_earned":
            coins_earned,

        "completed":
            score == total

    }), 200


# =========================================================
# START LEVEL
# =========================================================

@app.route(
    "/start-level/<int:level_id>",
    methods=["POST"]
)
def start_level(level_id):

    if "user_id" not in session:

        return jsonify({
            "message": "Please login first."
        }), 401

    user_id = session["user_id"]

    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )

    cursor.execute(
        """
        SELECT
            id,
            subject_id,
            level_number
        FROM levels
        WHERE id = %s
        """,
        (level_id,)
    )

    level = cursor.fetchone()

    if level is None:

        cursor.close()

        return jsonify({
            "message": "Level not found."
        }), 404

    cursor.execute(
        """
        SELECT coins
        FROM users
        WHERE id = %s
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:

        cursor.close()

        return jsonify({
            "message": "User not found."
        }), 404

    current_coins = int(
        user.get("coins") or 0
    )

    if current_coins < 10:

        cursor.close()

        return jsonify({
            "message":
                "You need at least 10 coins to open this level.",

            "coins":
                current_coins,

            "required_coins":
                10
        }), 400

    new_coins = current_coins - 10

    cursor.execute(
        """
        UPDATE users
        SET coins = %s
        WHERE id = %s
        """,
        (
            new_coins,
            user_id
        )
    )

    db.commit()

    cursor.close()

    return jsonify({

        "message":
            "Level opened. 10 coins deducted.",

        "coins_deducted":
            10,

        "coins":
            new_coins

    }), 200


# =========================================================
# GET SINGLE LEVEL
# =========================================================

@app.route(
    "/level/<int:level_id>",
    methods=["GET"]
)
def get_single_level(level_id):

    if "user_id" not in session:

        return jsonify({
            "message": "Please login first."
        }), 401

    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )

    cursor.execute(
        """
        SELECT
            id,
            subject_id,
            level_number,
            level_name,
            topic,
            difficulty,
            video_url_en,
            video_url_te,
            video_url_hi,
            xp_reward,
            coin_reward
        FROM levels
        WHERE id = %s
        """,
        (level_id,)
    )

    level = cursor.fetchone()

    cursor.close()

    if not level:

        return jsonify({
            "message":
                "Level not found."
        }), 404

    return jsonify({

        "message":
            "Level loaded successfully.",

        "level":
            level

    }), 200


# =========================================================
# SET LANGUAGE
# =========================================================

@app.route(
    "/set-language",
    methods=["POST"]
)
def set_language():

    data = request.get_json() or {}

    language = data.get(
        "language",
        "en"
    )

    if language not in [
        "en",
        "hi",
        "te"
    ]:

        return jsonify({
            "message": "Invalid language."
        }), 400

    session["language"] = language

    return jsonify({

        "message":
            "Language selected successfully!",

        "language":
            language

    }), 200