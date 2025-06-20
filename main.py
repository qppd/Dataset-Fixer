import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage

# App Config
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Window Setup
app = ctk.CTk()
app.title("Dataset Fixer")
app.geometry("900x600")
app.resizable(False, False)

# --- Load Background ---
bg_image = Image.open("assets/main_bg.png").resize((900, 600))
bg_photo = CTkImage(light_image=bg_image, size=(900, 600))

bg_label = ctk.CTkLabel(master=app, image=bg_photo, text="")
bg_label.place(relx=0.5, rely=0.5, anchor="center")

# --- Load Logo ---
logo_image = Image.open("assets/logo.png").resize((200, 200))
logo_photo = CTkImage(light_image=logo_image, size=(200, 200))

logo_label = ctk.CTkLabel(master=app, image=logo_photo, text="")
logo_label.place(relx=0.5, rely=0.2, anchor="center")

# --- Title ---
title = ctk.CTkLabel(
    app,
    text="Dataset Fixer",
    font=ctk.CTkFont(size=32, weight="bold"),
    text_color="#ffffff"
)
title.place(relx=0.5, rely=0.42, anchor="center")

# --- Subtitle ---
subtitle = ctk.CTkLabel(
    app,
    text="Fix mismatched labels, clean data, and prepare CSVs for ML",
    font=ctk.CTkFont(size=16),
    text_color="#dddddd"
)
subtitle.place(relx=0.5, rely=0.47, anchor="center")

# --- Start Button ---
def start_app():
    print("Start Preprocessing...")

start_button = ctk.CTkButton(
    app,
    text="🚀 Start Preprocessing",
    font=ctk.CTkFont(size=16, weight="bold"),
    command=start_app
)
start_button.place(relx=0.5, rely=0.58, anchor="center")

# --- Footer ---
footer = ctk.CTkLabel(
    app,
    text="© 2025 QPPD • Dataset Fixer",
    font=ctk.CTkFont(size=12),
    text_color="#aaaaaa"
)
footer.place(relx=0.5, rely=0.95, anchor="center")

# Run the app
app.mainloop()
