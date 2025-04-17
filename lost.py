import os
import shutil

def recover_deleted_file(filename, backup_folder, destination_folder):
    """
    Recover a deleted file from a backup folder to the destination folder.
    """
    backup_path = os.path.join(backup_folder, filename)
    destination_path = os.path.join(destination_folder, filename)

    if os.path.exists(backup_path):
        shutil.copy2(backup_path, destination_path)
        print(f"✅ Recovered '{filename}' to '{destination_folder}'")
    else:
        print(f"❌ Backup for '{filename}' not found in '{backup_folder}'.")

# Example usage
recover_deleted_file("important_data.txt", "C:\\Users\\DELL\\Downloads", "D:\\data")
