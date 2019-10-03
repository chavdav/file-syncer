from os import listdir, getcwd, remove
from os.path import isfile, join, splitext, basename, sep
from glob import glob

modifiedPath = getcwd() + sep + input("Enter the relative path for the files have been deleted from: ")
otherPath = getcwd() + sep + input("Enter the relative path for the files you WISH TO DELETE: ")

modifiedExtensions = {input("Enter the file extension for the files that have been deleted: ")}
otherExtensions =  {input("Enter the file extension for the files that you WISH TO DELETE: ")}

for me in modifiedExtensions:
    modifiedFiles = glob(modifiedPath + "/*." + me)

for mf in modifiedFiles.copy():
    modifiedFiles.remove(mf)
    mf = splitext(basename(mf))[0]
    modifiedFiles.append(mf)

filesToDelete = []
for oe in otherExtensions:
    otherfiles = glob(otherPath + "/*." + oe)

    for f in otherfiles:
        if splitext(basename(f))[0] not in modifiedFiles:
            filesToDelete.append(f)
print() #newline
print(*filesToDelete, '\n')
if 'y' == input("Do you wish to delete these files? (y/n): "):
    print("deleting...")
    for f in filesToDelete:
        remove(f)
