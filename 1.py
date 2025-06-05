import tkinter as tk
from tkinter import ttk
from textblob import TextBlob

# Analyze sentiment function
def analyze_sentiment():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        result_label.config(text="⚠️ Please enter text to analyze.", fg="#c62828")
        return

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    confidence = round(abs(polarity) * 100, 2)

    if polarity > 0:
        result = f"😊 Positive Sentiment\n"
        result_label.config(fg="#2e7d32")
    elif polarity < 0:
        result = f"😞 Negative Sentiment\n"
        result_label.config(fg="#b71c1c")
    else:
        result = f"😐 Neutral Sentiment\n"
        result_label.config(fg="#37474f")

    result_label.config(text=result)

# Main UI
root = tk.Tk()
root.title("🔍 SentimentIQ - Intelligent Systems")
root.geometry("860x600")
root.configure(bg="#e3f2fd")

# Style customization
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton",
                font=("Helvetica Neue", 12, "bold"),
                foreground="white",
                background="#1976d2",
                padding=10)
style.map("TButton", background=[('active', '#0d47a1')])

# Title Header
header = tk.Label(
    root,
    text="💡 SentimentIQ - Smart Emotion Detector",
    font=("Helvetica Neue", 20, "bold"),
    bg="#e3f2fd",
    fg="#0d47a1"
)
header.pack(pady=25)

# Input Frame
input_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="flat", highlightbackground="#90caf9", highlightthickness=2)
input_frame.pack(padx=40, pady=10, fill="both", expand=True)

prompt_label = tk.Label(
    input_frame,
    text="💬 Share your thoughts below:",
    font=("Helvetica Neue", 13, "bold"),
    bg="#ffffff",
    fg="#1565c0"
)
prompt_label.pack(pady=(15, 5))

input_text = tk.Text(
    input_frame,
    height=10,
    font=("Helvetica Neue", 12),
    bg="#fafafa",
    fg="#263238",
    wrap="word",
    relief="flat",
    padx=10,
    pady=10
)
input_text.pack(padx=15, pady=(0, 15), fill="both", expand=True)

# Analyze Button
analyze_btn = ttk.Button(root, text="🔎 Analyze Now", command=analyze_sentiment)
analyze_btn.pack(pady=20)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Helvetica Neue", 15, "bold"),
    bg="#e3f2fd",
    wraplength=600,
    justify="center"
)
result_label.pack(pady=10)

# Footer
footer = tk.Label(
    root,
    text="Made with ❤️ by Raja Rajeswari | 22IT072 | May 2025",
    font=("Helvetica Neue", 10),
    bg="#e3f2fd",
    fg="#546e7a"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
