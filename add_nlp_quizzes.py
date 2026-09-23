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

# ================= LEVEL 1 — NLP BASICS =================

(26, "What does NLP stand for?",
 "एनएलपी का पूरा नाम क्या है?",
 "NLP का पूरा नाम क्या है?",
 ["Natural Language Processing", "Natural Learning Process", "Neural Language Program", "Natural Logic Processing"],
 ["प्राकृतिक भाषा संसाधन", "प्राकृतिक अधिगम प्रक्रिया", "न्यूरल भाषा प्रोग्राम", "प्राकृतिक तर्क संसाधन"],
 ["నేచురల్ లాంగ్వేజ్ ప్రాసెసింగ్", "నేచురల్ లెర్నింగ్ ప్రాసెస్", "న్యూరల్ లాంగ్వేజ్ ప్రోగ్రామ్", "నేచురల్ లాజిక్ ప్రాసెసింగ్"],
 "A"),

(26, "What is the main goal of NLP?",
 "एनएलपी का मुख्य उद्देश्य क्या है?",
 "NLP యొక్క ప్రధాన లక్ష్యం ఏమిటి?",
 ["To enable computers to understand human language", "To design computer hardware", "To store images only", "To increase internet speed"],
 ["कंप्यूटर को मानव भाषा समझने में सक्षम बनाना", "कंप्यूटर हार्डवेयर डिजाइन करना", "केवल चित्र संग्रहित करना", "इंटरनेट की गति बढ़ाना"],
 ["కంప్యూటర్లు మానవ భాషను అర్థం చేసుకునేలా చేయడం", "కంప్యూటర్ హార్డ్‌వేర్‌ను రూపొందించడం", "చిత్రాలను మాత్రమే నిల్వ చేయడం", "ఇంటర్నెట్ వేగాన్ని పెంచడం"],
 "A"),

(26, "Which of these is an NLP application?",
 "इनमें से कौन सा एनएलपी का अनुप्रयोग है?",
 "వీటిలో ఏది NLP అప్లికేషన్?",
 ["Chatbots", "Computer assembly", "Battery charging", "Screen cleaning"],
 ["चैटबॉट", "कंप्यूटर असेंबली", "बैटरी चार्जिंग", "स्क्रीन सफाई"],
 ["చాట్‌బాట్‌లు", "కంప్యూటర్ అసెంబ్లీ", "బ్యాటరీ ఛార్జింగ్", "స్క్రీన్ శుభ్రపరచడం"],
 "A"),

(26, "Which type of data is mainly processed in NLP?",
 "एनएलपी में मुख्य रूप से किस प्रकार के डेटा को संसाधित किया जाता है?",
 "NLPలో ప్రధానంగా ఏ రకమైన డేటాను ప్రాసెస్ చేస్తారు?",
 ["Text and speech", "Only numbers", "Only images", "Only videos"],
 ["टेक्स्ट और भाषण", "केवल संख्याएँ", "केवल चित्र", "केवल वीडियो"],
 ["టెక్స్ట్ మరియు స్పీచ్", "సంఖ్యలు మాత్రమే", "చిత్రాలు మాత్రమే", "వీడియోలు మాత్రమే"],
 "A"),

(26, "Which field is closely related to NLP?",
 "एनएलपी किस क्षेत्र से निकटता से संबंधित है?",
 "NLP ఏ రంగంతో దగ్గరగా సంబంధం కలిగి ఉంది?",
 ["Artificial Intelligence", "Civil Engineering", "Mechanical Design", "Electrical Wiring"],
 ["कृत्रिम बुद्धिमत्ता", "सिविल इंजीनियरिंग", "मैकेनिकल डिजाइन", "इलेक्ट्रिकल वायरिंग"],
 ["కృత్రిమ మేధస్సు", "సివిల్ ఇంజినీరింగ్", "మెకానికల్ డిజైన్", "ఎలక్ట్రికల్ వైరింగ్"],
 "A"),

