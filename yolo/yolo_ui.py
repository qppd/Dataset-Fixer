import customtkinter as ctk

class YOLOWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("YOLO Preprocessing")
        self.attributes("-fullscreen", True)
        self.parent = parent

        self.bind("<Escape>", lambda event: self.close_window())
        self._setup_ui()

    def _setup_ui(self):
        ctk.CTkLabel(
            self,
            text="🧠 YOLO Object Detection Preprocessing",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#ffffff"
        ).pack(pady=40)

        ctk.CTkButton(
            self,
            text="📁 Upload YOLO Dataset Folder",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.upload_dataset
        ).pack(pady=20)

        ctk.CTkButton(
            self,
            text="⚙️ Start Preprocessing",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.start_preprocessing
        ).pack(pady=20)

        ctk.CTkButton(
            self,
            text="🔙 Back to Model Selection",
            font=ctk.CTkFont(size=16),
            command=self.close_window
        ).pack(pady=40)

    def upload_dataset(self):
        ctk.CTkMessagebox(title="Upload", message="Dataset upload placeholder", icon="info")

    def start_preprocessing(self):
        ctk.CTkMessagebox(title="Start", message="Starting YOLO preprocessing...", icon="check")

    def close_window(self):
        self.destroy()
        self.parent.deiconify()
