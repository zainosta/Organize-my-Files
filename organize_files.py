#!/usr/bin/env python3
"""
organize_files.py - Sorts files in the current directory into folders by extension.
"""

import os
import shutil

def organize_by_extension():
    current_dir = os.getcwd()
    script_name = os.path.basename(__file__)
    
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        
        # Skip directories
        if os.path.isdir(item_path):
            continue
        
        # Skip the script itself
        if item == script_name:
            continue
        
        # Split filename and extension
        name, ext = os.path.splitext(item)
        if not ext:
            continue  # skip files without extension
        
        folder_name = ext[1:]  # remove the leading dot
        target_folder = os.path.join(current_dir, folder_name)
        os.makedirs(target_folder, exist_ok=True)
        
        # Build destination path
        dest_path = os.path.join(target_folder, item)
        
        # Avoid overwriting: add a suffix if file exists
        counter = 1
        base, ext2 = os.path.splitext(item)
        while os.path.exists(dest_path):
            new_name = f"{base}_{counter}{ext2}"
            dest_path = os.path.join(target_folder, new_name)
            counter += 1
        
        shutil.move(item_path, dest_path)
        print(f"Moved: {item} -> {folder_name}/")

if __name__ == "__main__":
    try:
        organize_by_extension()
        print("✅ All files organized successfully!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
