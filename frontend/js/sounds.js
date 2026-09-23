/* =========================================================
   LEARNQUEST GAME MUSIC + UI SOUND
   ========================================================= */

let audioContext = null;

let musicMasterGain = null;

let musicTimer = null;

let musicPlaying = false;

let melodyIndex = 0;


/* =========================================================
   STORAGE KEYS
   ========================================================= */

const MUSIC_KEY =
    "learnquest_music";

const SOUND_KEY =
    "learnquest_sound";

const MUSIC_TIME_KEY =
    "learnquest_music_time";


/* =========================================================
   CHECK MUSIC
   ========================================================= */

function isMusicEnabled() {

    return (
        localStorage.getItem(
            MUSIC_KEY
        ) !== "off"
    );

}


/* =========================================================
   CHECK SOUND
   ========================================================= */

function isSoundEnabled() {

    return (
        localStorage.getItem(
            SOUND_KEY
        ) !== "off"
    );

}


/* =========================================================
   CREATE AUDIO CONTEXT
   ========================================================= */

function createAudioContext() {

    if (
        audioContext
    ) {

        return true;

    }


    const AudioContextClass =
        window.AudioContext ||
        window.webkitAudioContext;


    if (
        !AudioContextClass
    ) {

        console.log(
            "Web Audio API is not supported."
        );


        return false;

    }


    audioContext =
        new AudioContextClass();


    return true;

}


/* =========================================================
   CREATE GAME MUSIC
   ========================================================= */

function createGameMusic() {

    if (
        !createAudioContext()
    ) {

        return;

    }


    if (
        musicMasterGain
    ) {

        return;

    }


    musicMasterGain =
        audioContext.createGain();


    /*
     * Background music volume.
     */

    musicMasterGain.gain.value =
        0.12;


    musicMasterGain.connect(
        audioContext.destination
    );

}


/* =========================================================
   PLAY MUSIC NOTE
   ========================================================= */

function playGameNote(
    frequency,
    duration = 0.35
) {

    if (
        !audioContext ||
        !musicMasterGain
    ) {

        return;

    }


    const oscillator =
        audioContext.createOscillator();


    const gain =
        audioContext.createGain();


    oscillator.type =
        "triangle";


    oscillator.frequency.value =
        frequency;


    const now =
        audioContext.currentTime;


    gain.gain.setValueAtTime(
        0.0001,
        now
    );


    gain.gain.exponentialRampToValueAtTime(
        0.22,
        now + 0.03
    );


    gain.gain.exponentialRampToValueAtTime(
        0.0001,
        now + duration
    );


    oscillator.connect(
        gain
    );


    gain.connect(
        musicMasterGain
    );


    oscillator.start(
        now
    );


    oscillator.stop(
        now +
        duration +
        0.02
    );

}


/* =========================================================
   GAME MELODY
   ========================================================= */

const gameMelody = [

    261.63,
    329.63,
    392.00,
    523.25,

    392.00,
    329.63,
    293.66,
    349.23,

    440.00,
    523.25,
    659.25,
    523.25,

    392.00,
    329.63,
    261.63,
    329.63

];


/* =========================================================
   START BACKGROUND MUSIC
   ========================================================= */

async function startBackgroundMusic() {

    if (
        !isMusicEnabled()
    ) {

        return;

    }


    try {

        createGameMusic();


        if (
            !audioContext
        ) {

            return;

        }


        if (
            audioContext.state ===
            "suspended"
        ) {

            await audioContext.resume();

        }


        if (
            musicPlaying
        ) {

            return;

        }


        musicPlaying =
            true;


        melodyIndex =
            0;


        playGameNote(
            gameMelody[
                melodyIndex
            ],
            0.55
        );


        melodyIndex =
            (
                melodyIndex +
                1
            ) %
            gameMelody.length;


        musicTimer =
            setInterval(
                function () {

                    if (
                        !isMusicEnabled()
                    ) {

                        return;

                    }


                    playGameNote(
                        gameMelody[
                            melodyIndex
                        ],
                        0.55
                    );


                    melodyIndex =
                        (
                            melodyIndex +
                            1
                        ) %
                        gameMelody.length;

                },
                650
            );


        const musicNote =
            document.getElementById(
                "musicNote"
            );


        if (
            musicNote
        ) {

            musicNote.textContent =
                "🎵 Music ON";

        }

    }

    catch (error) {

        console.error(
            "Music start error:",
            error
        );


        musicPlaying =
            false;

    }

}


