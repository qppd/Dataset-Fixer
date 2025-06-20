import os
import time

def check_dataset_filenames(folder_path, update_callback=None):
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".jpg")]
    label_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".txt")]

    image_basenames = {os.path.splitext(f)[0] for f in image_files}
    label_basenames = {os.path.splitext(f)[0] for f in label_files}

    matched = image_basenames & label_basenames
    mismatched = image_basenames - label_basenames

    total = len(image_basenames)
    scanned = 0

    for name in sorted(image_basenames):
        #time.sleep(0.2)  # Simulated delay
        scanned += 1
        if update_callback:
            update_callback(scanned, total)

    percentage = (len(matched) / total * 100) if total else 0
    return len(matched), total, percentage, mismatched
