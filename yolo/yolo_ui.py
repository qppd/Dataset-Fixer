# yolo_ui.py

import customtkinter as ctk
from tkinter import filedialog
import threading
from yolo.yolo_dataset_filename_checker import check_dataset_filenames

class YOLOWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("YOLO Dashboard")
        self.state("zoomed")
        self.parent = parent
        self.selected_path = None
        self.processing = False

        self.bind("<Escape>", lambda event: self.close_window())
        self._setup_ui()

    def _setup_ui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar
        sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="ns")
        sidebar.grid_rowconfigure(5, weight=1)

        ctk.CTkLabel(sidebar, text="🧠 YOLO", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(20, 10))

        self.select_button = ctk.CTkButton(
            sidebar, text="📁 Select Folder", command=self.upload_dataset
        )
        self.select_button.pack(pady=10, fill="x", padx=10)

        ctk.CTkButton(
            sidebar, text="🔙 Back", command=self.close_window
        ).pack(pady=10, fill="x", padx=10, side="bottom")

        # Main content
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        self.status_label = ctk.CTkLabel(
            self.content,
            text="Welcome to the YOLO Dashboard.\nUse the buttons on the left to begin.",
            font=ctk.CTkFont(size=20),
            justify="center"
        )
        self.status_label.pack(expand=True)

        self.path_label = ctk.CTkLabel(
            self.content,
            text="", font=ctk.CTkFont(size=14), text_color="#888"
        )
        self.path_label.pack(pady=(10, 20))

        self.check_button = ctk.CTkButton(
            self.content,
            text="🔍 Check Filenames",
            font=ctk.CTkFont(size=16),
            command=self.check_filenames,
            state="disabled"
        )
        self.check_button.pack(pady=10)

        self.progress_bar = ctk.CTkProgressBar(self.content, width=400)
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)

    def upload_dataset(self):
        folder_path = filedialog.askdirectory(title="Select YOLO Dataset Folder")
        if folder_path:
            self.selected_path = folder_path
            self.select_button.configure(state="disabled")
            self.check_button.configure(state="normal")
            self.path_label.configure(text=f"📍 Path: {folder_path}")
            self.status_label.configure(text="✅ Folder selected. Ready to check filenames.")
        else:
            self.status_label.configure(text="⚠️ No folder selected.")

    def check_filenames(self):
        import threading
        import time

        if not self.selected_path:
            ctk.CTkMessagebox(title="Error", message="No dataset folder selected.", icon="cancel")
            return

        # === Create unclosable loading dialog ===
        self.loading_box = ctk.CTkToplevel(self)
        self.loading_box.title("Checking...")
        self.loading_box.geometry("300x150")
        self.loading_box.resizable(False, False)
        self.loading_box.attributes("-toolwindow", True)
        self.loading_box.attributes("-topmost", True)
        self.loading_box.grab_set()
        self.loading_box.protocol("WM_DELETE_WINDOW", lambda: None)

        title_label = ctk.CTkLabel(self.loading_box, text="🔍 Checking filenames...", font=ctk.CTkFont(size=16))
        title_label.pack(pady=(15, 5))

        self.spinner = ctk.CTkProgressBar(self.loading_box, mode="indeterminate")
        self.spinner.pack(pady=5, padx=20)
        self.spinner.start()

        self.scan_label = ctk.CTkLabel(self.loading_box, text="Scanning 0 files...", font=ctk.CTkFont(size=14))
        self.scan_label.pack(pady=(5, 15))

        # === Run check in a background thread ===
        def run_check():
            from yolo.yolo_dataset_filename_checker import check_dataset_filenames

            result = check_dataset_filenames(self.selected_path, update_callback=self.update_scan_progress)

            self.spinner.stop()
            self.loading_box.destroy()

            matched, total, percentage, mismatched = result
            self.status_label.configure(
                text=(
                    f"✅ Filename check complete!\n\n"
                    f"Total images: {total}\n"
                    f"Matching labels: {matched}\n"
                    f"Missing labels: {len(mismatched)}\n"
                    f"✅ Match: {percentage:.2f}%"
                )
            )

        threading.Thread(target=run_check, daemon=True).start()

    def update_scan_progress(self, scanned, total):
        self.scan_label.configure(text=f"Scanned {scanned}/{total} files...")

    def close_window(self):
        if self.processing:
            return  # prevent exit during processing
        self.destroy()
        self.parent.deiconify()
