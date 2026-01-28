import os
import json
from collections import Counter

root_dir = "/Users/mg/Downloads/Disease-Dataset-db/diseases"
keys_stats = Counter()
domains = Counter()

def scan_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".json"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, dict):
                            keys_stats.update(data.keys())
                            if 'domain' in data:
                                domains[data['domain']] += 1
                            else:
                                domains['unknown'] += 1
                except Exception as e:
                    print(f"Error reading {full_path}: {e}")

scan_dir(root_dir)

print("Domains found:", domains)
print("\nKey frequencies:")
for k, v in keys_stats.most_common():
    print(f"{k}: {v}")
