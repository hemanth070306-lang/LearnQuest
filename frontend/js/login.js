const API_BASE = "https://learnquest-h5hb.onrender.com";
/* =========================================================
   CLICK SOUND
   ========================================================= */

let clickAudioContext = null;


function playClickSound() {

    try {

        if (
            !clickAudioContext
        ) {

            const AudioContext =
                window.AudioContext ||
                window.webkitAudioContext;


            if (!AudioContext) {

                return;

            }


            clickAudioContext =
                new AudioContext();

        }


        if (
            clickAudioContext.state ===
            "suspended"
        ) {

            clickAudioContext.resume();

        }


        const now =
            clickAudioContext.currentTime;


        const masterGain =
            clickAudioContext.createGain();


        masterGain.gain.setValueAtTime(
            0.0001,
            now
        );


        masterGain.gain.exponentialRampToValueAtTime(
            0.12,
            now + 0.01
        );


        masterGain.gain.exponentialRampToValueAtTime(
            0.0001,
            now + 0.18
        );


        masterGain.connect(
            clickAudioContext.destination
        );


        const firstTone =
            clickAudioContext.createOscillator();


        firstTone.type =
            "sine";


        firstTone.frequency.setValueAtTime(
            850,
            now
        );


        firstTone.connect(
            masterGain
        );


        firstTone.start(
            now
        );


        firstTone.stop(
            now + 0.08
        );


        const secondTone =
            clickAudioContext.createOscillator();


        secondTone.type =
            "sine";


        secondTone.frequency.setValueAtTime(
            1250,
            now + 0.07
        );


        secondTone.connect(
            masterGain
        );


        secondTone.start(
            now + 0.07
        );


        secondTone.stop(
            now + 0.18
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
   EVERY CLICK = TING TONG
   ========================================================= */

document.addEventListener(
    "click",
    function () {

        playClickSound();

    },
    true
);


/* =========================================================
   LOGIN
   ========================================================= */

document
    .getElementById(
        "loginForm"
    )
    .addEventListener(
        "submit",
        async function (
            event
        ) {

            event.preventDefault();


            const email =
                document
                    .getElementById(
                        "email"
                    )
                    .value
                    .trim();


            const password =
                document
                    .getElementById(
                        "password"
                    )
                    .value;


            const message =
                document
                    .getElementById(
                        "message"
                    );


            const loginButton =
                document.querySelector(
                    ".login-btn"
                );


            if (
                !email ||
                !password
            ) {

                message.textContent =
                    "Email and password are required.";

                message.style.color =
                    "#ff6b6b";

                return;

            }


            loginButton.disabled =
                true;


            loginButton.textContent =
                "Checking...";


            message.textContent =
                "";


            try {


                const response =
                    await fetch(
                        API_BASE +
                        "/login",
                        {

                            method:
                                "POST",

                            headers: {

                                "Content-Type":
                                    "application/json"

                            },

                            credentials:
                                "include",

                            body:
                                JSON.stringify({

                                    email:
                                        email,

                                    password:
                                        password

                                })

                        }
                    );


                const data =
                    await response.json();


                if (
                    response.ok
                ) {


                    /* -----------------------------------------
                       STORE USER INFORMATION
                       ----------------------------------------- */

                    if (
                        data.user
                    ) {

                        localStorage.setItem(
                            "user_id",
                            String(
                                data.user.id
                            )
                        );


                        localStorage.setItem(
                            "user_name",
                            data.user.name ||
                            ""
                        );


                        localStorage.setItem(
                            "user_email",
                            data.user.email ||
                            ""
                        );


                        if (
                            data.user.preferred_language
                        ) {

                            localStorage.setItem(
                                "preferred_language",
                                data.user.preferred_language
                            );

                        }

                    }


                    /* -----------------------------------------
                       SUCCESS
                       ----------------------------------------- */

                    message.textContent =
                        "Login successful!";

                    message.style.color =
                        "#58e39d";


                    loginButton.textContent =
                        "Welcome 🚀";


                    /*
                     * Do NOT play automatic voice or
                     * automatic audio here.
                     */


                    setTimeout(
                        function () {

                            window.location.href =
                                "language.html";

                        },
                        500
                    );

                }

                else {


                    message.textContent =
                        data.message ||
                        "Invalid email or password.";

                    message.style.color =
                        "#ff6b6b";


                    loginButton.disabled =
                        false;


                    loginButton.textContent =
                        "Login 🚀";

                }

            }

            catch (error) {

                console.error(
                    "Login error:",
                    error
                );


                message.textContent =
                    "Cannot connect to LearnQuest server.";

                message.style.color =
                    "#ff6b6b";


                loginButton.disabled =
                    false;


                loginButton.textContent =
                    "Login 🚀";

            }

        }
    );
