"""
Main controller for the Jarvis voice assistant.

This script handles speech recognition, command processing,
AI-based responses, and audio output. Jarvis listens for a
wake word, executes predefined commands, and falls back to
AI-generated replies when needed.
"""

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import os
import uuid


# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# API key for fetching news headlines
newsapi = "Your API here"

# OpenAI client (API key is read from environment variables)
client = OpenAI()


# ---------- SPEECH OUTPUT ----------

def speak_old(text):
    """
    Converts text to speech using pyttsx3.
    Retained as a fallback or alternative speech engine.
    """
    engine.say(text)
    engine.runAndWait()


def speak(text):
    """
    Converts text to speech using Google Text-to-Speech (gTTS).

    Audio is generated dynamically, played, and deleted
    immediately to avoid file clutter.
    """
    filename = f"temp_{uuid.uuid4()}.mp3"
    tts = gTTS(text)
    tts.save(filename)

    os.system(f"afplay {filename}")
    os.remove(filename)


# ---------- AI RESPONSE HANDLING ----------

def aiProcess(command):
    """
    Sends the user's command to the OpenAI API and returns
    a concise AI-generated response in Jarvis-style tone.
    """
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"You are Jarvis, a virtual assistant. Reply briefly.\nUser: {command}"
    )

    return response.output_text


# ---------- COMMAND PROCESSOR ----------

def processCommand(c):
    """
    Parses and executes user voice commands.

    Supports website navigation, music playback,
    news fetching, and AI-based conversational responses.
    """
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play"):
        song = c.split(" ", 1)[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found")

    elif "news" in c:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
        )
        if r.status_code == 200:
            articles = r.json().get("articles", [])
            for article in articles[:5]:
                speak(article["title"])

    else:
        output = aiProcess(c)
        speak(output)


# ---------- MAIN EXECUTION LOOP ----------

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            # Listen briefly for the wake word
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)

            # Activate assistant after detecting wake word
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis active")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            # Prevents the assistant from crashing on recognition errors
            print("Error:", e)