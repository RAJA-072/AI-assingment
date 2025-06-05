import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import speech_recognition as sr
import datetime
import threading
import time
import pyaudio

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Function to speak and update chat
def speak_and_display(text):
    append_to_chat("Assistant: " + text, 'assistant')
    engine.say(text)
    engine.runAndWait()

# Function to process voice commands
def handle_command(command):
    command = command.lower()
    append_to_chat("You: " + command, 'user')

    if "hello" in command:
        speak_and_display("Hello! I'm your voice assistant. How can I help you?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak_and_display("The current time is " + now)
    elif "your name" in command:
        speak_and_display("I'm Rajeswari's intelligent voice assistant.")
    elif "assignment" in command:
        speak_and_display("Assignment II is due on May 14, 2025.")
    elif "course" in command:
        speak_and_display("You're enrolled in the Artificial Intelligence course.")
    elif "exam" in command:
        speak_and_display("The next internal exam is on May 14, 2025.")
    elif "developer" in command:
        speak_and_display("I was developed by Raja Rajeswari, student of the IT department.")
    elif "motivational" in command:
        speak_and_display("Keep pushing forward! Great things take time.")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak_and_display("Today's date is " + today)
    else:
        speak_and_display("I'm not sure how to respond to that.")

# Append messages to chat with different colors
def append_to_chat(text, tag):
    chat_history.config(state='normal')
    chat_history.insert(tk.END, text + "\n", tag)
    chat_history.config(state='disabled')
    chat_history.yview(tk.END)

# Continuous listening loop in thread
def continuous_listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
    while listening:
        try:
            with mic as source:
                append_to_chat("🎧 Listening...", 'status')
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio)
                handle_command(command)
        except sr.UnknownValueError:
            append_to_chat("Assistant: Sorry, I didn't catch that.", 'assistant')
        except sr.WaitTimeoutError:
            append_to_chat("Assistant: Listening timed out.", 'assistant')
        except Exception:
            append_to_chat("Assistant: An error occurred while listening.", 'assistant')
        time.sleep(0.5)

# Start listening in background
def start_listening():
    global listening
    listening = True
    listen_btn.config(state="disabled", bg="#bdbdbd")
    threading.Thread(target=continuous_listen, daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("🎤 Voice Assistant - Raja Rajeswari (22IT072)")
root.geometry("700x650")
root.configure(bg="#f3f0ff")

# Header
header = tk.Label(
    root, text="✨ AI Voice Assistant - Raja Rajeswari (22IT072)",
    font=("Segoe UI", 18, "bold"), bg="#7e57c2", fg="white", pady=15
)
header.pack(fill="x")

# Chat history
chat_history = scrolledtext.ScrolledText(
    root, font=("Segoe UI", 13), wrap=tk.WORD, state='disabled',
    bg="#f5f5f5", fg="#212121", bd=3, height=18, relief="groove"
)
chat_history.tag_config('user', foreground='#2e7d32', font=("Segoe UI", 12, "bold"))
chat_history.tag_config('assistant', foreground='#1565c0', font=("Segoe UI", 12))
chat_history.tag_config('status', foreground='gray', font=("Segoe UI", 11, "italic"))
chat_history.pack(padx=20, pady=20, fill="both", expand=True)

# Hover effects
def on_hover(event):
    listen_btn.config(bg="#4527a0", fg="white")

def on_leave(event):
    listen_btn.config(bg="#673ab7")

# Listen button
listen_btn = tk.Button(
    root, text="🎙️ Start Listening", font=("Segoe UI", 14, "bold"),
    bg="#673ab7", fg="white", padx=40, pady=15,
    command=start_listening, relief="flat", bd=0, cursor="hand2"
)
listen_btn.pack(pady=10)
listen_btn.bind("<Enter>", on_hover)
listen_btn.bind("<Leave>", on_leave)

# Footer
footer = tk.Label(
    root, text="Developed by Raja Rajeswari | 22IT072 | May 2025",
    font=("Segoe UI", 10), bg="#f3f0ff", fg="#555"
)
footer.pack(pady=8)

root.mainloop()
