#!/usr/bin/env python
import sys
import os

# Add the parent directory (commands/Ls) and the project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import style

# Now you can use elements from style.py
color = style.colors

# cat filename > colorname
args = sys.argv
file_name = sys.argv[1]

def handle_output(color_selected):
    match(color_selected):
        case "red":
            print(color['RED'],end='')
        case "yellow":
            print(color['YELLOW'],end='')
        case "green":
            print(color['GREEN'],end='')
        case "magenta":
            print(color['MAGENTA'],end='')
        case "cyan":
            print(color['CYAN'],end='')
        case "blue":
            print(color['BLUE'],end='')


# print(args)
for index,arg in enumerate(args):
    if arg == "--color=":
        output_color = args[index+1] # access to color
        handle_output(output_color)

with open(file_name,'r') as file:
    file_content = file.readlines()

    for line in file_content:
        print(line,end='')