import sys
import subprocess

try:
    # filename from command argument
    # filename = sys.argv[1]

    filename = "prova.txt"
    with open(filename, "r") as f:
        lines = f.read().split('\n')
except IndexError:
    print("ERROR: No file name specified. Please provide a file name as an argument.")
    exit(1)
except FileNotFoundError:
    print(f"ERROR: The file '{filename}' doesn't exist.")
    exit(1)
except PermissionError:
    print(f"ERROR: You don't have permission to access the file '{filename}'.")
    exit(1)
except:
    print(f"ERROR: An unknown error occurred while opening the file {filename}.")
    exit(1)

# filename = "script.sh"

for line in lines:
    command = line.split()
    run = subprocess.run(command, capture_output=True, text=True)
    # if output does not have new-lines, remove 'sep' parameter
    if run.stderr:
        print(f"ERROR: {run.stderr}", sep="")
    else:
        print(run.stdout, sep="")