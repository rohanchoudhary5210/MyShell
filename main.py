import sys
import os
import shlex  # For proper argument parsing, including handling of quotes


def find_in_path(param):
    """Find a command in the system PATH."""
    path = os.environ['PATH']
    for directory in path.split(":"):
        if os.path.isdir(directory):  # Ensure it's a valid directory
            for filename in os.listdir(directory):
                if filename == param:
                    return os.path.join(directory, filename)
    return None


def main():
    """Main REPL loop."""
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command_line = input().strip()  # Get user input

        if not command_line:  # Skip empty commands
            continue

        try:
            # Use shlex.split to handle quoted arguments properly
            args = shlex.split(command_line)
        except ValueError as e:
            print(f"Error parsing command: {e}")
            continue

        if not args:
            continue

        cmd = args[0]
        cmd_args = args[1:]

        # Match cases for handling commands
        match cmd:
            case "exit" if cmd_args == ["0"]:
                exit(0)
            case "echo":
                # Simply join and print the arguments to simulate `echo`
                print(" ".join(cmd_args))
            case "pwd":
                print(os.getcwd())  # Print the current working directory
            case "cd":
                if cmd_args:  # Check if an argument is provided
                    path = cmd_args[0]
                    if path == "~":  # Handle the ~ character
                        home_dir = os.environ.get("HOME")
                        if home_dir:
                            try:
                                os.chdir(home_dir)
                            except PermissionError:
                                print(f"cd: {home_dir}: Permission denied")
                        else:
                            print("cd: HOME environment variable not set")
                    elif os.path.isabs(path):  # Handle absolute paths
                        try:
                            os.chdir(path)
                        except FileNotFoundError:
                            print(f"cd: {path}: No such file or directory")
                        except NotADirectoryError:
                            print(f"cd: {path}: Not a directory")
                        except PermissionError:
                            print(f"cd: {path}: Permission denied")
                    elif path.startswith("./") or path.startswith("../") or path == "." or path == "..":
                        try:
                            os.chdir(path)  # Handle relative paths
                        except FileNotFoundError:
                            print(f"cd: {path}: No such file or directory")
                        except NotADirectoryError:
                            print(f"cd: {path}: Not a directory")
                        except PermissionError:
                            print(f"cd: {path}: Permission denied")
                    else:
                        print(f"cd: {path}: Unsupported path type")
                else:
                    print("cd: missing operand")
            case "type":
                if cmd_args:
                    match cmd_args[0]:
                        case "echo" | "exit" | "type" | "pwd" | "cd":
                            print(f"{cmd_args[0]} is a shell builtin")
                        case _:
                            location = find_in_path(cmd_args[0])
                            if location:
                                print(f"{cmd_args[0]} is {location}")
                            else:
                                print(f"{cmd_args[0]} not found")
                else:
                    print("type: missing arguments")
            case "cat":
                for file_path in cmd_args:
                    try:
                        with open(file_path, "r") as f:
                            print(f.read(), end="")  # Print file content without extra newlines
                    except FileNotFoundError:
                        print(f"cat: {file_path}: No such file or directory")
                    except PermissionError:
                        print(f"cat: {file_path}: Permission denied")
            case _:
                # Handle non-built-in commands
                location = find_in_path(cmd)
                if location:
                    os.system(command_line)  # Execute the command
                else:
                    print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
