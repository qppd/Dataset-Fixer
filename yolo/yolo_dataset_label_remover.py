import os
import customtkinter as ctk
from tkinter import filedialog


def show_class_removal_dialog(parent, folder_path):
    dialog = ctk.CTkToplevel(parent)
    dialog.title("Delete Class")
    dialog.geometry("500x400")
    dialog.grab_set()
    dialog.attributes("-topmost", True)
    dialog.resizable(False, False)

    ctk.CTkLabel(dialog, text="📑 Upload classes.txt or type classes manually\n(One class per line, index = line #)",
                 font=ctk.CTkFont(size=14), justify="center").pack(pady=(10, 5))

    text_area = ctk.CTkTextbox(dialog, height=180)
    text_area.pack(padx=10, pady=10, fill="both", expand=True)

    def load_classes_txt():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                classes = f.read()
                text_area.delete("1.0", "end")
                text_area.insert("1.0", classes)

    upload_btn = ctk.CTkButton(dialog, text="📂 Upload classes.txt", command=load_classes_txt)
    upload_btn.pack(pady=5)

    def delete_labels(delete_images=False):
        lines = text_area.get("1.0", "end").strip().splitlines()
        classes = {str(i): name for i, name in enumerate(lines)}
        label_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
