import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from model_selector_ui import ModelSelectorApp


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # App Setup
        self.title("Dataset Fixer")
        self.geometry("900x600")

        self.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.setup_ui()

        self._center_window()
    def _center_window(self):
        self.update_idletasks()  # Ensure the window dimensions are calculated

        width = self.winfo_width()
        height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.geometry(f"{width}x{height}+{x}+{y}")

    def setup_ui(self):
        # Load background image
        bg_image = Image.open("assets/main_bg.png").resize((900, 600))
        bg_photo = CTkImage(light_image=bg_image, size=(900, 600))

        # Background frame
        bg_frame = ctk.CTkFrame(self, width=900, height=600, corner_radius=0)
        bg_frame.pack(fill="both", expand=True)

        # Background label
        ctk.CTkLabel(bg_frame, image=bg_photo, text="").place(relx=0.5, rely=0.5, anchor="center")

        # Transparent overlay
        overlay = ctk.CTkFrame(bg_frame, fg_color="transparent", width=900, height=600)
        overlay.place(relx=0.5, rely=0.5, anchor="center")

        # Logo
        logo_image = Image.open("assets/logo.png").resize((200, 200))
        logo_photo = CTkImage(light_image=logo_image, size=(200, 200))
        ctk.CTkLabel(overlay, image=logo_photo, text="", bg_color="transparent").place(relx=0.5, rely=0.2, anchor="center")

        # Title
        ctk.CTkLabel(
            overlay,
            text="Dataset Fixer",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#ffffff",
            bg_color="transparent"
        ).place(relx=0.5, rely=0.42, anchor="center")

        # Subtitle
        ctk.CTkLabel(
            overlay,
            text="Fix mismatched labels, clean data, and prepare CSVs for ML",
            font=ctk.CTkFont(size=16),
            text_color="#dddddd",
            bg_color="transparent"
        ).place(relx=0.5, rely=0.47, anchor="center")

        # Start Button
        ctk.CTkButton(
            overlay,
            text="🚀 Start Preprocessing",
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.start_preprocessing
        ).place(relx=0.5, rely=0.58, anchor="center")

        # Footer
        ctk.CTkLabel(
            overlay,
            text="© 2025 QPPD • Dataset Fixer",
            font=ctk.CTkFont(size=12),
            text_color="#aaaaaa",
            bg_color="transparent"
        ).place(relx=0.5, rely=0.95, anchor="center")

    def start_preprocessing(self):
        self.withdraw()  # Hide the main window
        selector = ModelSelectorApp(parent=self)  # Pass self as parent
        selector.mainloop()
