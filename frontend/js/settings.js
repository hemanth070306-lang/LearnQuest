// LearnQuest Settings

const MUSIC_KEY = "learnquest_music";

function isMusicEnabled() {
    return localStorage.getItem(MUSIC_KEY) !== "off";
}

function setMusicEnabled(enabled) {
    localStorage.setItem(
        MUSIC_KEY,
        enabled ? "on" : "off"
    );

    if (enabled) {
        startBackgroundMusic();
    } else {
        stopBackgroundMusic();
    }
}

function startBackgroundMusic() {
    const music = document.getElementById("backgroundMusic");

    if (!music || !isMusicEnabled()) {
        return;
    }

    music.volume = 0.25;

    music.play().catch(() => {
        // Browser may block autoplay until user interacts.
    });
}

function stopBackgroundMusic() {
    const music = document.getElementById("backgroundMusic");

    if (!music) {
        return;
    }

    music.pause();
    music.currentTime = 0;
}

document.addEventListener("DOMContentLoaded", () => {
    const music = document.getElementById("backgroundMusic");

    if (music && isMusicEnabled()) {
        startBackgroundMusic();
    }
});