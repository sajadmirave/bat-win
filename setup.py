# write os command and find module path
import os

# commands
from src.commands.Ls.root import root_path as root_path_ls
from src.commands.Cat.root import root_path as root_path_cat
from src.commands.Touch.root import root_path as root_path_touch

# set all commands
os.system(f'doskey bat-ls={root_path_ls}\index.bat') #bat-ls
os.system(f'doskey bat-cat={root_path_cat}\index.bat') #bat-cat
os.system(f'doskey bat-touch={root_path_touch}\index.bat') #bat-touch