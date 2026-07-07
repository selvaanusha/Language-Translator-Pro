import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator

# Language Dictionary
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt",
    "Malayalam": "ml",
    "Telugu": "te",
    "Kannada": "kn"
}

# Translate Function
def translate_text():
    text = text_box.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    try:
        source = languages[source_var.get()]
        target = languages[target_var.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, translated)
        result_box.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Clear Function
def clear_text():
    text_box.delete("1.0", tk.END)

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.config(state="disabled")

    count_label.config(text="Characters: 0")


# Swap Languages
def swap_languages():
    source = source_var.get()
    target = target_var.get()

    source_var.set(target)
    target_var.set(source)


# Copy Translation
def copy_text():
    text = result_box.get("1.0", tk.END).strip()

    if text:
        window.clipboard_clear()
        window.clipboard_append(text)
        messagebox.showinfo("Success", "Translation copied successfully!")


# Character Counter
def update_count(event):
    text = text_box.get("1.0", tk.END)
    count_label.config(text=f"Characters: {len(text)-1}")


# ---------------- WINDOW ---------------- #

window = tk.Tk()
window.title("Language Translation Pro")
window.geometry("650x650")
window.resizable(False, False)
window.configure(bg="#E3F2FD")   #

# Heading
heading = tk.Label(
    window,
    text="🌍 Language Translation Pro",
    font=("Arial", 20, "bold"),
    bg="#E3F2FD",
    fg="#0D47A1"
)
heading.pack(pady=15)

# Source Language
tk.Label(
    window,
    text="Source Language",
    font=("Arial", 11)
).pack()

source_var = tk.StringVar()
source_var.set("English")

source_menu = tk.OptionMenu(window, source_var, *languages.keys())
source_menu.pack()

# Target Language
tk.Label(
    window,
    text="Target Language",
    font=("Arial", 11)
).pack(pady=5)

target_var = tk.StringVar()
target_var.set("Tamil")

target_menu = tk.OptionMenu(window, target_var, *languages.keys())
target_menu.pack()

# Input Label
tk.Label(
    window,
    text="Enter Text",
    font=("Arial", 11)
).pack(pady=10)

# Text Box
text_box = tk.Text(
    window,
    height=6,
    width=55,
    font=("Arial", 11)
)
text_box.pack()

text_box.bind("<KeyRelease>", update_count)

# Character Counter
count_label = tk.Label(
    window,
    text="Characters: 0",
    font=("Arial", 10)
)
count_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=15)

translate_btn = tk.Button(
    button_frame,
    text="Translate",
    command=translate_text,
    bg="green",
    fg="white",
    width=12
)
translate_btn.grid(row=0, column=0, padx=5)

swap_btn = tk.Button(
    button_frame,
    text="⇄ Swap",
    command=swap_languages,
    bg="blue",
    fg="white",
    width=12
)
swap_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    bg="red",
    fg="white",
    width=12
)
clear_btn.grid(row=0, column=2, padx=5)

copy_btn = tk.Button(
    button_frame,
    text="Copy",
    command=copy_text,
    bg="purple",
    fg="white",
    width=12
)
copy_btn.grid(row=1, column=1, pady=10)

# Output Label
tk.Label(
    window,
    text="Translated Text",
    font=("Arial", 11)
).pack()

# Output Box
result_box = tk.Text(
    window,
    height=6,
    width=55,
    font=("Arial", 11),
    state="disabled"
)
result_box.pack(pady=10)

window.mainloop()