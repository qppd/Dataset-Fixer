import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Dataset Fixer")
app.geometry("900x600")
app.resizable(False, False)

# --- Background Image ---
bg_image = Image.open("assets/main_bg.png").resize((900, 600))
bg_photo = CTkImage(light_image=bg_image, size=(900, 600))

# --- Background Frame ---
bg_frame = ctk.CTkFrame(master=app, width=900, height=600, corner_radius=0)
bg_frame.pack(fill="both", expand=True)

bg_label = ctk.CTkLabel(master=bg_frame, image=bg_photo, text="")
bg_label.place(relx=0.5, rely=0.5, anchor="center")

# --- Transparent Overlay Frame ---
overlay = ctk.CTkFrame(master=bg_frame, fg_color="transparent", width=900, height=600)
overlay.place(relx=0.5, rely=0.5, anchor="center")

# --- Logo ---
logo_image = Image.open("assets/logo.png").resize((200, 200))
logo_photo = CTkImage(light_image=logo_image, size=(200, 200))

ctk.CTkLabel(master=overlay, image=logo_photo, text="", bg_color="transparent").place(relx=0.5, rely=0.2, anchor="center")

# --- Title and Subtitle ---
ctk.CTkLabel(master=overlay, text="Dataset Fixer", font=ctk.CTkFont(size=32, weight="bold"), text_color="#ffffff", bg_color="transparent").place(relx=0.5, rely=0.42, anchor="center")

ctk.CTkLabel(master=overlay, text="Fix mismatched labels, clean data, and prepare CSVs for ML", font=ctk.CTkFont(size=16), text_color="#dddddd", bg_color="transparent").place(relx=0.5, rely=0.47, anchor="center")

# --- Button ---
def start_app():
    print("Start Preprocessing...")

ctk.CTkButton(master=overlay, text="🚀 Start Preprocessing", font=ctk.CTkFont(size=16, weight="bold"), command=start_app).place(relx=0.5, rely=0.58, anchor="center")

# --- Footer ---
ctk.CTkLabel(master=overlay, text="© 2025 QPPD • Dataset Fixer", font=ctk.CTkFont(size=12), text_color="#aaaaaa", bg_color="transparent").place(relx=0.5, rely=0.95, anchor="center")

app.mainloop()
