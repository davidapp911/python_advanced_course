# Task instructions

Develop a Python command-line tool that reads a text file, processes its content, and outputs the result to another file. The tool should use a virtual environment, handle command-line arguments, implement logging, and manage exceptions gracefully. Finally, package the tool for distribution.
By completing this task, you will touch on all the essential Python concepts including:
- Packaging and distributing
- Import method implementation
- Working with command line arguments
- Logging events
- Virtual Environments
- Exception Handling
- File I/O
- Decorators

## Detailed Steps:
1. Set up a Virtual Environment
o Create a virtual environment for the project.
o Install any necessary dependencies within this environment.
2. Create the Command-Line Interface
o Use the argparse module to handle command-line arguments.
o Accept input and output file paths as arguments.
3. Implement File I/O
o Read the content from the input file.
o Process the content (e.g., count word frequency, filter specific words, etc.).
o Write the processed content to the output file.
4. Implement Logging
o Set up logging to record the tool’s activity (e.g., when files are read/written, any errors
encountered).
o Use different logging levels (INFO, ERROR).
5. Handle Exceptions
o Use try-except blocks to handle potential errors (e.g., file not found, permission errors).
o Ensure the program does not crash unexpectedly and provides informative error
messages.
6. Use Decorators
o Implement a simple decorator to log the execution time of the main processing function.
7. Package the Tool
o Create a setup.py file for the project.
o Ensure all dependencies are listed and the tool can be installed via pip.
o Optionally, include a requirements.txt file.
8. Implement Import Method
o Organize the code into modules and packages.
o Use appropriate import statements to ensure code is modular and maintainable.