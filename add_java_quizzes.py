import mysql.connector

# ==========================================
# CONNECT TO MYSQL
# ==========================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="learnquest",
    charset="utf8"
)

cursor = db.cursor()

# ==========================================
# JAVA QUIZ QUESTIONS
# 5 QUESTIONS PER LEVEL
# TOTAL = 25 QUESTIONS
# ==========================================

questions = [

    # ==========================================
    # LEVEL 1 - JAVA VARIABLES
    # level_id = 6
    # ==========================================

    (
        6,
        "Which symbol is used to end a statement in Java?",
        ";", "{", ":", ".",

        "जावा में स्टेटमेंट को समाप्त करने के लिए किस चिन्ह का उपयोग किया जाता है?",
        ";", "{", ":", ".",

        "జావాలో స్టేట్‌మెంట్‌ను ముగించడానికి ఏ గుర్తును ఉపయోగిస్తారు?",
        ";", "{", ":", ".",

        "A semicolon is used to end most Java statements.",
        100
    ),

    (
        6,
        "Which keyword is used to declare an integer variable in Java?",
        "int", "integer", "num", "number",

        "जावा में पूर्णांक वेरिएबल घोषित करने के लिए किस कीवर्ड का उपयोग किया जाता है?",
        "int", "integer", "num", "number",

        "జావాలో పూర్ణాంక వేరియబుల్‌ను ప్రకటించడానికి ఏ కీవర్డ్‌ను ఉపయోగిస్తారు?",
        "int", "integer", "num", "number",

        "The int keyword declares an integer variable in Java.",
        100
    ),

    (
        6,
        "Which is a valid Java variable declaration?",
        "int age = 20;",
        "age int = 20;",
        "integer age = 20;",
        "var int age = 20;",

        "इनमें से कौन-सा एक मान्य Java वेरिएबल डिक्लेरेशन है?",
        "int age = 20;",
        "age int = 20;",
        "integer age = 20;",
        "var int age = 20;",

        "క్రింది వాటిలో సరైన Java వేరియబుల్ డిక్లరేషన్ ఏది?",
        "int age = 20;",
        "age int = 20;",
        "integer age = 20;",
        "var int age = 20;",

        "A Java variable declaration places the data type before the variable name.",
        100
    ),

    (
        6,
        "Which method is the entry point of a Java program?",
        "main()", "start()", "run()", "execute()",

        "जावा प्रोग्राम का एंट्री पॉइंट कौन-सा मेथड है?",
        "main()", "start()", "run()", "execute()",

        "జావా ప్రోగ్రామ్ యొక్క ఎంట్రీ పాయింట్ ఏ మెథడ్?",
        "main()", "start()", "run()", "execute()",

        "The main() method is the standard entry point for a Java application.",
        100
    ),

    (
        6,
        "Which keyword is used to create an object in Java?",
        "new", "object", "create", "make",

        "जावा में ऑब्जेक्ट बनाने के लिए किस कीवर्ड का उपयोग किया जाता है?",
        "new", "object", "create", "make",

        "జావాలో ఆబ్జెక్ట్‌ను సృష్టించడానికి ఏ కీవర్డ్‌ను ఉపయోగిస్తారు?",
        "new", "object", "create", "make",

        "The new keyword creates a new object in Java.",
        100
    ),


    # ==========================================
    # LEVEL 2 - JAVA DATA TYPES
    # level_id = 7
    # ==========================================

    (
        7,
        "Which data type is used to store whole numbers in Java?",
        "int", "float", "char", "boolean",

        "जावा में पूर्ण संख्याओं को स्टोर करने के लिए किस डेटा टाइप का उपयोग किया जाता है?",
        "int", "float", "char", "boolean",

        "జావాలో పూర్ణ సంఖ్యలను నిల్వ చేయడానికి ఏ డేటా టైప్‌ను ఉపయోగిస్తారు?",
        "int", "float", "char", "boolean",

        "The int data type stores whole-number values.",
        100
    ),

    (
        7,
        "Which data type is used to store a single character in Java?",
        "char", "String", "character", "text",

        "जावा में एक अक्षर को स्टोर करने के लिए किस डेटा टाइप का उपयोग किया जाता है?",
        "char", "String", "character", "text",

        "జావాలో ఒక అక్షరాన్ని నిల్వ చేయడానికి ఏ డేటా టైప్‌ను ఉపయోగిస్తారు?",
        "char", "String", "character", "text",

        "The char data type stores a single character.",
        100
    ),

    (
        7,
        "Which data type stores true or false values?",
        "boolean", "bool", "logical", "bit",

        "कौन-सा डेटा टाइप true या false मानों को स्टोर करता है?",
        "boolean", "bool", "logical", "bit",

        "true లేదా false విలువలను ఏ డేటా టైప్ నిల్వ చేస్తుంది?",
        "boolean", "bool", "logical", "bit",

        "The boolean data type represents true or false values.",
        100
    ),

    (
        7,
        "Which data type is commonly used to store decimal values in Java?",
        "double", "int", "char", "boolean",

        "जावा में दशमलव मानों को स्टोर करने के लिए सामान्यतः किस डेटा टाइप का उपयोग किया जाता है?",
        "double", "int", "char", "boolean",

        "జావాలో దశాంశ విలువలను నిల్వ చేయడానికి సాధారణంగా ఏ డేటా టైప్‌ను ఉపయోగిస్తారు?",
        "double", "int", "char", "boolean",

        "The double data type is commonly used for decimal floating-point values.",
        100
    ),

    (
        7,
        "Which of these is a reference type in Java?",
        "String", "int", "double", "boolean",

        "इनमें से कौन-सा Java में एक रेफरेंस टाइप है?",
        "String", "int", "double", "boolean",

        "వీటిలో Javaలో reference type ఏది?",
        "String", "int", "double", "boolean",

        "String is a class and therefore is a reference type.",
        100
    ),


    # ==========================================
    # LEVEL 3 - JAVA OPERATORS
    # level_id = 8
    # ==========================================

    (
        8,
        "Which operator is used for addition in Java?",
        "+", "-", "*", "/",

        "जावा में जोड़ के लिए किस ऑपरेटर का उपयोग किया जाता है?",
        "+", "-", "*", "/",

        "జావాలో కూడిక కోసం ఏ ఆపరేటర్‌ను ఉపయోగిస్తారు?",
        "+", "-", "*", "/",

        "The plus operator performs addition.",
        100
    ),

    (
        8,
        "Which operator checks whether two values are equal?",
        "==", "=", "!=", "<=",

        "कौन-सा ऑपरेटर जाँचता है कि दो मान बराबर हैं?",
        "==", "=", "!=", "<=",

        "రెండు విలువలు సమానంగా ఉన్నాయో లేదో ఏ ఆపరేటర్ తనిఖీ చేస్తుంది?",
        "==", "=", "!=", "<=",

        "The equality operator == compares two values for equality.",
        100
    ),

    (
        8,
        "Which operator is used for logical AND in Java?",
        "&&", "||", "!", "&",

        "जावा में लॉजिकल AND के लिए किस ऑपरेटर का उपयोग किया जाता है?",
        "&&", "||", "!", "&",

        "జావాలో logical AND కోసం ఏ ఆపరేటర్‌ను ఉపయోగిస్తారు?",
        "&&", "||", "!", "&",

        "The && operator performs logical AND.",
        100
    ),

    (
        8,
        "Which operator is used to find the remainder after division?",
        "%", "/", "//", "rem",

        "भाग देने के बाद शेषफल ज्ञात करने के लिए किस ऑपरेटर का उपयोग किया जाता है?",
        "%", "/", "//", "rem",

        "భాగించిన తర్వాత మిగిలిన శేషాన్ని కనుగొనడానికి ఏ ఆపరేటర్‌ను ఉపయోగిస్తారు?",
        "%", "/", "//", "rem",

        "The percent operator returns the remainder of integer division.",
        100
    ),

    (
        8,
        "What is the result of 10 > 5 in Java?",
        "true", "false", "10", "5",

        "जावा में 10 > 5 का परिणाम क्या होगा?",
        "true", "false", "10", "5",

        "జావాలో 10 > 5 ఫలితం ఏమిటి?",
        "true", "false", "10", "5",

        "Since 10 is greater than 5, the comparison evaluates to true.",
        100
    ),


    # ==========================================
    # LEVEL 4 - JAVA LOOPS
    # level_id = 9
    # ==========================================

    (
        9,
        "Which loop is commonly used when the number of iterations is known?",
        "for loop", "while loop", "do-while loop", "if statement",

        "जब पुनरावृत्तियों की संख्या ज्ञात हो तो सामान्यतः किस लूप का उपयोग किया जाता है?",
        "for loop", "while loop", "do-while loop", "if statement",

        "ఎన్ని iterations చేయాలో ముందుగా తెలిసినప్పుడు సాధారణంగా ఏ లూప్‌ను ఉపయోగిస్తారు?",
        "for loop", "while loop", "do-while loop", "if statement",

        "A for loop is commonly used when the iteration count is known.",
        100
    ),

    (
        9,
        "Which loop checks its condition before executing the body?",
        "while loop", "do-while loop", "for-each loop", "switch loop",

        "कौन-सा लूप बॉडी को चलाने से पहले कंडीशन की जाँच करता है?",
        "while loop", "do-while loop", "for-each loop", "switch loop",

        "బాడీని అమలు చేయడానికి ముందు కండిషన్‌ను ఏ లూప్ తనిఖీ చేస్తుంది?",
        "while loop", "do-while loop", "for-each loop", "switch loop",

        "A while loop checks its condition before each iteration.",
        100
    ),

    (
        9,
        "Which statement immediately exits a loop in Java?",
        "break", "continue", "exitLoop", "stop",

        "जावा में कौन-सा स्टेटमेंट तुरंत लूप से बाहर निकलता है?",
        "break", "continue", "exitLoop", "stop",

        "జావాలో ఏ స్టేట్‌మెంట్ వెంటనే లూప్ నుండి బయటకు వస్తుంది?",
        "break", "continue", "exitLoop", "stop",

        "The break statement terminates the nearest loop or switch statement.",
        100
    ),

    (
        9,
        "Which statement skips the current iteration and continues with the next one?",
        "continue", "break", "skipLoop", "next",

        "कौन-सा स्टेटमेंट वर्तमान इटरेशन को छोड़कर अगले इटरेशन पर जाता है?",
        "continue", "break", "skipLoop", "next",

        "ప్రస్తుత iteration‌ను దాటవేసి తదుపరి iteration‌కు వెళ్లడానికి ఏ స్టేట్‌మెంట్ ఉపయోగిస్తారు?",
        "continue", "break", "skipLoop", "next",

        "The continue statement skips the rest of the current iteration.",
        100
    ),

    (
        9,
        "Which loop is guaranteed to execute its body at least once?",
        "do-while loop", "while loop", "for loop", "for-each loop",

        "कौन-सा लूप कम से कम एक बार अपनी बॉडी को चलाता है?",
        "do-while loop", "while loop", "for loop", "for-each loop",

        "ఏ లూప్ తన బాడీని కనీసం ఒకసారి అమలు చేస్తుంది?",
        "do-while loop", "while loop", "for loop", "for-each loop",

        "A do-while loop executes its body before checking the condition.",
        100
    ),


    # ==========================================
    # LEVEL 5 - JAVA METHODS
    # level_id = 10
    # ==========================================

    (
        10,
        "Which keyword is used to define a method that returns no value?",
        "void", "null", "empty", "none",

        "ऐसी मेथड को परिभाषित करने के लिए किस कीवर्ड का उपयोग किया जाता है जो कोई मान वापस नहीं करती?",
        "void", "null", "empty", "none",

        "ఏ విలువను return చేయని మెథడ్‌ను నిర్వచించడానికి ఏ కీవర్డ్‌ను ఉపయోగిస్తారు?",
        "void", "null", "empty", "none",

        "The void keyword specifies that a method does not return a value.",
        100
    ),

    (
        10,
        "Which keyword is used to return a value from a method?",
        "return", "send", "give", "output",

        "मेथड से मान वापस करने के लिए किस कीवर्ड का उपयोग किया जाता है?",
        "return", "send", "give", "output",

        "మెథడ్ నుండి విలువను తిరిగి ఇవ్వడానికి ఏ కీవర్డ్‌ను ఉపయోగిస్తారు?",
        "return", "send", "give", "output",

        "The return keyword sends a value back from a method.",
        100
    ),

    (
        10,
        "What is a method parameter?",
        "A value passed into a method",
        "A class name",
        "A loop condition",
        "A package name",

        "मेथड पैरामीटर क्या होता है?",
        "मेथड में पास किया गया मान",
        "एक क्लास का नाम",
        "एक लूप कंडीशन",
        "एक पैकेज का नाम",

        "మెథడ్ parameter అంటే ఏమిటి?",
        "మెథడ్‌కు పంపిన విలువ",
        "ఒక class పేరు",
        "ఒక loop condition",
        "ఒక package పేరు",

        "A method parameter is a variable that receives a value passed to the method.",
        100
    ),

    (
        10,
        "Which keyword refers to the current object inside a Java class?",
        "this", "self", "current", "object",

        "जावा क्लास के अंदर वर्तमान ऑब्जेक्ट को कौन-सा कीवर्ड संदर्भित करता है?",
        "this", "self", "current", "object",

        "జావా క్లాస్‌లో ప్రస్తుత ఆబ్జెక్ట్‌ను ఏ కీవర్డ్ సూచిస్తుంది?",
        "this", "self", "current", "object",

        "The this keyword refers to the current object.",
        100
    ),

    (
        10,
        "Which keyword allows a method to be called without creating an object of the class?",
        "static", "public", "private", "final",

        "कौन-सा कीवर्ड क्लास का ऑब्जेक्ट बनाए बिना मेथड को कॉल करने की अनुमति देता है?",
        "static", "public", "private", "final",

        "ఏ కీవర్డ్ class object‌ను సృష్టించకుండా మెథడ్‌ను call చేయడానికి అనుమతిస్తుంది?",
        "static", "public", "private", "final",

        "A static method belongs to the class rather than an individual object.",
        100
    )
]