# ================= LEVEL 2 — TEXT PROCESSING =================

(27, "What is tokenization in NLP?",
 "एनएलपी में टोकनाइजेशन क्या है?",
 "NLPలో టోకనైజేషన్ అంటే ఏమిటి?",
 ["Splitting text into smaller units", "Converting text into images", "Deleting all text", "Encrypting a computer"],
 ["टेक्स्ट को छोटे भागों में विभाजित करना", "टेक्स्ट को चित्रों में बदलना", "सभी टेक्स्ट हटाना", "कंप्यूटर को एन्क्रिप्ट करना"],
 ["టెక్స్ట్‌ను చిన్న భాగాలుగా విభజించడం", "టెక్స్ట్‌ను చిత్రాలుగా మార్చడం", "అన్ని టెక్స్ట్‌ను తొలగించడం", "కంప్యూటర్‌ను ఎన్‌క్రిప్ట్ చేయడం"],
 "A"),

(27, "What does sentence tokenization divide a document into?",
 "सेंटेंस टोकनाइजेशन किसी दस्तावेज़ को किसमें विभाजित करता है?",
 "సెంటెన్స్ టోకనైజేషన్ డాక్యుమెంట్‌ను దేనిగా విభజిస్తుంది?",
 ["Sentences", "Characters only", "Images", "Numbers only"],
 ["वाक्यों में", "केवल अक्षरों में", "चित्रों में", "केवल संख्याओं में"],
 ["వాక్యాలుగా", "అక్షరాలుగా మాత్రమే", "చిత్రాలుగా", "సంఖ్యలుగా మాత్రమే"],
 "A"),

(27, "What is stopword removal?",
 "स्टॉपवर्ड रिमूवल क्या है?",
 "స్టాప్‌వర్డ్ రిమూవల్ అంటే ఏమిటి?",
 ["Removing common words that may add little information", "Removing every noun", "Removing every number", "Removing all sentences"],
 ["ऐसे सामान्य शब्दों को हटाना जो कम जानकारी देते हैं", "हर संज्ञा को हटाना", "हर संख्या को हटाना", "सभी वाक्यों को हटाना"],
 ["తక్కువ సమాచారాన్ని ఇచ్చే సాధారణ పదాలను తొలగించడం", "ప్రతి నామవాచకాన్ని తొలగించడం", "ప్రతి సంఖ్యను తొలగించడం", "అన్ని వాక్యాలను తొలగించడం"],
 "A"),

(27, "Which process converts words to their root-like form?",
 "कौन सी प्रक्रिया शब्दों को उनके मूल जैसे रूप में बदलती है?",
 "పదాలను వాటి మూల రూపానికి దగ్గరగా మార్చే ప్రక్రియ ఏది?",
 ["Stemming", "Parsing images", "Rendering", "Encryption"],
 ["स्टेमिंग", "चित्र पार्सिंग", "रेंडरिंग", "एन्क्रिप्शन"],
 ["స్టెమింగ్", "చిత్రాలను పార్సింగ్ చేయడం", "రెండరింగ్", "ఎన్‌క్రిప్షన్"],
 "A"),

(27, "Which process usually uses vocabulary and morphology to find a valid base form?",
 "कौन सी प्रक्रिया आमतौर पर शब्दावली और मॉर्फोलॉजी का उपयोग करके सही मूल रूप खोजती है?",
 "పదకోశం మరియు మోర్ఫాలజీని ఉపయోగించి సరైన మూల రూపాన్ని కనుగొనే ప్రక్రియ ఏది?",
 ["Lemmatization", "Token deletion", "Image filtering", "Audio compression"],
 ["लेमेटाइजेशन", "टोकन हटाना", "चित्र फ़िल्टरिंग", "ऑडियो संपीड़न"],
 ["లెమటైజేషన్", "టోకెన్ తొలగింపు", "ఇమేజ్ ఫిల్టరింగ్", "ఆడియో కంప్రెషన్"],
 "A"),

