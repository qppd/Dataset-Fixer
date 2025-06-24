import customtkinter as ctk
from tkinter import filedialog
import threading
from tensor.tensorflow_dataset_filename_checker import check_dataset_filenames
from tensor.tensorflow_dataset_label_remover import show_class_removal_dialog

class TENSORWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("TENSORFLOW Dashboard")
        self.state("zoomed")
        self.parent = parent
        self.selected_path = None
        self.processing = False

        self.bind("<Escape>", lambda event: self.close_window())
        self._setup_ui()

    def _setup_ui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # === Sidebar ===
        sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="ns")
        sidebar.grid_rowconfigure(5, weight=1)

        ctk.CTkLabel(sidebar, text="🧠 TENSORFLOW", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(20, 10))

        self.select_button = ctk.CTkButton(
            sidebar, text="📁 Select Folder", command=self.upload_dataset
        )
        self.select_button.pack(pady=10, fill="x", padx=10)

        ctk.CTkButton(
            sidebar, text="🔙 Back", command=self.close_window
        ).pack(pady=10, fill="x", padx=10, side="bottom")

        # === Main content area ===
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        # Right panel container (will hold different views)
        self.right_container = ctk.CTkFrame(self.content)
        self.right_container.grid(row=0, column=0, sticky="nsew")

        self._show_main_menu()

    def _clear_right_container(self):
        for widget in self.right_container.winfo_children():
            widget.destroy()

    def _show_main_menu(self):
        self._clear_right_container()

        self.right_container.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.right_container.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(self.right_container, text="🔧 Dataset Tools", font=ctk.CTkFont(size=26, weight="bold"))
        title.grid(row=0, column=0, pady=(30, 10), sticky="n")

        check_btn = ctk.CTkButton(
            self.right_container,
            text="🔍 Check Filenames",
            font=ctk.CTkFont(size=20),
            height=60,
            width=250,
            command=self._show_filename_checker_ui,
            state="normal" if self.selected_path else "disabled"
        )
        check_btn.grid(row=1, column=0, pady=20, padx=20, sticky="n")

        delete_btn = ctk.CTkButton(
            self.right_container,
            text="🗑️ Delete Class",
            font=ctk.CTkFont(size=20),
            height=60,
            width=250,
            command=self._open_delete_class_dialog,
            state="normal" if self.selected_path else "disabled"
        )
        delete_btn.grid(row=2, column=0, pady=10, padx=20, sticky="n")

    def _show_filename_checker_ui(self):
        self._clear_right_container()

        ctk.CTkLabel(self.right_container, text="🔍 Checking Filenames", font=ctk.CTkFont(size=20)).pack(pady=(10, 5))

        self.progress_bar = ctk.CTkProgressBar(self.right_container, width=400)
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)

        self.scan_label = ctk.CTkLabel(self.right_container, text="Waiting to start...", font=ctk.CTkFont(size=14))
        self.scan_label.pack(pady=(5, 10))

        self.result_label = ctk.CTkLabel(self.right_container, text="", font=ctk.CTkFont(size=14), justify="left")
        self.result_label.pack(pady=(10, 10))

        self.run_button = ctk.CTkButton(self.right_container, text="▶️ Run Check", command=self.check_filenames)
        self.run_button.pack(pady=(5, 10))

        back_button = ctk.CTkButton(self.right_container, text="🔙 Back", command=self._show_main_menu)
        back_button.pack()

    def upload_dataset(self):
        folder_path = filedialog.askdirectory(title="Select TENSORFLOW Dataset Folder")
        if folder_path:
            self.selected_path = folder_path
            self.select_button.configure(state="disabled")
            self._show_main_menu()  # Refresh with enabled buttons

    def check_filenames(self):
        if not self.selected_path:
            return

        # Hide the run button while scanning
        if hasattr(self, "run_button"):
            self.run_button.pack_forget()

        def run_check():
            result = check_dataset_filenames(self.selected_path, update_callback=self.update_scan_progress)
            matched, total, percentage, mismatched = result

            self.scan_label.configure(text="✅ Done scanning.")
            self.result_label.configure(
                text=(
                    f"✅ Filename check complete!\n\n"
                    f"Total images: {total}\n"
                    f"Matching labels: {matched}\n"
                    f"Missing labels: {len(mismatched)}\n"
                    f"✅ Match: {percentage:.2f}%"
                )
            )

            # Show the run button again
            self.run_button.pack(pady=(5, 10))

        threading.Thread(target=run_check, daemon=True).start()

    def update_scan_progress(self, scanned, total):
        self.scan_label.configure(text=f"Scanned {scanned}/{total} files...")
        self.progress_bar.set(scanned / total)

    def _open_delete_class_dialog(self):
        if self.selected_path:
            show_class_removal_dialog(self, self.selected_path)

    def close_window(self):
        if self.processing:
            return
        self.destroy()
        self.parent.deiconify()
