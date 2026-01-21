# Jarvis – AI Voice Assistant (Python)

Jarvis is a Python-based voice assistant inspired by Tony Stark’s AI assistant from the Marvel Cinematic Universe.  
It listens for a wake word, understands voice commands, performs predefined actions, and uses AI for intelligent conversational responses.

This project was initially inspired by a YouTube tutorial and has been **extended and modified** to:
- Remove unnecessary dependencies
- Integrate OpenAI for AI-powered replies
- Use Google Text-to-Speech for natural voice output
- Improve modularity and clarity

---

## 🚀 Features

- Wake-word activation ("Jarvis")
- Speech-to-text using Google Speech Recognition
- Text-to-speech responses using gTTS
- Open popular websites via voice commands
- Play music using predefined YouTube links
- Fetch and read latest news headlines
- AI-powered conversational fallback using OpenAI

---

## 🛠️ Tech Stack & Libraries

- **Python**
- `speech_recognition`
- `gTTS`
- `pyttsx3` (fallback TTS)
- `webbrowser`
- `requests`
- `openai`
- `uuid`

---

## 📁 Project Structure

```
Jarvis/
│
├── main.py           # Core logic: speech recognition, commands, AI responses
├── musicLibrary.py   # Dictionary mapping song names to YouTube URLs
├── README.md
|-- requirements.txt
```

---

## 🧠 How It Works

1. Jarvis continuously listens for the wake word **"Jarvis"**
2. Once activated, it listens for a user command
3. Based on the command, Jarvis can:
   - Open websites (Google, YouTube, LinkedIn, etc.)
   - Play music from YouTube
   - Read top news headlines
   - Generate AI-based responses using OpenAI
4. All responses are spoken aloud using text-to-speech

---

## ▶️ How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/jarvis.git
cd jarvis
```

### 2️⃣ Install Dependencies
```bash
pip install speechrecognition gtts pyttsx3 requests openai
```

### 3️⃣ Set Environment Variables

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

(Windows users can use `setx OPENAI_API_KEY "your_api_key_here"`)

---

### 4️⃣ Add News API Key

Replace the placeholder in `main.py`:

```python
newsapi = "Your API here"
```

---

### 5️⃣ Run Jarvis
```bash
python main.py
```

Speak **"Jarvis"** to activate the assistant 🎙️

---

## ⚠️ Notes & Limitations

- Requires an active internet connection
- Voice recognition accuracy depends on microphone quality
- Designed primarily for macOS (uses `afplay` for audio playback)
- This project is intended for **learning and experimentation**

---

## 🌱 Future Improvements

- Offline speech recognition
- Cross-platform audio playback
- More system-level commands
- Context-aware conversations
- GUI or web interface

---

## 🙌 Acknowledgements

- Inspired by YouTube tutorials on Python voice assistants
- Concept inspired by **Jarvis (Marvel Cinematic Universe)**

---

## 📄 License

This project is open-source and available for educational purposes.
