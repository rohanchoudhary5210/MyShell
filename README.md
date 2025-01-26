[![progress-banner](https://backend.codecrafters.io/progress/shell/97d61c9b-7923-4e35-827f-da43c2051c98)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)
# REPL Shell - A Simple Python Shell

This project implements a simple Read-Eval-Print Loop (REPL) shell in Python, providing a basic command-line interface (CLI) environment. It supports several built-in commands (`echo`, `pwd`, `cd`, `type`, `cat`) and the ability to execute external commands found in the system's `PATH`. Additionally, it includes features like argument parsing, error handling, and basic shell functionality.

## Features

- **Basic Shell Commands**: Supports common shell commands such as `echo`, `pwd`, `cd`, `type`, and `cat`.
- **External Command Execution**: Executes non-built-in commands that are located in the directories listed in the `$PATH` environment variable.
- **Argument Parsing**: Handles quoted arguments and special characters (e.g., spaces, quotes) correctly using `shlex.split()`.
- **Error Handling**: Provides informative error messages for common issues (e.g., missing arguments, invalid file paths, permissions errors).
- **Customizable Environment**: Users can navigate directories, display current working directories, print output, and manage file contents.
- **Extensibility**: The shell can be easily extended to include additional features like piping, redirection, and background processes.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repl-shell.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd repl-shell
   ```

3. This project has no external dependencies, so no additional installation is required beyond cloning the repository.

## Usage

To run the REPL shell, execute the following command in your terminal:

```bash
python3 repl_shell.py
```

The shell will start and prompt you with `$`:

```
$ 
```

You can then enter commands just like in a typical Unix shell.

### Example usage:

- **Echo Command**: 
  ```
  $ echo Hello, World!
  Hello, World!
  ```

- **Print Working Directory**:
  ```
  $ pwd
  /home/user
  ```

- **Change Directory**:
  ```
  $ cd /tmp
  $ pwd
  /tmp
  ```

- **List Files in File**:
  ```
  $ cat example.txt
  Hello, this is an example text.
  ```

- **Exit the REPL**:
  ```
  $ exit 0
  ```

## Built-in Commands

The REPL shell supports several built-in commands:

1. **`echo`**: Prints the arguments passed to the command.
   - Example: `echo Hello, World!`

2. **`pwd`**: Prints the current working directory.
   - Example: `pwd`

3. **`cd`**: Changes the current directory to the specified path.
   - Example: `cd /home/user`

4. **`type`**: Displays whether a command is built-in or shows its location in the system’s `PATH`.
   - Example: `type echo`

5. **`exit 0`**: Exits the REPL with a success status code.
   - Example: `exit 0`

## Non-Built-in Commands

If a command is not a built-in, the REPL shell will search for the command in the system's `PATH`. If found, the command is executed using `os.system()`.

Example:
```
$ ls
$ python3 --version
```

If the command is not found, an error message will be printed:
```
$ my_custom_command
my_custom_command: command not found
```

## Error Handling

The REPL shell handles several common error scenarios:

- **Empty Input**: Ignores empty input and prompts for the next command.
- **Argument Parsing Errors**: Provides clear messages if there are issues parsing command arguments (e.g., unmatched quotes).
- **File and Directory Errors**:
  - **File Not Found**: For commands like `cat`, if a file is not found, an appropriate error message is printed.
  - **Permission Denied**: If a file or directory is inaccessible due to permission issues, the shell will display a permission error.

Example:
```
$ cat nonexistent_file.txt
cat: nonexistent_file.txt: No such file or directory
```

## Enhancements (Planned)

### 1. **Pipelining (`|`) and Redirection (`>`, `>>`)**
Support for piping and output redirection allows chaining commands and redirecting output to files.

Example:
```
$ echo "Hello, World!" | grep "World"
Hello, World!
$ echo "Hello, World!" > output.txt
```

### 2. **Background Processes (`&`)**
Run commands in the background by appending `&` at the end of a command.

Example:
```
$ long_running_command &
```

### 3. **Command History and Recall**
Implement a history feature to allow users to recall previously executed commands.

### 4. **Variable Support**
Allow users to define and use variables within the shell.

Example:
```
$ var="Hello, World!"
$ echo $var
Hello, World!
```

### 5. **Job Control**
Allow suspending and resuming processes using job control commands like `fg`, `bg`, and `jobs`.

### 6. **Color-Coded Output**
Implement color-coded output for better user experience (e.g., green for success, red for errors).

### 7. **Scripting Support**
Support running shell scripts (or Python scripts) from within the REPL environment.

---

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request. You can also open an issue for any feature requests or bug reports.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by Unix-like shells (Bash, Zsh, etc.).
- Built using Python's standard libraries: `os`, `shlex`, `sys`.
- Special thanks to open-source communities for building powerful and extensible shell environments.

---