/* =========================================================
   STOP BACKGROUND MUSIC
   ========================================================= */

function stopBackgroundMusic() {

    if (
        musicTimer
    ) {

        clearInterval(
            musicTimer
        );


        musicTimer =
            null;

    }


    musicPlaying =
        false;


    if (
        audioContext &&
        audioContext.state ===
            "running"
    ) {

        audioContext.suspend();

    }


    const musicNote =
        document.getElementById(
            "musicNote"
        );


    if (
        musicNote
    ) {

        musicNote.textContent =
            "🔇 Music OFF";

    }

}


/* =========================================================
   CLICK SOUND
   ========================================================= */

function playClickSound() {

    if (
        !isSoundEnabled()
    ) {

        return;

    }


    try {

        if (
            !createAudioContext()
        ) {

            return;

        }


        if (
            audioContext.state ===
            "suspended"
        ) {

            audioContext.resume();

        }


        const oscillator =
            audioContext.createOscillator();


        const gain =
            audioContext.createGain();


        const now =
            audioContext.currentTime;


        oscillator.type =
            "sine";


        /*
         * Small "ting" sound.
         */

        oscillator.frequency.setValueAtTime(
            820,
            now
        );


        oscillator.frequency.exponentialRampToValueAtTime(
            1250,
            now + 0.08
        );


        gain.gain.setValueAtTime(
            0.0001,
            now
        );


        gain.gain.exponentialRampToValueAtTime(
            0.16,
            now + 0.015
        );


        gain.gain.exponentialRampToValueAtTime(
            0.0001,
            now + 0.14
        );


        oscillator.connect(
            gain
        );


        gain.connect(
            audioContext.destination
        );


        oscillator.start(
            now
        );


        oscillator.stop(
            now + 0.15
        );

    }

    catch (error) {

        console.log(
            "Click sound error:",
            error
        );

    }

}


/* =========================================================
   COIN SOUND
   ========================================================= */

function playCoinSound() {

    if (
        !isSoundEnabled()
    ) {

        return;

    }


    try {

        if (
            !createAudioContext()
        ) {

            return;

        }


        if (
            audioContext.state ===
            "suspended"
        ) {

            audioContext.resume();

        }


        const oscillator =
            audioContext.createOscillator();


        const gain =
            audioContext.createGain();


        const now =
            audioContext.currentTime;


        oscillator.type =
            "sine";


        oscillator.frequency.setValueAtTime(
            700,
            now
        );


        oscillator.frequency.exponentialRampToValueAtTime(
            1100,
            now + 0.12
        );


        gain.gain.setValueAtTime(
            0.15,
            now
        );


        gain.gain.exponentialRampToValueAtTime(
            0.001,
            now + 0.18
        );


        oscillator.connect(
            gain
        );


        gain.connect(
            audioContext.destination
        );


        oscillator.start(
            now
        );


        oscillator.stop(
            now + 0.18
        );

    }

    catch (error) {

        console.log(
            "Coin sound error:",
            error
        );

    }

}


/* =========================================================
   BUTTON / CLICK SOUND SETUP
   ========================================================= */

function setupClickSounds() {

    /*
     * Event delegation:
     * one listener handles buttons,
     * links and selectable controls.
     */

    document.addEventListener(
        "click",
        function (event) {

            const target =
                event.target.closest(
                    "button, a, input, select, .clickable, .subject"
                );


            if (
                !target
            ) {

                return;

            }


            /*
             * Do not play another click sound
             * when disabled.
             */

            if (
                target.disabled
            ) {

                return;

            }


            /*
             * Settings switches can also
             * make a small sound.
             */

            playClickSound();


            /*
             * Start music after first
             * user interaction when enabled.
             */

            if (
                isMusicEnabled()
            ) {

                startBackgroundMusic();

            }

        }
    );

}


/* =========================================================
   SETTINGS
   ========================================================= */

