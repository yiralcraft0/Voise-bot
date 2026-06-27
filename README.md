# 🎙️ Python Voice Assistant

## **Author:** Priyanshu ([YiralcrafT](https://github.com/yiralcraft0))

## About🚩
A simple **Python Voice Assistant** that listens to your voice commands and performs different desktop automation tasks such as opening websites, searching on the web, controlling YouTube, scrolling pages, and even launching a hand gesture control system.

This project was built to improve my understanding of **Speech Recognition**, **Desktop Automation**, and **Python Automation Libraries**.

---

## ✨ Features

* 🎤 Voice command recognition
* 🌐 Open websites or applications using voice
* 🔍 Search anything on the web
* 📺 Search videos directly on YouTube
* 📜 Scroll pages using voice commands
* ✋ Launch hand gesture control
* ⚡ Fast and lightweight

---

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* PyAudio
* PyAutoGUI
* Pyperclip
* Webbrowser Module

---

## 📦 Required Libraries

Install the required packages before running the project.

```bash
pip install SpeechRecognition
pip install PyAudio
pip install pyautogui
pip install pyperclip
```

Or install everything at once:

```bash
pip install SpeechRecognition PyAudio pyautogui pyperclip
```

---

## 📁 Project Structure

```
Voice-Assistant/
│
├── Voice-bot(YT-Control).py               # Main voice assistant
├── Open_App.py                            # Dictionary of websites/apps
├── hand_control.py                        # Hand gesture control module
├── README.md
└── requirements.txt                       # (Optional)(Will add soon...)
```

---

## 🎯 Supported Commands

### Open Applications / Websites

```
Python open youtube
Python open github
Python open google
```

*(Applications and websites depend on the entries inside `Open_App.py`.)*

---

### Search on Browser

```
Python search
```

The assistant will ask what you want to search and automatically type it into the browser.

---

### Search on YouTube

```
Python youtube search
```

It will activate the YouTube search bar, listen to your query, and search automatically.

---

### Scroll

```
Python scroll up
Python scroll down
```

---

### Hand Control

```
Python hand control
```

Launches the hand gesture control module.

---

### Exit Program

```
exit
```

Stops the assistant.

---

## ⚙️ How It Works

1. The assistant continuously listens through your microphone.
2. Speech is converted into text using Google's Speech Recognition API.
3. The spoken command is analyzed.
4. The corresponding automation task is executed.

---

## 🚀 Running the Project

Clone the repository:

```bash
git clone https://github.com/yiralcraft0/Voice-bot.git
```

Move into the project directory:

```bash
cd Voice-bot
```

Run the program:

```bash
python Voice-bot(YT-Control).py 
```

---

## 📌 Future Improvements

* 🤖 AI-powered conversations using an LLM
* 🎵 Play music with voice commands
* 📅 Calendar and reminder integration
* 🌤️ Weather updates
* 📰 News headlines
* 💻 Open desktop applications directly
* 🧠 Wake word detection (e.g., "Hey Python")
* 🔊 Text-to-Speech responses
* 🏠 Smart home automation support

---

## 🤝 Contributing

Contributions are welcome!

If you have ideas for improvements or discover any bugs, feel free to fork the repository, create a new branch, and submit a pull request.

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Priyanshu**

Aspiring Software Developer passionate about Python, Android Development, Web Development, Automation, and Problem Solving.

⭐ If you like this project, consider giving it a star on GitHub!
