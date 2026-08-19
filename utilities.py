import shutil
import datetime
from pathlib import Path

timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H.%M.%S")

def backup(src_path, dst_path):
    valid_items = []
    src_path = Path(src_path)
    dst_path = Path(dst_path)
    if src_path.is_dir():
        for item in src_path.iterdir():
            if item.is_file() and item.suffix == '.hg':
                valid_items.append(item)
    elif src_path.is_file() and src_path.suffix == '.hg':
        valid_items.append(src_path)
    if valid_items:
        if dst_path.is_dir():
            dst_path = Path(f'{dst_path}/{timestamp}')
            dst_path.mkdir(parents=True, exist_ok=True)
            for item in valid_items:
                print(f'Backing up "{item}" to "{dst_path}"...')
                shutil.copy2(item, dst_path)
            return True
        else:
            print(f'The directory "{dst_path}" does not exist or is not a directory.')
            return False
    else:
        print(f'No valid file found at "{src_path}".')
        return False
