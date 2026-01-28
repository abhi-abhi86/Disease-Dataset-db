import csv
import os
import json

ROOT_DIR = "/Users/mg/Downloads/Disease-Dataset-db"
CSV_PATH = os.path.join(ROOT_DIR, "dataset_index.csv")

def verify():
    if not os.path.exists(CSV_PATH):
        print("CSV index not found!")
        return

    errors = []
    checked_count = 0
    
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            checked_count += 1
            
            # Verify image
            img_full_path = os.path.join(ROOT_DIR, row['image_path'])
            if not os.path.exists(img_full_path):
                errors.append(f"Missing Image: {row['image_path']}")
            
            # Verify metadata
            meta_full_path = os.path.join(ROOT_DIR, row['metadata_path'])
            if not os.path.exists(meta_full_path):
                errors.append(f"Missing Metadata: {row['metadata_path']}")
            else:
                try:
                    with open(meta_full_path, 'r') as jf:
                        json.load(jf)
                except Exception as e:
                    errors.append(f"Invalid JSON {row['metadata_path']}: {e}")

    print(f"Verified {checked_count} entries.")
    
    if errors:
        print(f"Found {len(errors)} errors:")
        for e in errors[:20]:
            print(e)
        if len(errors) > 20:
            print("...")
    else:
        print("All checks passed!")

if __name__ == "__main__":
    verify()
