# 🔒 File Integrity Checker

A Python-based File Integrity Checker that monitors files for unauthorized changes using the SHA-256 hashing algorithm.

This project recursively scans a directory, calculates the SHA-256 hash of every file, stores a trusted baseline in a JSON file, and detects new, modified, deleted, or unchanged files during future scans.

---

## Features

- Recursive directory scanning
- SHA-256 hashing for file integrity verification
- Efficient chunk-based file reading
- Baseline creation and management
- Detects:
  - New files
  - Modified files
  - Deleted files
  - Unchanged files
- Displays old and new hashes for modified files
- JSON database for storing hashes
- User confirmation before updating the baseline

---

## Project Structure

```
IntegrityChecker/
│
├── checker.py
├── hashes.json
├── monitored/
│   ├── file1.txt
│   ├── file2.pdf
│   └── images/
│       └── image.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## How It Works

### 1. Create a Baseline

On the first run, the program scans every file inside the monitored folder and creates a SHA-256 hash for each file.

These hashes are stored inside:

```
hashes.json
```

This file becomes the trusted baseline.

---

### 2. Scan Again

During later scans, the program:

- Recalculates the hash of every file
- Loads the previous hashes
- Compares both sets

---

### 3. Detect Changes

The checker reports:

- New files
- Modified files
- Deleted files
- Unchanged files

For modified files, both the previous and current SHA-256 hashes are displayed.

---

## Example Output

```
==================================================
            FILE INTEGRITY REPORT
==================================================

Modified Files (1)

--------------------------------------------------
File     : monitored/notes.txt

Old Hash : 185f8db32271fe25f561a6fc938b2e264306...
New Hash : 6f5902ac237024bdd0c176cb93063dc4...

New Files (1)

• monitored/report.pdf

Deleted Files (1)

• monitored/old_notes.txt

Unchanged Files (5)

• monitored/image.png
• monitored/config.json
• monitored/data.csv

==================================================
Total Files Scanned : 8
==================================================

Update baseline? (y/n):
```

---

## Technologies Used

- Python 3
- pathlib
- hashlib
- json

---

## Concepts Learned

This project demonstrates:

- Python file handling
- Recursive directory traversal
- SHA-256 hashing
- Dictionaries
- Lists
- Functions
- JSON serialization
- Exception handling
- Context managers
- File integrity monitoring concepts

---

## Future Improvements

- Logging to a file
- Ignore file support (.gitignore style)
- Command-line arguments
- File metadata tracking
- Scheduled scans
- Email or desktop notifications
- Multi-threaded hashing for large directories

---

## Disclaimer

This project was built for educational purposes to learn Python and understand the fundamentals of File Integrity Monitoring (FIM).