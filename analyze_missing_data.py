import os
import json

def analyze_missing_data(root_dir):
    stats = {
        "total_files": 0,
        "files_with_missing_data": 0,
        "missing_fields_counts": {},
        "files_list": []
    }
    
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file == "info.json":
                file_path = os.path.join(subdir, file)
                stats["total_files"] += 1
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                    
                    missing_in_file = []
                    
                    # Recursive check function
                    def check_missing(obj, prefix=""):
                        for key, value in obj.items():
                            curr_key = f"{prefix}.{key}" if prefix else key
                            if value == "Unknown" or value == "" or value == [] or value == {}:
                                missing_in_file.append(curr_key)
                            elif isinstance(value, dict):
                                check_missing(value, curr_key)
                            # We don't check inside lists for now unless they are basic types
                    
                    check_missing(data)
                    
                    if missing_in_file:
                        stats["files_with_missing_data"] += 1
                        stats["files_list"].append(file_path)
                        for field in missing_in_file:
                            stats["missing_fields_counts"][field] = stats["missing_fields_counts"].get(field, 0) + 1
                            
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return stats

if __name__ == "__main__":
    root_directory = "/Users/mg/Downloads/Disease-Dataset-db/diseases"
    results = analyze_missing_data(root_directory)
    print(json.dumps(results, indent=2))
    print("\nFiles with missing data:")
    # We need to capture the filenames in the function, so let's modify it slightly or just run a simpler check here if I could, 
    # but refining the function is better.
    # Actually, let's just re-read the function above. I didn't store the filenames in `stats`.
    # I will modify the function to store filenames.
