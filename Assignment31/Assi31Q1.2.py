import os
import sys

def DirectoryRename(path, old_ext, new_ext):
    try:
        if not os.path.isdir(path):
            print("Invalid directory")
            return

        for file in os.listdir(path):
            if file.endswith(old_ext):
                old_path = os.path.join(path, file)
                new_file = file.replace(old_ext, new_ext)
                new_path = os.path.join(path, new_file)
                os.rename(old_path, new_path)

    except Exception as e:
        print("Error:", e)

def main():
    if len(sys.argv) != 4:
        print("Usage: DirectoryRename.py Directory .old .new")
        return

    DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()

# Outpuut is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi31Q1.2.py
# Usage: DirectoryRename.py Directory .old .new