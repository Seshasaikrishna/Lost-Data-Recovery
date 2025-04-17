# 🔍 Lost Data Recovery using Python

This is a simple Python utility to **recover deleted or lost files** from a backup folder. It's useful for users who maintain local backups and want a quick way to restore accidentally deleted files.

---

## 📁 Project Structure

```
project/
│
├── lost.py           # Main Python script
└── README.md         # Documentation (you are here)
```

---

## ✅ Features

- Recover deleted files from a specified backup folder
- Copies recovered files to a specified destination folder
- Cross-platform support (works best on Windows)
- Simple, readable, and extendable code

---

## 🧑‍💻 Prerequisites

- Python 3.6 or higher installed  
- Backup copies of files available in a known folder  
- Basic understanding of file paths on your system  

---

## 📦 Setup & Installation

1. **Clone or download** this repository.

2. Place your script (`lost.py`) inside the project folder.

3. Make sure the files you want to recover exist in a known backup location.

4. Edit the last line of the script to fit your filename and folder paths:
   ```python
   recover_deleted_file("important_data.txt", r"C:\Users\DELL\Downloads", r"D:\data")
   ```

---

## 🚀 Running the Script

Run the script using Python:

```bash
python lost.py
```

You should see output like:

```bash
✅ Recovered 'important_data.txt' to 'D:\data'
```

If the file doesn't exist in the backup folder, you’ll see:

```bash
❌ Backup for 'important_data.txt' not found in 'C:\Users\DELL\Downloads'.
```

---

## ⚙️ Function Explanation

### `recover_deleted_file(filename, backup_folder, destination_folder)`

- `filename`: Name of the file to recover.
- `backup_folder`: Path to the folder where the backup is stored.
- `destination_folder`: Path to the folder where the file should be restored.

The function checks if the file exists in the backup folder and copies it to the destination using `shutil.copy2()` (which preserves metadata).

---

## 🛠️ Example Use Case

Let's say you accidentally deleted `report.pdf` from your desktop, but you have a backup in your `Downloads` folder. You can call:

```python
recover_deleted_file("report.pdf", r"C:\Users\DELL\Downloads", r"C:\Users\DELL\Desktop")
```

This will copy the file back to the desktop.

---

## 🔒 Limitations

- Does **not** recover files that are permanently deleted from disk with no backup.
- This script does **not** scan for deleted files on disk sectors (not low-level recovery).
- Make sure your backup folder is accessible and not corrupted.

---

## 📚 Future Enhancements

- GUI version using Tkinter or PyQt
- Logging feature to keep track of recovered files
- Version history (store multiple versions of recovered files)
- Automatic scan for lost files by name

---

## 🧑‍💼 Author

**Your Name**  
[LinkedIn](https://linkedin.com) • [GitHub](https://github.com) • [Email](mailto:you@example.com)

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

```

---

Let me know if you'd like to add:
- A GUI interface
- Error logging
- Drag-and-drop support
- Or turn it into an `.exe` with `pyinstaller`

I’d be happy to help!
