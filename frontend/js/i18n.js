const translations = {

    en: {
        level: "Level",
        beginner: "Beginner",
        explorer: "Explorer",
        challenger: "Challenger",
        problemSolver: "Problem Solver",
        master: "Master",

        topic: "Topic",
        difficulty: "Difficulty",
        xpReward: "XP Reward",
        coins: "Coins",

        learningQuest: "Learning Quest",
        watchVideo: "Watch the learning video and understand the concept.",
        startQuiz: "Start Level Quiz",
        backWorld: "Back to Learning World",

        videoComingSoon:
            "Learning video in your selected language is coming soon!",

        levelComplete: "Level Complete!",
        levelUnlocked: "Level Unlocked!"
    },

    hi: {
        level: "स्तर",
        beginner: "शुरुआती",
        explorer: "अन्वेषक",
        challenger: "चुनौतीकर्ता",
        problemSolver: "समस्या समाधानकर्ता",
        master: "मास्टर",

        topic: "विषय",
        difficulty: "कठिनाई",
        xpReward: "XP पुरस्कार",
        coins: "सिक्के",

        learningQuest: "लर्निंग क्वेस्ट",
        watchVideo:
            "वीडियो देखें और अवधारणा को समझें।",
        startQuiz: "लेवल क्विज शुरू करें",
        backWorld: "लर्निंग वर्ल्ड पर वापस जाएं",

        videoComingSoon:
            "आपकी चुनी हुई भाषा में सीखने का वीडियो जल्द आएगा!",

        levelComplete: "लेवल पूरा हुआ!",
        levelUnlocked: "नया लेवल अनलॉक हुआ!"
    },

    te: {
        level: "స్థాయి",
        beginner: "ప్రారంభికుడు",
        explorer: "అన్వేషకుడు",
        challenger: "ఛాలెంజర్",
        problemSolver: "సమస్య పరిష్కర్త",
        master: "మాస్టర్",

        topic: "అంశం",
        difficulty: "కఠినత",
        xpReward: "XP బహుమతి",
        coins: "నాణేలు",

        learningQuest: "లెర్నింగ్ క్వెస్ట్",
        watchVideo:
            "వీడియోను చూసి కాన్సెప్ట్‌ను అర్థం చేసుకోండి.",
        startQuiz: "లెవల్ క్విజ్ ప్రారంభించండి",
        backWorld: "లెర్నింగ్ వరల్డ్‌కు తిరిగి వెళ్ళండి",

        videoComingSoon:
            "మీరు ఎంచుకున్న భాషలో లెర్నింగ్ వీడియో త్వరలో అందుబాటులో ఉంటుంది!",

        levelComplete: "లెవల్ పూర్తయింది!",
        levelUnlocked: "కొత్త లెవల్ అన్‌లాక్ అయింది!"
    }
};


function getLanguage() {

    return localStorage.getItem("selected_language") || "en";

}


function t(key) {

    const language = getLanguage();

    return translations[language][key]
        || translations.en[key]
        || key;

}