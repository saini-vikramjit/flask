import difflib
import hashlib

def compareFiles(file1, file2):
    with open(file1) as f1:
        f1Text = f1.read()

    with open(file2) as f2:
        f2Text = f2.read()

    print(hashlib.md5(f1Text).hexdigest())
    print(hashlib.md5(f2Text).hexdigest())

    
