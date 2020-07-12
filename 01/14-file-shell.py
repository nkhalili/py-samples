import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")

        dst = src + ".bak"

        ## use shell copy command
        #shutil.copy(src, dst)

        ## copy the new file meta-data as same as the original file
        #shutil.copystat(src, dst)

        ## rename file using os modules
        #os.rename("textfile.txt", "newfile.txt")

        ## create a zip file
        #root_dir, tail = path.split(src)
        #shutil.make_archive("archive", "zip", root_dir)

        # fine-grained control over ZIP files (with...as is like using statement)
        with ZipFile("textzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()
