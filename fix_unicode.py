import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="learnquest",
    charset="utf8"
)

cursor = db.cursor()

data = {
    1: (
        "पाइथन में किसी वेरिएबल को मान देने के लिए किस चिन्ह का उपयोग किया जाता है?",
        "పైథాన్‌లో వేరియబుల్‌కు విలువ కేటాయించడానికి ఏ గుర్తును ఉపయోగిస్తారు?"
    ),
    6: (
        "पाइथन में टेक्स्ट को स्टोर करने के लिए किस डेटा टाइप का उपयोग किया जाता है?",
        "పైథాన్‌లో టెక్స్ట్‌ను నిల్వ చేయడానికి ఏ డేటా టైప్‌ను ఉపయోగిస్తారు?"
    ),
    7: (
        "पाइथन में घातांक के लिए किस ऑपरेटर का उपयोग किया जाता है?",
        "పైథాన్‌లో ఘాతాంకం కోసం ఏ ఆపరేటర్‌ను ఉపయోగిస్తారు?"
    ),
    8: (
        "पाइथन में किसी सीक्वेंस पर इटरेट करने के लिए आमतौर पर किस लूप का उपयोग किया जाता है?",
        "పైథాన్‌లో ఒక సీక్వెన్స్‌పై ఇటరేట్ చేయడానికి సాధారణంగా ఏ లూప్‌ను ఉపయోగిస్తారు?"
    ),
    9: (
        "पाइथन में फ़ंक्शन को परिभाषित करने के लिए किस कीवर्ड का उपयोग किया जाता है?",
        "పైథాన్‌లో ఫంక్షన్‌ను నిర్వచించడానికి ఏ కీవర్డ్‌ను ఉపయోగిస్తారు?"
    )
}

for quiz_id, (hindi, telugu) in data.items():
    cursor.execute(
        "UPDATE quizzes SET question_hi=%s, question_te=%s WHERE id=%s",
        (hindi, telugu, quiz_id)
    )

db.commit()

print("Unicode questions updated successfully!")

cursor.execute(
    "SELECT id, question_hi, question_te "
    "FROM quizzes "
    "WHERE id IN (1,6,7,8,9) "
    "ORDER BY id"
)

for row in cursor.fetchall():
    print(row)

cursor.close()
db.close()