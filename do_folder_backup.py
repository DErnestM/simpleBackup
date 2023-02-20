import shutil
import time
import os

# Define the paths of the folders
origin_folder = os.path.abspath('../folderOrigen')
dropbox_folder = os.path.abspath('../folderDropbox')

def backup_folder():
    try:

        current_time = time.strftime('%b-%d-%Y-h%H-m%M-s%S')
        backup_name = f'backup_{current_time}'
        
        # Compress the origin folder
        shutil.make_archive(backup_name, 'zip', origin_folder)

        print(f"File {backup_name}.zip created")
        
        # Move the compressed folder to the Dropbox folder
        full_path = os.path.join(dropbox_folder, f'{backup_name}.zip')
        shutil.move(f'{backup_name}.zip', full_path)
        
        print(f"file moved to {dropbox_folder}")

        # Get the size of the compressed folder
        file_size = os.path.getsize(full_path) / (1024 * 1024)

        # Write a record into the log file
        with open("backup_log.txt", "a") as log_file:
            log_file.write("-------------------------\nBackup created successfully on {}.\nBackup name:{}\nSize of backup: {:.2f} MB\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),backup_name, file_size))

    except Exception as e:
        print(f"An error ocurred: {e}")
    
    finally:
        print("Backup completed, if no error ocurred, it was successfull")

if __name__ == "__main__":
    backup_folder()