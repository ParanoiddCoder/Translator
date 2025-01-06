import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk

# Initialize translator
translator = Translator()

# Function to perform translation
def translate_text():
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    dest_language_code = language_codes.get(language_choice.get())
    try:
        translation = translator.translate(input_text, dest=dest_language_code)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"Error translating text: {str(e)}")

# Function to clear input and output fields
def clear_text():
    text_input.delete("1.0", tk.END)
    text_output.delete("1.0", tk.END)

# Function to resize background image
def resize_background(event):
    resized_bg = bg_image.resize((event.width, event.height), Image.LANCZOS)
    bg_photo_resized = ImageTk.PhotoImage(resized_bg)
    canvas.itemconfig(bg_label, image=bg_photo_resized)
    canvas.bg_photo_resized = bg_photo_resized  # Prevent image from being garbage collected

# Create the main window
root = tk.Tk()
root.title("Google Translator")
root.geometry("800x600")
# root.state("zoomed")  # Start in full screen mode
root.maxsize(800,600)
#root.iconify()

# Load and set the background image
bg_image = Image.open("background_image.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
bg_label = canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Place widgets directly on the canvas for seamless integration
canvas.create_text(400, 50, text="Translator", font=("TimesNewRoman", 35, "bold"), fill="white")

# Text input box with blended style
text_input = tk.Text(canvas, height=7, width=50, wrap="word", font=("Arial", 12), bg="#ccf8fc", fg="black", bd=0, highlightthickness=1, highlightbackground="#97e1f0")
canvas.create_window(400, 150, window=text_input, anchor="center")
canvas.pack(fill="both",expand=True)

# Language selection dropdown
language_names = [name.title() for name in LANGUAGES.values()]
language_codes = {name.title(): code for code, name in LANGUAGES.items()}
language_choice = ttk.Combobox(canvas, values=language_names, state="readonly", width=47)
language_choice.set("Hindi")
canvas.create_window(400, 250, window=language_choice, anchor="center")

# Buttons for Translate and Clear with adjusted styles
translate_button = ttk.Button(canvas, text="Translate", command=translate_text, style="TButton")
clear_button = ttk.Button(canvas, text="Clear", command=clear_text, style="TButton")
canvas.create_window(350, 300, window=translate_button, anchor="center")
canvas.create_window(450, 300, window=clear_button, anchor="center")

# Output text box with blended style
text_output = tk.Text(canvas, height=7, width=50, wrap="word", font=("Arial", 12), bg="#ccf8fc", fg="black", bd=0, highlightthickness=1, highlightbackground="#CCCCCC")
canvas.create_window(400, 400, window=text_output, anchor="center")

# Style adjustments for better blending
style = ttk.Style()
style.configure("TButton", background="#555555", foreground="black", padding=5, font=("Arial", 10, "bold"))

# Bind resize event to adjust the background image
root.bind("<Configure>", resize_background)

# Run the app
root.mainloop()


