import hashlib
import json
from pathlib import Path

# Folder to monitor
folder = Path("monitored")

# JSON database
HASH_DATABASE = "hashes.json"

# Store hashes from the current scan
current_hashes = {}


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


# -----------------------------
# Scan all files
# -----------------------------

for file_path in folder.rglob("*"):

    if file_path.is_file():

        if file_path.name == HASH_DATABASE:
            continue

        current_hashes[str(file_path)] = calculate_hash(file_path)


# -----------------------------
# Load previous hashes
# -----------------------------

try:

    with open(HASH_DATABASE, "r") as json_file:
        old_hashes = json.load(json_file)

except FileNotFoundError:

    old_hashes = {}

    print("No previous database found. A new one will be created.\n")


# -----------------------------
# Lists for results
# -----------------------------

modified = []
new = []
deleted = []
unchanged = []


# -----------------------------
# Compare hashes
# -----------------------------

for filename, new_hash in current_hashes.items():

    if filename not in old_hashes:

        new.append(filename)

    elif old_hashes[filename] != new_hash:

        modified.append({
            "file": filename,
            "old_hash": old_hashes[filename],
            "new_hash": new_hash
        })

    else:

        unchanged.append(filename)


# -----------------------------
# Detect deleted files
# -----------------------------

for filename in old_hashes:

    if filename not in current_hashes:

        deleted.append(filename)


# -----------------------------
# Print Report
# -----------------------------

print("=" * 50)
print("        FILE INTEGRITY REPORT")
print("=" * 50)

print()

print(f"Modified Files ({len(modified)})")

if modified:

    for file in modified:

        print("-" * 50)
        print(f"File     : {file['file']}")
        print(f"Old Hash : {file['old_hash']}")
        print(f"New Hash : {file['new_hash']}")

else:

    print("None")

print()

print(f"New Files ({len(new)})")

if new:

    for file in new:
        print(" •", file)

else:

    print("None")

print()

print(f"Deleted Files ({len(deleted)})")

if deleted:

    for file in deleted:
        print(" •", file)

else:

    print("None")

print()

print(f"Unchanged Files ({len(unchanged)})")

if unchanged:

    for file in unchanged:
        print(" •", file)

else:

    print("None")

print()

print("=" * 50)
print(f"Total Files Scanned : {len(current_hashes)}")
print("=" * 50)


# -----------------------------
# Update baseline
# -----------------------------

choice = input("\nUpdate baseline? (y/n): ").lower()

if choice == "y":

    with open(HASH_DATABASE, "w") as json_file:

        json.dump(current_hashes, json_file, indent=4)

    print("\nBaseline updated successfully.")

else:

    print("\nBaseline was not updated.")