function setupSettings() {

    const musicToggle =
        document.getElementById(
            "musicToggle"
        );


    const soundToggle =
        document.getElementById(
            "soundToggle"
        );


    /*
     * Settings may not exist on
     * every LearnQuest page.
     */

    if (
        !musicToggle ||
        !soundToggle
    ) {

        console.log(
            "Settings controls not found."
        );


        setupClickSounds();


        /*
         * Try music immediately.
         * Browser may block autoplay.
         */

        startBackgroundMusic();


        return;

    }


    /* =====================================================
       INITIAL SWITCH STATES
       ===================================================== */

    musicToggle.checked =
        isMusicEnabled();


    soundToggle.checked =
        isSoundEnabled();


    /* =====================================================
       MUSIC SWITCH
       ===================================================== */

    musicToggle.addEventListener(
        "change",
        async function () {

            /*
             * Stop click sound duplication
             * for this switch.
             */

            if (
                this.checked
            ) {

                localStorage.setItem(
                    MUSIC_KEY,
                    "on"
                );


                await startBackgroundMusic();

            }

            else {

                localStorage.setItem(
                    MUSIC_KEY,
                    "off"
                );


                stopBackgroundMusic();

            }

        }
    );


    /* =====================================================
       SOUND SWITCH
       ===================================================== */

    soundToggle.addEventListener(
        "change",
        function () {

            localStorage.setItem(
                SOUND_KEY,
                this.checked
                    ? "on"
                    : "off"
            );

        }
    );


    /*
     * First user click starts music
     * because most browsers block
     * automatic audio playback.
     */

    document.addEventListener(
        "click",
        async function startMusicAfterFirstClick() {

            if (
                isMusicEnabled()
            ) {

                await startBackgroundMusic();

            }

        },
        {
            once:
                true
        }
    );


    /*
     * Also attempt immediately.
     */

    startBackgroundMusic();


    /*
     * Setup all click sounds.
     */

    setupClickSounds();

}


/* =========================================================
   MUSIC TIME
   ========================================================= */

function saveMusicTime() {

    localStorage.setItem(
        MUSIC_TIME_KEY,
        String(
            Date.now()
        )
    );

}


/* =========================================================
   COIN VISUAL EFFECT
   ========================================================= */

function showCoinEffect() {

    const coin =
        document.createElement(
            "div"
        );


    coin.className =
        "coin-pop";


    coin.textContent =
        "🪙";


    coin.style.position =
        "fixed";


    coin.style.left =
        "50%";


    coin.style.top =
        "45%";


    coin.style.zIndex =
        "99999";


    coin.style.fontSize =
        "32px";


    coin.style.pointerEvents =
        "none";


    coin.style.transform =
        "translate(-50%, -50%)";


    coin.style.transition =
        "all 0.7s ease";


    document.body.appendChild(
        coin
    );


    requestAnimationFrame(
        function () {

            coin.style.transform =
                "translate(-50%, -90px) scale(1.4)";

            coin.style.opacity =
                "0";

        }
    );


    setTimeout(
        function () {

            coin.remove();

        },
        700
    );

}


/* =========================================================
   LEVEL WON EFFECT
   ========================================================= */

function levelWonEffect() {

    if (
        navigator.vibrate
    ) {

        navigator.vibrate(
            [
                120,
                80,
                120,
                80,
                220
            ]
        );

    }


    playCoinSound();

    showCoinEffect();

}


/* =========================================================
   AUTO START
   ========================================================= */

function initializeLearnQuestAudio() {

    try {

        setupSettings();

    }

    catch (error) {

        console.error(
            "Audio initialization error:",
            error
        );

    }

}


/* =========================================================
   GLOBAL FUNCTIONS
   ========================================================= */

window.startBackgroundMusic =
    startBackgroundMusic;

window.stopBackgroundMusic =
    stopBackgroundMusic;

window.playClickSound =
    playClickSound;

window.playCoinSound =
    playCoinSound;

window.showCoinEffect =
    showCoinEffect;

window.levelWonEffect =
    levelWonEffect;

window.saveMusicTime =
    saveMusicTime;

window.setupSettings =
    setupSettings;


/* =========================================================
   INITIALIZE
   ========================================================= */

initializeLearnQuestAudio();