# ==========================================
# INSERT QUERY
# ==========================================

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
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)
"""


# ==========================================
# CORRECT ANSWERS
# ==========================================

correct_answers = [
    ";",
    "int",
    "int age = 20;",
    "main()",
    "new",

    "int",
    "char",
    "boolean",
    "double",
    "String",

    "+",
    "==",
    "&&",
    "%",
    "true",

    "for loop",
    "while loop",
    "break",
    "continue",
    "do-while loop",

    "void",
    "return",
    "A value passed into a method",
    "this",
    "static"
]


# ==========================================
# INSERT ALL QUESTIONS
# ==========================================

for i, q in enumerate(questions):

    level_id = q[0]

    question_en = q[1]

    en_options = q[2:6]

    question_hi = q[6]

    hi_options = q[7:11]

    question_te = q[11]

    te_options = q[12:16]

    explanation_en = q[16]

    xp_reward = q[17]

    # Get correct answer text
    correct_text = correct_answers[i]

    # Find A/B/C/D position
    correct_index = en_options.index(correct_text)

    correct_answer = chr(65 + correct_index)

    values = (
        level_id,

        question_en,
        question_te,
        question_hi,

        en_options[0],
        en_options[1],
        en_options[2],
        en_options[3],

        te_options[0],
        te_options[1],
        te_options[2],
        te_options[3],

        hi_options[0],
        hi_options[1],
        hi_options[2],
        hi_options[3],

        correct_answer,

        explanation_en,

        xp_reward
    )

    cursor.execute(sql, values)


# ==========================================
# SAVE
# ==========================================

db.commit()

print("Java quiz questions added successfully!")
print("New questions inserted:", len(questions))


# ==========================================
# CLOSE CONNECTION
# ==========================================

cursor.close()
db.close()