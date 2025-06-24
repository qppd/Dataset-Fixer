import os
import xml.etree.ElementTree as ET
import customtkinter as ctk
from tkinter import filedialog, messagebox

def show_class_removal_dialog(parent, folder_path):
    dialog = ctk.CTkToplevel(parent)
    dialog.title("Delete Class")
    dialog.geometry("500x400")
    dialog.grab_set()
    dialog.attributes("-topmost", True)
    dialog.resizable(False, False)

    ctk.CTkLabel(dialog, text="📑 Upload classes.txt or type classes manually\n(One class per line - must match <name> tag in XML)",
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
        class_names_to_delete = {name.strip() for name in text_area.get("1.0", "end").strip().splitlines() if name.strip()}
        deleted_files_count = 0
        annotation_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".xml")]

        for xml_file in annotation_files:
            xml_path = os.path.join(folder_path, xml_file)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            objects = root.findall("object")
            for obj in objects:
                name = obj.find("name").text.strip()
                if name in class_names_to_delete:
                    root.remove(obj)

            if not root.findall("object"):
                os.remove(xml_path)
                deleted_files_count += 1

                if delete_images:
                    image_base = os.path.splitext(xml_file)[0]
                    for ext in [".jpg", ".jpeg", ".png", ".bmp"]:
                        image_path = os.path.join(folder_path, image_base + ext)
                        if os.path.exists(image_path):
                            os.remove(image_path)
                            break
            else:
                tree.write(xml_path)

        messagebox.showinfo("Done", f"Deleted {deleted_files_count} annotation files.")

    delete_btn = ctk.CTkButton(dialog, text="🗑 Delete Classes + XML Only",
                               command=lambda: delete_labels(delete_images=False))
    delete_btn.pack(pady=(15, 5))

    delete_img_btn = ctk.CTkButton(dialog, text="🗑 Delete Classes + XML + Images",
                                   command=lambda: delete_labels(delete_images=True))
    delete_img_btn.pack(pady=(0, 10))
