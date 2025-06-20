import customtkinter as ctk

class ModelSelectorApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Select ML Model Type")
        self.geometry("600x400")
        self.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.selected_model = None
        self._create_widgets()

    def _create_widgets(self):
        # --- Title ---
        ctk.CTkLabel(
            self,
            text="📊 Select Model Type",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#ffffff"
        ).pack(pady=40)

        # --- Dropdown ---
        self.model_types = [
            "YOLO (Object Detection)",
            "TensorFlow (Image Classification)",
            "Random Forest (ML)",
            "Regression (ML)"
        ]

        self.selector = ctk.CTkOptionMenu(
            master=self,
            values=self.model_types,
            width=400,
            font=ctk.CTkFont(size=16),
            dropdown_font=ctk.CTkFont(size=14)
        )
        self.selector.pack(pady=20)

        # --- Confirm Button ---
        ctk.CTkButton(
            master=self,
            text="✔️ Confirm",
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self._on_confirm
        ).pack(pady=30)

        # --- Footer ---
        ctk.CTkLabel(
            master=self,
            text="© 2025 QPPD • Dataset Fixer",
            font=ctk.CTkFont(size=12),
            text_color="#aaaaaa"
        ).pack(side="bottom", pady=10)

    def _on_confirm(self):
        self.selected_model = self.selector.get()
        ctk.CTkMessagebox(
            title="Model Selected",
            message=f"You selected:\n{self.selected_model}",
            icon="check"
        )
        # Future: Call a router, open next step, or write to config
