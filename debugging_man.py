#!/usr/bin/env python3

"""
p 	Print the value of an expression.
pp 	Pretty-print the value of an expression.
n 	Continue execution until the next line in the current function is reached 
    or it returns.
s 	Execute the current line and stop at the first possible 
    occasion (either in a function that is called or in the current function).
c 	Continue execution and only stop when a breakpoint is encountered.
unt Continue execution until the line with a number greater than the current 
    one is reached. With a line number argument, continue execution until a 
    line with a number greater or equal to that is reached.
l 	List source code for the current file. Without arguments, list 11 
    lines around the current line or continue the previous listing.
ll 	List the whole source code for the current function or frame.
b 	With no arguments, list all breaks. With a line number argument, set a 
    breakpoint at this line in the current file.
w 	Print a stack trace, with the most recent frame at the bottom. An arrow 
    indicates the current frame, which determines the context of most commands.
u 	Move the current frame count (default one) levels up in the stack trace 
    (to an older frame).
d 	Move the current frame count (default one) levels down in the stack trace 
    (to a newer frame).
h 	See a list of available commands.
h <topic> 	Show help for a command or topic.
h pdb 	Show the full pdb documentation.
q 	Quit the debugger and exit.
"""


# import dbutils

# if __name__ == "__main__":
#     filename = __file__
#     breakpoint()
#     filename_path = dbutils.get_path(filename)
#     print(f"path = {filename_path}")


# import os


# def get_path(fname):
#     """Return file's path or empty string if no path."""
#     breakpoint()
#     head, tail = os.path.split(fname)
#     for char in tail:
#         pass  # Check filename char
#     return head


# filename = __file__
# filename_path = get_path(filename)
# print(f"path = {filename_path}")


import dbutils


def get_file_info(full_fname):
    file_path = dbutils.get_path(full_fname)
    return file_path


if __name__ == "__main__":
    filename = __file__
    filename_path = get_file_info(filename)
    print(f"path = {filename_path}")
