# save data in file
import sys
import os


# Add the parent directory (commands/Ls) and the project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from storage import root

# bat-db -C collection_name -R read data
# bat-db -add data -uname my_unique_name
#  0        1   2   3       4
args = sys.argv

def write():
    data = args[2] #data
    uname = args[4] #data

    with open(f"src/storage/{uname}.txt","w") as file:
        file.write(data)

def read():
    uname = args[2]

    with open(f"src/storage/{uname}.txt",'r') as file:
        data = file.readline()
        print(data)

def dbs():
    storage_path = root.root_path
    dbs = os.listdir(storage_path)

    for i in dbs:
        if ".txt" in i:
            # print(i)
            x = i.replace('.txt','')
            print(x)

def help():
    print("""
    add: --add content --uname unique_name
    read: --uname unique_name
    show all db: --dbs
    """)

if args[1] == "--add": write()

# bat-db -read uname
if args[1] == "--read": read()

if args[1] == '--dbs': dbs()

if args[1] == '--help': help()

else: print('invalid command! | type bat-db --help')
