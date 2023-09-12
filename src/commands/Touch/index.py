import sys
import os

# Add the parent directory (commands/Ls) and the project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import style

# Now you can use elements from style.py
output = style.output_style

# bat-touch filename -> content
# 0           1      2,3 4
args = sys.argv
file_name = args[1]
content = args[3:] #get content

with open(file_name,'w') as file:
    for item in content:
        if item == ".n" :
            newItem = '\n'
        else:
            newItem = item

        file.write(newItem)    
    print(output['success'],"success")