# ================= LEVEL 3 — POS AND FEATURES =================

(28, "What does POS tagging identify?",
 "POS टैगिंग क्या पहचानता है?",
 "POS ట్యాగింగ్ ఏమి గుర్తిస్తుంది?",
 ["The grammatical category of a word", "The color of an image", "The size of a file", "The internet speed"],
 ["शब्द की व्याकरणिक श्रेणी", "चित्र का रंग", "फ़ाइल का आकार", "इंटरनेट की गति"],
 ["పదం యొక్క వ్యాకరణ వర్గం", "చిత్రం యొక్క రంగు", "ఫైల్ పరిమాణం", "ఇంటర్నెట్ వేగం"],
 "A"),

(28, "In POS tagging, what does NN usually represent?",
 "POS टैगिंग में NN आमतौर पर क्या दर्शाता है?",
 "POS ట్యాగింగ్‌లో NN సాధారణంగా దేనిని సూచిస్తుంది?",
 ["Noun", "Verb", "Adjective", "Preposition"],
 ["संज्ञा", "क्रिया", "विशेषण", "पूर्वसर्ग"],
 ["నామవాచకం", "క్రియ", "విశేషణం", "పూర్వసర్గం"],
 "A"),

(28, "In POS tagging, what does VB usually represent?",
 "POS टैगिंग में VB आमतौर पर क्या दर्शाता है?",
 "POS ట్యాగింగ్‌లో VB సాధారణంగా దేనిని సూచిస్తుంది?",
 ["Verb", "Noun", "Determiner", "Adverb"],
 ["क्रिया", "संज्ञा", "निर्धारक", "क्रियाविशेषण"],
 ["క్రియ", "నామవాచకం", "డిటర్మినర్", "క్రియావిశేషణం"],
 "A"),

(28, "What is a corpus in NLP?",
 "एनएलपी में कॉर्पस क्या है?",
 "NLPలో కార్పస్ అంటే ఏమిటి?",
 ["A collection of texts or language data", "A computer processor", "A graphics card", "A database of images only"],
 ["टेक्स्ट या भाषा डेटा का संग्रह", "कंप्यूटर प्रोसेसर", "ग्राफिक्स कार्ड", "केवल चित्रों का डेटाबेस"],
 ["టెక్స్ట్ లేదా భాషా డేటా యొక్క సేకరణ", "కంప్యూటర్ ప్రాసెసర్", "గ్రాఫిక్స్ కార్డ్", "చిత్రాల డేటాబేస్ మాత్రమే"],
 "A"),

(28, "Which library is commonly used for basic NLP tasks in Python?",
 "पाइथन में बुनियादी एनएलपी कार्यों के लिए कौन सी लाइब्रेरी आमतौर पर उपयोग होती है?",
 "పైథాన్‌లో ప్రాథమిక NLP పనులకు సాధారణంగా ఏ లైబ్రరీని ఉపయోగిస్తారు?",
 ["NLTK", "NumPy only", "Matplotlib only", "Tkinter only"],
 ["NLTK", "केवल NumPy", "केवल Matplotlib", "केवल Tkinter"],
 ["NLTK", "NumPy మాత్రమే", "Matplotlib మాత్రమే", "Tkinter మాత్రమే"],
 "A"),

# ================= LEVEL 4 — N-GRAMS AND TF-IDF =================

(29, "What is a bigram in NLP?",
 "एनएलपी में बिग्राम क्या है?",
 "NLPలో బిగ్రామ్ అంటే ఏమిటి?",
 ["A sequence of two consecutive words", "A single character", "A sequence of four words", "A paragraph"],
 ["दो लगातार शब्दों का क्रम", "एक अक्षर", "चार शब्दों का क्रम", "एक पैराग्राफ"],
 ["వరుసగా వచ్చే రెండు పదాల క్రమం", "ఒక అక్షరం", "నాలుగు పదాల క్రమం", "ఒక పేరాగ్రాఫ్"],
 "A"),

