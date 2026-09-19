import hashlib
import json
from pathlib import Path

# Define the folder path
folder = Path('monitored')
hashes = {}

# Loop through all files in the directory
for file_path in folder.iterdir():
    if file_path.is_file():  # Skip subfolders
        with open(file_path, 'rb') as file:
            content = file.read()
            file_hash = hashlib.sha256(content).hexdigest()
            
        hashes[file_path.name] = file_hash

# Try loading the old hashes
try:
    with open("hashes.json", "r") as json_file:
        old_hashes = json.load(json_file)

except FileNotFoundError:
    old_hashes = {}
    print("No previous hash database found. Creating one...")

# Compare old and new hashes

for filename, new_hash in hashes.items():

    if filename not in old_hashes:
        print(f"[NEW] {filename}")

    elif old_hashes[filename] != new_hash:
        print(f"[MODIFIED] {filename}")

    else:
        print(f"[UNCHANGED] {filename}")

# Check for deleted files

for filename in old_hashes:

    if filename not in hashes:
        print(f"[DELETED] {filename}")

# Save the new hashes

with open("hashes.json", "w") as json_file:
    json.dump(hashes, json_file, indent=4)