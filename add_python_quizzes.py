import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="learnquest",
    charset="utf8"
)

cursor = db.cursor()

questions = [
    # ---------------- LEVEL 2: PYTHON DATA TYPES ----------------

    {
        "level_id": 2,
        "question_en": "Which data type is used to store a whole number in Python?",
        "question_te": "పైథాన్‌లో పూర్ణ సంఖ్యను నిల్వ చేయడానికి ఏ డేటా టైప్‌ను ఉపయోగిస్తారు?",
        "question_hi": "पाइथन में पूर्ण संख्या को स्टोर करने के लिए किस डेटा टाइप का उपयोग किया जाता है?",
        "a_en": "int", "b_en": "float", "c_en": "str", "d_en": "bool",
        "a_te": "int", "b_te": "float", "c_te": "str", "d_te": "bool",
        "a_hi": "int", "b_hi": "float", "c_hi": "str", "d_hi": "bool",
        "correct": "A",
        "explanation": "The int data type stores whole numbers in Python."
    },

    {
        "level_id": 2,
        "question_en": "Which data type is used to store decimal numbers in Python?",
        "question_te": "పైథాన్‌లో దశాంశ సంఖ్యలను నిల్వ చేయడానికి ఏ డేటా టైప్‌ను ఉపయోగిస్తారు?",
        "question_hi": "पाइथन में दशमलव संख्याओं को स्टोर करने के लिए किस डेटा टाइप का उपयोग किया जाता है?",
        "a_en": "int", "b_en": "float", "c_en": "str", "d_en": "bool",
        "a_te": "int", "b_te": "float", "c_te": "str", "d_te": "bool",
        "a_hi": "int", "b_hi": "float", "c_hi": "str", "d_hi": "bool",
        "correct": "B",
        "explanation": "The float data type stores numbers with decimal values."
    },

    {
        "level_id": 2,
        "question_en": "Which data type stores True or False values in Python?",
        "question_te": "పైథాన్‌లో True లేదా False విలువలను ఏ డేటా టైప్ నిల్వ చేస్తుంది?",
        "question_hi": "पाइथन में True या False मानों को कौन सा डेटा टाइप स्टोर करता है?",
        "a_en": "int", "b_en": "float", "c_en": "bool", "d_en": "str",
        "a_te": "int", "b_te": "float", "c_te": "bool", "d_te": "str",
        "a_hi": "int", "b_hi": "float", "c_hi": "bool", "d_hi": "str",
        "correct": "C",
        "explanation": "The bool data type represents True or False values."
    },

    {
        "level_id": 2,
        "question_en": "Which Python data type is commonly used to store multiple values in an ordered collection?",
        "question_te": "పైథాన్‌లో అనేక విలువలను క్రమబద్ధమైన కలెక్షన్‌గా నిల్వ చేయడానికి సాధారణంగా ఏ డేటా టైప్‌ను ఉపయోగిస్తారు?",
        "question_hi": "पाइथन में कई मानों को क्रमबद्ध संग्रह के रूप में स्टोर करने के लिए सामान्यतः किस डेटा टाइप का उपयोग किया जाता है?",
        "a_en": "list", "b_en": "int", "c_en": "float", "d_en": "bool",
        "a_te": "list", "b_te": "int", "c_te": "float", "d_te": "bool",
        "a_hi": "list", "b_hi": "int", "c_hi": "float", "d_hi": "bool",
        "correct": "A",
        "explanation": "A list stores multiple values in an ordered and changeable collection."
    },

    # ---------------- LEVEL 3: PYTHON OPERATORS ----------------

    {
        "level_id": 3,
        "question_en": "Which operator is used for addition in Python?",
        "question_te": "పైథాన్‌లో కూడిక కోసం ఏ ఆపరేటర్‌ను ఉపయోగిస్తారు?",
        "question_hi": "पाइथन में जोड़ के लिए किस ऑपरेटर का उपयोग किया जाता है?",
        "a_en": "+", "b_en": "-", "c_en": "*", "d_en": "/",
        "a_te": "+", "b_te": "-", "c_te": "*", "d_te": "/",
        "a_hi": "+", "b_hi": "-", "c_hi": "*", "d_hi": "/",
        "correct": "A",
        "explanation": "The + operator performs addition in Python."
    },

    {
        "level_id": 3,
        "question_en": "Which operator is used for subtraction in Python?",
        "question_te": "పైథాన్‌లో తీసివేత కోసం ఏ ఆపరేటర్‌ను ఉపయోగిస్తారు?",
        "question_hi": "पाइथन में घटाव के लिए किस ऑपरेटर का उपयोग किया जाता है?",
        "a_en": "+", "b_en": "-", "c_en": "*", "d_en": "%",
        "a_te": "+", "b_te": "-", "c_te": "*", "d_te": "%",
        "a_hi": "+", "b_hi": "-", "c_hi": "*", "d_hi": "%",
        "correct": "B",
        "explanation": "The - operator performs subtraction in Python."
    },

    {
        "level_id": 3,
        "question_en": "Which operator is used for multiplication in Python?",
        "question_te": "పైథాన్‌లో గుణకారం కోసం ఏ ఆపరేటర్‌ను ఉపయోగిస్తారు?",
        "question_hi": "पाइथन में गुणा के लिए किस ऑपरेटर का उपयोग किया जाता है?",
        "a_en": "+", "b_en": "-", "c_en": "*", "d_en": "/",
        "a_te": "+", "b_te": "-", "c_te": "*", "d_te": "/",
        "a_hi": "+", "b_hi": "-", "c_hi": "*", "d_hi": "/",
        "correct": "C",
        "explanation": "The * operator performs multiplication in Python."
    },

    {
        "level_id": 3,
        "question_en": "Which operator returns the remainder after division in Python?",
        "question_te": "పైథాన్‌లో భాగహారం చేసిన తర్వాత మిగిలిన శేషాన్ని ఏ ఆపరేటర్ ఇస్తుంది?",
        "question_hi": "पाइथन में भाग देने के बाद शेषफल कौन सा ऑपरेटर देता है?",
        "a_en": "/", "b_en": "//", "c_en": "%", "d_en": "**",
        "a_te": "/", "b_te": "//", "c_te": "%", "d_te": "**",
        "a_hi": "/", "b_hi": "//", "c_hi": "%", "d_hi": "**",
        "correct": "C",
        "explanation": "The % operator returns the remainder of a division."
    },

    # ---------------- LEVEL 4: PYTHON LOOPS ----------------

    {
        "level_id": 4,
        "question_en": "Which loop is commonly used when the number of iterations is known?",
        "question_te": "ఎన్ని సార్లు లూప్ నడవాలో ముందే తెలిసినప్పుడు సాధారణంగా ఏ లూప్‌ను ఉపయోగిస్తారు?",
        "question_hi": "जब लूप कितनी बार चलेगा यह पहले से पता हो, तब सामान्यतः किस लूप का उपयोग किया जाता है?",
        "a_en": "for loop", "b_en": "while loop", "c_en": "if loop", "d_en": "switch loop",
        "a_te": "for లూప్", "b_te": "while లూప్", "c_te": "if లూప్", "d_te": "switch లూప్",
        "a_hi": "for लूप", "b_hi": "while लूप", "c_hi": "if लूप", "d_hi": "switch लूप",
        "correct": "A",
        "explanation": "A for loop is commonly used to iterate over a known sequence or range."
    },

    {
        "level_id": 4,
        "question_en": "Which statement immediately stops a loop in Python?",
        "question_te": "పైథాన్‌లో లూప్‌ను వెంటనే ఆపడానికి ఏ స్టేట్‌మెంట్‌ను ఉపయోగిస్తారు?",
        "question_hi": "पाइथन में लूप को तुरंत रोकने के लिए किस स्टेटमेंट का उपयोग किया जाता है?",
        "a_en": "stop", "b_en": "break", "c_en": "exitloop", "d_en": "end",
        "a_te": "stop", "b_te": "break", "c_te": "exitloop", "d_te": "end",
        "a_hi": "stop", "b_hi": "break", "c_hi": "exitloop", "d_hi": "end",
        "correct": "B",
        "explanation": "The break statement immediately terminates the current loop."
    },

    {
        "level_id": 4,
        "question_en": "Which statement skips the remaining code of the current loop iteration?",
        "question_te": "ప్రస్తుత లూప్ ఇటరేషన్‌లో మిగిలిన కోడ్‌ను దాటవేయడానికి ఏ స్టేట్‌మెంట్‌ను ఉపయోగిస్తారు?",
        "question_hi": "लूप की वर्तमान iteration के बाकी कोड को छोड़ने के लिए किस स्टेटमेंट का उपयोग किया जाता है?",
        "a_en": "break", "b_en": "skip", "c_en": "continue", "d_en": "pass",
        "a_te": "break", "b_te": "skip", "c_te": "continue", "d_te": "pass",
        "a_hi": "break", "b_hi": "skip", "c_hi": "continue", "d_hi": "pass",
        "correct": "C",
        "explanation": "The continue statement skips to the next loop iteration."
    },

    {
        "level_id": 4,
        "question_en": "Which keyword is used to create a loop that continues while a condition is true?",
        "question_te": "ఒక షరతు True గా ఉన్నంత వరకు కొనసాగుతున్న లూప్‌ను సృష్టించడానికి ఏ కీవర్డ్‌ను ఉపయోగిస్తారు?",
        "question_hi": "किसी शर्त के True रहने तक चलने वाला लूप बनाने के लिए किस कीवर्ड का उपयोग किया जाता है?",
        "a_en": "for", "b_en": "while", "c_en": "loop", "d_en": "repeat",
        "a_te": "for", "b_te": "while", "c_te": "loop", "d_te": "repeat",
        "a_hi": "for", "b_hi": "while", "c_hi": "loop", "d_hi": "repeat",
        "correct": "B",
        "explanation": "The while keyword creates a loop that runs while its condition is true."
    },

    # ---------------- LEVEL 5: PYTHON FUNCTIONS ----------------

    {
        "level_id": 5,
        "question_en": "Which keyword is used to return a value from a Python function?",
        "question_te": "పైథాన్ ఫంక్షన్ నుండి విలువను తిరిగి ఇవ్వడానికి ఏ కీవర్డ్‌ను ఉపయోగిస్తారు?",
        "question_hi": "पाइथन फ़ंक्शन से मान वापस करने के लिए किस कीवर्ड का उपयोग किया जाता है?",
        "a_en": "return", "b_en": "send", "c_en": "output", "d_en": "back",
        "a_te": "return", "b_te": "send", "c_te": "output", "d_te": "back",
        "a_hi": "return", "b_hi": "send", "c_hi": "output", "d_hi": "back",
        "correct": "A",
        "explanation": "The return keyword sends a value back from a function."
    },

    {
        "level_id": 5,
        "question_en": "What are the values passed to a function when it is called?",
        "question_te": "పైథాన్‌లో ఫంక్షన్‌ను కాల్ చేసినప్పుడు దానికి పంపే విలువలను ఏమంటారు?",
        "question_hi": "पाइथन में फ़ंक्शन को कॉल करते समय पास किए जाने वाले मानों को क्या कहते हैं?",
        "a_en": "arguments", "b_en": "loops", "c_en": "operators", "d_en": "classes",
        "a_te": "arguments", "b_te": "loops", "c_te": "operators", "d_te": "classes",
        "a_hi": "arguments", "b_hi": "loops", "c_hi": "operators", "d_hi": "classes",
        "correct": "A",
        "explanation": "Arguments are the values supplied to a function when it is called."
    },

    {
        "level_id": 5,
        "question_en": "Which function is used to display output on the screen in Python?",
        "question_te": "పైథాన్‌లో స్క్రీన్‌పై అవుట్‌పుట్‌ను చూపించడానికి ఏ ఫంక్షన్‌ను ఉపయోగిస్తారు?",
        "question_hi": "पाइथन में स्क्रीन पर आउटपुट दिखाने के लिए किस फ़ंक्शन का उपयोग किया जाता है?",
        "a_en": "input()", "b_en": "display()", "c_en": "print()", "d_en": "show()",
        "a_te": "input()", "b_te": "display()", "c_te": "print()", "d_te": "show()",
        "a_hi": "input()", "b_hi": "display()", "c_hi": "print()", "d_hi": "show()",
        "correct": "C",
        "explanation": "The print() function displays output on the screen."
    },

    {
        "level_id": 5,
        "question_en": "What is the purpose of a function in Python?",
        "question_te": "పైథాన్‌లో ఫంక్షన్ యొక్క ప్రధాన ఉద్దేశ్యం ఏమిటి?",
        "question_hi": "पाइथन में फ़ंक्शन का मुख्य उद्देश्य क्या है?",
        "a_en": "Reuse a block of code",
        "b_en": "Delete a program",
        "c_en": "Create only variables",
        "d_en": "Stop the computer",
        "a_te": "కోడ్ బ్లాక్‌ను మళ్లీ ఉపయోగించడం",
        "b_te": "ప్రోగ్రామ్‌ను తొలగించడం",
        "c_te": "వేరియబుల్స్ మాత్రమే సృష్టించడం",
        "d_te": "కంప్యూటర్‌ను ఆపడం",
        "a_hi": "कोड के एक ब्लॉक को दोबारा उपयोग करना",
        "b_hi": "प्रोग्राम को हटाना",
        "c_hi": "केवल वेरिएबल बनाना",
        "d_hi": "कंप्यूटर को बंद करना",
        "correct": "A",
        "explanation": "Functions organize reusable blocks of code."
    }
]


sql = """
INSERT INTO quizzes (
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
    correct_answer,
    explanation_en,
    xp_reward
)
VALUES (
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s
)
"""

for q in questions:
    values = (
        q["level_id"],
        q["question_en"],
        q["question_te"],
        q["question_hi"],

        q["a_en"],
        q["b_en"],
        q["c_en"],
        q["d_en"],

        q["a_te"],
        q["b_te"],
        q["c_te"],
        q["d_te"],

        q["a_hi"],
        q["b_hi"],
        q["c_hi"],
        q["d_hi"],

        q["correct"],
        q["explanation"],
        30
    )

    cursor.execute(sql, values)

db.commit()

print("Python quiz questions added successfully!")
print("New questions inserted:", len(questions))

cursor.close()
db.close()