(29, "What is a trigram?",
 "ट्रिग्राम क्या है?",
 "ట్రిగ్రామ్ అంటే ఏమిటి?",
 ["A sequence of three consecutive words", "A single word", "Two paragraphs", "An image feature"],
 ["तीन लगातार शब्दों का क्रम", "एक शब्द", "दो पैराग्राफ", "एक चित्र विशेषता"],
 ["వరుసగా వచ్చే మూడు పదాల క్రమం", "ఒక పదం", "రెండు పేరాగ్రాఫ్‌లు", "ఒక ఇమేజ్ ఫీచర్"],
 "A"),

(29, "What does TF-IDF help measure?",
 "TF-IDF क्या मापने में मदद करता है?",
 "TF-IDF దేనిని కొలవడంలో సహాయపడుతుంది?",
 ["The importance of a word in a document relative to a collection", "Image brightness", "Audio volume", "CPU temperature"],
 ["किसी संग्रह की तुलना में दस्तावेज़ में शब्द का महत्व", "चित्र की चमक", "ऑडियो की आवाज़", "CPU तापमान"],
 ["పత్రాల సమూహంతో పోల్చినప్పుడు డాక్యుమెంట్‌లో పదం యొక్క ప్రాముఖ్యత", "చిత్రం ప్రకాశం", "ఆడియో వాల్యూమ్", "CPU ఉష్ణోగ్రత"],
 "A"),

(29, "What does TF measure in TF-IDF?",
 "TF-IDF में TF क्या मापता है?",
 "TF-IDFలో TF దేనిని కొలుస్తుంది?",
 ["How often a term appears in a document", "How many images exist", "The document size in bytes", "The number of computers"],
 ["दस्तावेज़ में किसी शब्द के आने की आवृत्ति", "चित्रों की संख्या", "बाइट्स में दस्तावेज़ का आकार", "कंप्यूटरों की संख्या"],
 ["డాక్యుమెంట్‌లో ఒక పదం ఎన్నిసార్లు కనిపిస్తుందో", "చిత్రాల సంఖ్య", "బైట్లలో డాక్యుమెంట్ పరిమాణం", "కంప్యూటర్ల సంఖ్య"],
 "A"),

(29, "What is IDF intended to reduce the importance of?",
 "IDF किसकी महत्ता को कम करने के लिए उपयोग किया जाता है?",
 "IDF దేనికి ప్రాముఖ్యతను తగ్గించడానికి ఉపయోగించబడుతుంది?",
 ["Words that occur in many documents", "Rare words only", "All numbers", "All sentences"],
 ["कई दस्तावेज़ों में आने वाले शब्द", "केवल दुर्लभ शब्द", "सभी संख्याएँ", "सभी वाक्य"],
 ["చాలా డాక్యుమెంట్లలో కనిపించే పదాలు", "అరుదైన పదాలు మాత్రమే", "అన్ని సంఖ్యలు", "అన్ని వాక్యాలు"],
 "A"),

# ================= LEVEL 5 — ADVANCED NLP BASICS =================

(30, "What is word embedding?",
 "वर्ड एम्बेडिंग क्या है?",
 "వర్డ్ ఎంబెడ్డింగ్ అంటే ఏమిటి?",
 ["A numerical vector representation of a word", "A video format", "A database table", "A programming language"],
 ["किसी शब्द का संख्यात्मक वेक्टर प्रतिनिधित्व", "एक वीडियो प्रारूप", "एक डेटाबेस तालिका", "एक प्रोग्रामिंग भाषा"],
 ["ఒక పదానికి సంఖ్యాత్మక వెక్టర్ ప్రాతినిధ్యం", "ఒక వీడియో ఫార్మాట్", "ఒక డేటాబేస్ టేబుల్", "ఒక ప్రోగ్రామింగ్ భాష"],
 "A"),

