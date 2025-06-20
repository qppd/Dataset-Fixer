import customtkinter as ctk
from PIL import Image
import os

class ModelSelectorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Select ML Model Type")
        self.geometry("600x500")
        self.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.selected_model = None
        self._create_widgets()

    def _create_widgets(self):
        ctk.CTkLabel(
            self,
            text="📊 Select Model Type",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="#ffffff"
        ).pack(pady=20)

        grid_frame = ctk.CTkFrame(self)
        grid_frame.pack(pady=10)

        asset_path = os.path.join(os.path.dirname(__file__), "assets")
        self.model_data = {
            "YOLO (Object Detection)": os.path.join(asset_path, "yolo_resized.png"),
            "TensorFlow (Image Classification)": os.path.join(asset_path, "tensorflow_resized.png"),
            "Regression (ML)": os.path.join(asset_path, "regression_resized.png"),
            "Random Forest (ML)": os.path.join(asset_path, "random_forest_resized.png")
        }

        row, col = 0, 0
        for label, img_file in self.model_data.items():
            image = ctk.CTkImage(light_image=Image.open(img_file), size=(100, 100))

            btn = ctk.CTkButton(
                master=grid_frame,
                image=image,
                text=label,
                compound="top",
                width=140,
                height=140,
                command=lambda l=label: self._on_model_select(l)
            )
            btn.grid(row=row, column=col, padx=20, pady=20)

            col += 1
            if col > 1:
                col = 0
                row += 1

        ctk.CTkLabel(
            master=self,
            text="© 2025 QPPD • Dataset Fixer",
            font=ctk.CTkFont(size=12),
            text_color="#aaaaaa"
        ).pack(side="bottom", pady=10)

    def _on_model_select(self, label):
        self.selected_model = label
        ctk.CTkMessagebox(
            title="Model Selected",
            message=f"You selected:\n{self.selected_model}",
            icon="check"
        )
