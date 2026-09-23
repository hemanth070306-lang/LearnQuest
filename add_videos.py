import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="learnquest",
    charset="utf8"
)

cursor = db.cursor()

# =========================================================
# VERIFIED COURSE VIDEOS
# =========================================================

# ---------- PYTHON ----------
python_en = "https://www.youtube.com/watch?v=rfscVS0vtbw"
python_hi = "https://www.youtube.com/watch?v=sRrkqjqTTQQ"
python_te = "https://www.youtube.com/watch?v=0c6JXSQKEP4"

# ---------- JAVA ----------
java_en = "https://www.youtube.com/watch?v=A74TOX803D0"
java_hi = "https://www.youtube.com/watch?v=qidXSSJl1II"
java_te = "https://www.youtube.com/watch?v=e-OS-FogDQM"

# ---------- MACHINE LEARNING ----------
ml_en = "https://www.youtube.com/watch?v=QRcd7_JeUeU"
ml_hi = "https://www.youtube.com/watch?v=OuPMVdski3E"
ml_te = "https://www.youtube.com/watch?v=HYM7XL52XZQ"

# ---------- NLP ----------
nlp_en = "https://www.youtube.com/watch?v=8rXD5-xhemo"
nlp_hi = "https://www.youtube.com/watch?v=gpH20YKBGs8"
nlp_te = "https://www.youtube.com/watch?v=yQOgrIvr5aU"


# =========================================================
# UPDATE PYTHON LEVELS 1-5
# =========================================================

for level_id in range(1, 6):

    cursor.execute(
        """
        UPDATE levels
        SET
            video_url_en = %s,
            video_url_hi = %s,
            video_url_te = %s
        WHERE id = %s
        """,
        (
            python_en,
            python_hi,
            python_te,
            level_id
        )
    )


# =========================================================
# UPDATE JAVA LEVELS 1-5
# IDs 6-10
# =========================================================

for level_id in range(6, 11):

    cursor.execute(
        """
        UPDATE levels
        SET
            video_url_en = %s,
            video_url_hi = %s,
            video_url_te = %s
        WHERE id = %s
        """,
        (
            java_en,
            java_hi,
            java_te,
            level_id
        )
    )


# =========================================================
# UPDATE MACHINE LEARNING LEVELS 1-5
# IDs 21-25
# =========================================================

for level_id in range(21, 26):

    cursor.execute(
        """
        UPDATE levels
        SET
            video_url_en = %s,
            video_url_hi = %s,
            video_url_te = %s
        WHERE id = %s
        """,
        (
            ml_en,
            ml_hi,
            ml_te,
            level_id
        )
    )


# =========================================================
# UPDATE NLP LEVELS 1-5
# IDs 26-30
# =========================================================

for level_id in range(26, 31):

    cursor.execute(
        """
        UPDATE levels
        SET
            video_url_en = %s,
            video_url_hi = %s,
            video_url_te = %s
        WHERE id = %s
        """,
        (
            nlp_en,
            nlp_hi,
            nlp_te,
            level_id
        )
    )


db.commit()

print("====================================")
print("ALL VIDEO LINKS UPDATED SUCCESSFULLY")
print("====================================")

cursor.execute(
    """
    SELECT
        id,
        topic,
        video_url_en,
        video_url_hi,
        video_url_te
    FROM levels
    WHERE id IN (
        1,2,3,4,5,
        6,7,8,9,10,
        21,22,23,24,25,
        26,27,28,29,30
    )
    ORDER BY id
    """
)

for row in cursor.fetchall():
    print(row)

cursor.close()
db.close()