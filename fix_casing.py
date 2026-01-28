import os
import re
import shutil

ROOT_DIR = "/Users/mg/Downloads/Disease-Dataset-db"
DISEASES_DIR = os.path.join(ROOT_DIR, "diseases")

def to_snake_case(name):
    name = re.sub(r'[^a-zA-Z0-9]', '_', name)
    name = re.sub(r'_+', '_', name)
    return name.strip('_').lower()

def fix_casing():
    for domain in os.listdir(DISEASES_DIR):
        domain_path = os.path.join(DISEASES_DIR, domain)
        if not os.path.isdir(domain_path) or domain.startswith('.'):
            continue
            
        print(f"Checking domain: {domain}")
        for class_name in os.listdir(domain_path):
            class_path = os.path.join(domain_path, class_name)
            if not os.path.isdir(class_path) or class_name.startswith('.'):
                continue
            
            desired_name = to_snake_case(class_name)
            
            if class_name != desired_name:
                desired_path = os.path.join(domain_path, desired_name)
                
                # Check if they reference the same inode/file (case insensitive match)
                # On mac, exists(desired) is true if actual is class_name.
                # But if we rename, we need to be careful.
                
                print(f"Renaming {class_name} -> {desired_name}")
                
                temp_path = os.path.join(domain_path, f"{class_name}_tmp_rename")
                try:
                    os.rename(class_path, temp_path)
                    os.rename(temp_path, desired_path)
                    print(f"  Success: {desired_name}")
                except Exception as e:
                    print(f"  Failed to rename {class_name}: {e}")

if __name__ == "__main__":
    fix_casing()
