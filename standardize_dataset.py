import os
import json
import re
import csv
import shutil

ROOT_DIR = "/Users/mg/Downloads/Disease-Dataset-db"
DISEASES_DIR = os.path.join(ROOT_DIR, "diseases")
CSV_PATH = os.path.join(ROOT_DIR, "dataset_index.csv")

def to_snake_case(name):
    name = re.sub(r'[^a-zA-Z0-9]', '_', name)
    name = re.sub(r'_+', '_', name)
    return name.strip('_').lower()

def update_json_content(file_path, domain, class_name, relative_path_to_class):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error decoding JSON: {file_path}")
            return None

    data['domain'] = domain.lower()
    
    # Update ID if needed
    if 'id' not in data or not data['id']:
        safe_class = class_name.upper().replace('_', '')
        data['id'] = f"DISEASE_{domain.upper()}_{safe_class}_001"

    # Fix image_url if present
    if 'image_url' in data:
        # Just ensure it points to the new path structure if possible
        # We might not know the exact filename if it was renamed, 
        # but usually we aren't renaming image files themselves, just folders.
        # But we need to update the path prefix.
        old_url = data['image_url']
        if 'images/' in old_url:
            filename = old_url.split('images/')[-1]
            new_url = f"diseases/{domain}/{class_name}/images/{filename}"
            data['image_url'] = new_url
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    return data

def process_dataset():
    index_rows = []
    
    # Iterate over domains (plant, animal, human)
    for domain in os.listdir(DISEASES_DIR):
        domain_path = os.path.join(DISEASES_DIR, domain)
        if not os.path.isdir(domain_path) or domain.startswith('.'):
            continue

        print(f"Processing domain: {domain}")
        
        # Iterate over disease classes
        for class_name in os.listdir(domain_path):
            class_path = os.path.join(domain_path, class_name)
            if not os.path.isdir(class_path) or class_name.startswith('.'):
                continue
            
            # 1. Rename directory to snake_case
            new_class_name = to_snake_case(class_name)
            new_class_path = os.path.join(domain_path, new_class_name)
            
            if class_path != new_class_path:
                if os.path.exists(new_class_path):
                     print(f"Warning: Target directory {new_class_path} already exists. Merging/Skipping renaming for {class_name}.")
                     # In a real merge scenario we'd move files, but let's assume unique mapping for now or just proceed with new path
                     # strict rename might fail if exists
                else:
                    os.rename(class_path, new_class_path)
                    class_path = new_class_path
            
            # 2. Find and rename metadata JSON
            # We look for a json file that is not in images/ subdirectory
            json_file = None
            files = [f for f in os.listdir(class_path) if f.endswith('.json')]
            
            # Heuristic: largest json or matching name
            # If info.json already exists, use it
            if 'info.json' in files:
                json_file = os.path.join(class_path, 'info.json')
            elif len(files) > 0:
                # Pick the one that looks most like a metadata file (usually same name as folder or similar)
                # We'll just take the first one that seems to be the main descriptor
                target_json = files[0]
                # If multiple, try to find one matching old class name?
                # For now take the first valid one
                old_json_path = os.path.join(class_path, target_json)
                new_json_path = os.path.join(class_path, 'info.json')
                os.rename(old_json_path, new_json_path)
                json_file = new_json_path
            
            metadata = {}
            if json_file:
                metadata = update_json_content(json_file, domain, new_class_name, f"diseases/{domain}/{new_class_name}")

            # 3. Collect images for CSV
            images_dir = os.path.join(class_path, "images")
            if os.path.isdir(images_dir):
                for img_name in os.listdir(images_dir):
                    if img_name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff')):
                        img_rel_path = f"diseases/{domain}/{new_class_name}/images/{img_name}"
                        row = {
                            "image_path": img_rel_path,
                            "label": new_class_name,
                            "domain": domain,
                            "metadata_path": f"diseases/{domain}/{new_class_name}/info.json"
                        }
                        index_rows.append(row)

    # Write CSV
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['image_path', 'label', 'domain', 'metadata_path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(index_rows)
    
    print(f"Processing complete. Index written to {CSV_PATH}")

if __name__ == "__main__":
    process_dataset()
