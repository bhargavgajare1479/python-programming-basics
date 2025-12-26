import os
import sys

print("---- SYSTEM INFORMATION ----")
print("OS Name:", os.name)
print("Platform:", sys.platform)
print("Python Version:", sys.version)
print("Current Working Directory:", os.getcwd())

print("\n---- DIRECTORY OPERATIONS ----")
# Create directory
if not os.path.exists("DemoFolder"):
    os.mkdir("DemoFolder")
    print("Directory created: DemoFolder")

# List files
print("Files in current directory:", os.listdir())

print("\n---- FILE OPERATIONS ----")
# Create and write file
file = open("DemoFolder/sample.txt", "w")
file.write("This file demonstrates system-level actions in Python.")
file.close()
print("File written")

# Read file
file = open("DemoFolder/sample.txt", "r")
print("File content:", file.read())
file.close()

print("\n---- SYSTEM COMMAND ----")
os.system("echo Hello from the Operating System")

print("\n---- RENAME & DELETE ----")
os.rename("DemoFolder/sample.txt", "DemoFolder/renamed.txt")
print("File renamed")

os.remove("DemoFolder/renamed.txt")
print("File deleted")

os.rmdir("DemoFolder")
print("Directory removed")

print("\n---- PROGRAM COMPLETED ----")