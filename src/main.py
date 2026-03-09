import os
import shutil

CURR_DIR = os.path.abspath(__file__)
ROOT_DIR = os.path.dirname(os.path.dirname(CURR_DIR))
SOURCE_DIR = os.path.join(ROOT_DIR, 'static')
TARGET_DIR = os.path.join(ROOT_DIR, 'public')

def copy_dir(dir):
    source = os.path.join(SOURCE_DIR, dir)
    target = os.path.join(TARGET_DIR, dir)
    dir_contents = os.listdir(source)
    dirs = []
    if not os.path.exists(target):
        os.mkdir(target)
    for obj in dir_contents:
        is_file = os.path.isfile(os.path.join(source,obj))
        print(f"{obj} is file? {is_file}")
        if is_file:
            print(f"attempting to copy file {obj}")
            shutil.copy(os.path.join(source, obj), os.path.join(target, obj))
        else:
            print(f"attempting to copy non-file {obj}")
            copy_dir(os.path.join(dir,obj))
        
def main():
    if os.path.exists(TARGET_DIR):
        shutil.rmtree(TARGET_DIR)
    copy_dir('')

if __name__ == "__main__":
    main()
