import os
import shutil
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_trash_items():
    applescript = '''
    tell application "Finder"
        set trashContents to items of trash
        set output to ""
        repeat with i from 1 to count of trashContents
            set thisItem to item i of trashContents
            set itemName to name of thisItem
            set itemPath to POSIX path of (thisItem as alias)
            set output to output & itemName & "|" & itemPath & "\n"
        end repeat
        return output
    end tell
    '''
    
    cmd = ['osascript', '-e', applescript]
    logging.debug(f"Running command: {cmd}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        items = []
        for line in output.split('\n'):
            if line:
                name, path = line.split('|')
                items.append({'name': name, 'path': path})
        logging.debug(f"Command output: {output}")
        logging.debug(f"get_trash_items returned: {items}")
        return items
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with error: {e.stderr}")
        return []

def recover_items(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
        logging.debug(f"Created destination directory: {destination}")

    recovered_count = 0
    trash_items = get_trash_items()
    logging.debug(f"Found {len(trash_items)} items in trash")
    
    for item in trash_items:
        item_path = item['path']
        item_name = item['name']
        destination_path = os.path.join(destination, item_name)
        logging.debug(f"Attempting to recover: {item_path}")

        try:
            if os.path.exists(item_path):
                shutil.copy2(item_path, destination_path)
                recovered_count += 1
                logging.info(f"Recovered: {item_name}")
            else:
                logging.warning(f"File not found: {item_path}")
        except PermissionError:
            logging.error(f"Permission denied: {item_path}")
        except Exception as e:
            logging.error(f"Failed to recover {item_name}: {str(e)}")

    logging.info(f"Recovery complete. Recovered {recovered_count} items.")
    return recovered_count

if __name__ == "__main__":
    recovery_destination = os.path.expanduser("~/Documents/RecoveredItems")
    recovered_count = recover_items(recovery_destination)
    print(f"Recovered {recovered_count} items to {recovery_destination}")