(30, "Which model architecture is designed to process sequences using recurrent connections?",
 "कौन सा मॉडल आर्किटेक्चर recurrent connections का उपयोग करके sequences को संसाधित करता है?",
 "Recurrent connections ఉపయోగించి sequences ను process చేయడానికి రూపొందించబడిన model architecture ఏది?",
 ["RNN", "CNN", "Decision Tree", "K-Means"],
 ["RNN", "CNN", "Decision Tree", "K-Means"],
 ["RNN", "CNN", "Decision Tree", "K-Means"],
 "A"),

(30, "What problem can vanilla RNNs have when learning long sequences?",
 "लंबे sequences सीखते समय vanilla RNN में कौन सी समस्या हो सकती है?",
 "పొడవైన sequences నేర్చుకునేటప్పుడు vanilla RNNలో ఏ సమస్య ఉండవచ్చు?",
 ["Vanishing gradients", "Image resizing", "Disk formatting", "Screen flickering"],
 ["वैनिशिंग ग्रेडिएंट्स", "चित्र का आकार बदलना", "डिस्क फॉर्मेटिंग", "स्क्रीन फ्लिकरिंग"],
 ["వానిషింగ్ గ్రేడియెంట్స్", "ఇమేజ్ రీసైజింగ్", "డిస్క్ ఫార్మాటింగ్", "స్క్రీన్ ఫ్లికరింగ్"],
 "A"),

(30, "Which neural network architecture is commonly used to capture sequence information with gates?",
 "कौन सा न्यूरल नेटवर्क आर्किटेक्चर gates के माध्यम से sequence information को संभालने के लिए उपयोग होता है?",
 "Gates ద్వారా sequence information ను నిర్వహించడానికి సాధారణంగా ఏ neural network architecture ఉపయోగిస్తారు?",
 ["LSTM", "K-Means", "Linear Regression", "Naive Bayes"],
 ["LSTM", "K-Means", "Linear Regression", "Naive Bayes"],
 ["LSTM", "K-Means", "Linear Regression", "Naive Bayes"],
 "A"),

(30, "What is sentiment analysis used for?",
 "Sentiment analysis का उपयोग किस लिए किया जाता है?",
 "Sentiment analysis దేనికి ఉపయోగిస్తారు?",
 ["Determining opinions or emotional polarity in text", "Compressing images", "Increasing CPU speed", "Creating databases"],
 ["टेक्स्ट में राय या भावनात्मक ध्रुवता निर्धारित करना", "चित्रों को संपीड़ित करना", "CPU की गति बढ़ाना", "डेटाबेस बनाना"],
 ["టెక్స్ట్‌లో అభిప్రాయాలు లేదా భావోద్వేగ ధోరణిని గుర్తించడం", "చిత్రాలను కంప్రెస్ చేయడం", "CPU వేగాన్ని పెంచడం", "డేటాబేస్‌లను సృష్టించడం"],
 "A")
]

sql = """
INSERT INTO quizzes
(
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
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 100)
"""

for level_id, q_en, q_hi, q_te, en_opts, hi_opts, te_opts, correct in questions:

    cursor.execute(
        sql,
        (
            level_id,
            q_en,
            q_te,
            q_hi,

            en_opts[0],
            en_opts[1],
            en_opts[2],
            en_opts[3],

            te_opts[0],
            te_opts[1],
            te_opts[2],
            te_opts[3],

            hi_opts[0],
            hi_opts[1],
            hi_opts[2],
            hi_opts[3],

            correct,
            "This answer correctly matches the NLP concept described in the question."
        )
    )

db.commit()

print("NLP quiz questions added successfully!")
print("New questions inserted:", len(questions))

cursor.close()
db.close()