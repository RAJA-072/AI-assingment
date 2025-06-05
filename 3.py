import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
from PIL import Image, ImageTk, ImageDraw

# Chatbot logic
pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you in your career today?']),
    (r'how are you?', ['I’m always here to assist you!']),
    (r'how do I choose a career?', ['Discover your strengths, explore fields, and try internships to guide your choice.']),
    (r'how to prepare for an interview?', ['Research the company, practice common questions, and stay confident!']),
    (r'tell me about yourself', ['Structure it as Present-Past-Future. E.g., "I’m a recent graduate with..."']),
    (r'goodbye|exit|quit', ['Wishing you the best in your career journey!']),
    (r'(.*)', ['Could you clarify or ask something more specific?']),
    (r'hello|hi|hey',
     ['Hello! How can I help you with your career today?', 'Hi there! Ready to prep for your dream job?']),
    (r'what\'s your name?', ['I am your Career and Interview Coach Assistant.']),
    (r'how are you?', ['I’m here and ready to help you shine in your career!']),

    (r'how do I choose a career?', [
        'Identify your strengths, interests, and values. Explore roles that align with them and seek mentorship if possible.']),
    (r'how can I grow in my career?',
     ['Focus on continuous learning, build your network, and seek challenging projects.']),
    (r'what are trending skills in 2025?', [
        'Some in-demand skills include data analysis, cloud computing, AI/ML, cybersecurity, and soft skills like communication.']),

    (r'how do I prepare for an interview?',
     ['Research the company, understand the role, and practice common interview questions.']),
    (r'what are your strengths and weaknesses?', [
        'A good strength: "I am a fast learner." A good weakness: "I sometimes overprepare, but I’m working on balancing it."']),
    (r'tell me about yourself', [
        'Structure it as Present → Past → Future. For example: "I’m a recent IT graduate, I interned at XYZ, and I’m excited to grow in software development."']),
    (r'i am nervous before interviews',
     ['It’s normal! Try breathing exercises, rehearse answers, and focus on being yourself.']),
    (r'what are good questions to ask at the end of an interview?',
     ['Ask about the company culture, growth opportunities, or "What does success look like in this role?"']),

    (r'how to write a resume?',
     ['Keep it concise, use bullet points, tailor it to the job, and include results-driven statements.']),
    (r'how to improve communication skills?',
     ['Practice speaking, join a club like Toastmasters, read aloud, and get feedback.']),

    (r'where can I find jobs?',
     ['Try platforms like LinkedIn, Indeed, Naukri, and also attend career fairs and networking events.']),
    (r'how to write a cover letter?', ['Personalize it, explain why you’re a fit, and show enthusiasm for the role.']),

    (r'give me a motivational quote',
     ['"Success is not final, failure is not fatal: it is the courage to continue that counts." - Winston Churchill']),
    (r'i feel like giving up',
     ['Stay strong! Every expert was once a beginner. Keep moving forward – you’ve got this!']),

    (r'can you tell me a joke?', ['Why did the developer go broke? Because he used up all his cache!']),
    (r'goodbye|exit', ['Good luck with your career! Stay confident and keep learning.']),

    (r'(.*)', ['That’s interesting! Can you tell me more or ask a specific career-related question?'])

]
chatbot = Chat(pairs, reflections)

# Create gradient background
def create_gradient(width, height, color1, color2):
    base = Image.new("RGB", (width, height), color1)
    top = Image.new("RGB", (width, height), color2)
    mask = Image.new("L", (width, height))
    mask_data = [int(255 * (y / height)) for y in range(height) for _ in range(width)]
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return ImageTk.PhotoImage(base)

# Initialize UI
root = tk.Tk()
root.title("✨ Career & Interview Coach")
root.geometry("720x850")
root.resizable(False, False)

# Gradient background
bg_img = create_gradient(720, 850, "#ffecd2", "#fcb69f")
bg_label = tk.Label(root, image=bg_img)
bg_label.place(relwidth=1, relheight=1)

# Fonts & Colors
HEADER_FONT = ("Segoe UI", 26, "bold")
TEXT_FONT = ("Segoe UI", 12)
BUTTON_FONT = ("Segoe UI", 12, "bold")
PRIMARY_COLOR = "#ff4b2b"
SECONDARY_COLOR = "#ff416c"

# Static Header
header_label = tk.Label(
    root,
    text="🌟 Career & Interview Coach",
    font=HEADER_FONT,
    fg="white",
    bg=SECONDARY_COLOR,
    pady=20
)
header_label.pack(pady=(20, 10), fill=tk.X)

# Chat Display Area
chat_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.FLAT)
chat_frame.pack(padx=25, pady=10, fill=tk.BOTH, expand=True)

chat_area = scrolledtext.ScrolledText(
    chat_frame, wrap=tk.WORD, font=TEXT_FONT,
    bg="#ffffff", fg="#333333", relief=tk.FLAT, bd=2
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.insert(tk.END, "🤖 Coach: Hello! I'm your Career & Interview Coach. Ask me anything!\n\n")
chat_area.config(state='disabled')

# Input Area
input_frame = tk.Frame(root, bg="#ffffff")
input_frame.pack(padx=25, pady=15, fill=tk.X)

entry = tk.Entry(
    input_frame, font=TEXT_FONT, bg="#f9f9f9", fg="#000",
    relief=tk.FLAT, bd=2
)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=10)

def send_message():
    user_msg = entry.get().strip()
    if user_msg == "":
        return
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"📝 You: {user_msg}\n")
    bot_response = chatbot.respond(user_msg)
    chat_area.insert(tk.END, f"🤖 Coach: {bot_response}\n\n")
    chat_area.config(state='disabled')
    chat_area.yview(tk.END)
    entry.delete(0, tk.END)

send_btn = tk.Button(
    input_frame,
    text="Send",
    font=BUTTON_FONT,
    bg=PRIMARY_COLOR,
    fg="white",
    activebackground=SECONDARY_COLOR,
    relief=tk.FLAT,
    command=send_message,
    padx=20,
    pady=10
)
send_btn.pack(side=tk.RIGHT)

# Footer
footer = tk.Label(
    root,
    text="✨ Empowering Futures | Developed by RAJA RAJESWARI R © 2025",
    font=("Segoe UI", 10),
    bg="#ff416c",
    fg="white",
    pady=10
)
footer.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
