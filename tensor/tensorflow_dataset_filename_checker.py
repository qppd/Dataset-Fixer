import os

def check_dataset_filenames(folder_path, update_callback=None):
    # Supported image extensions
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp")

    # Collect image and annotation files
    image_files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(image_extensions)
    ]
    annotation_files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(".xml")
    ]

    # Get base names (without extensions)
    image_basenames = {os.path.splitext(f)[0] for f in image_files}
    annotation_basenames = {os.path.splitext(f)[0] for f in annotation_files}

    matched = image_basenames & annotation_basenames
    mismatched = sorted(image_basenames - annotation_basenames)

    total = len(image_basenames)
    scanned = 0

    for name in sorted(image_basenames):
        scanned += 1
        if update_callback:
            update_callback(scanned, total)

    percentage = (len(matched) / total * 100) if total else 0
    return len(matched), total, percentage, mismatched
