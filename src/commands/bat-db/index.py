# save data in file
import sys

# bat-db -C collection_name -R read data
# bat-db -add data -uname my_unique_name
#  0        1   2   3       4
args = sys.argv

if args[1] == "-add": 
    data = args[2] #data
    uname = args[4] #data

    with open(f"src/storage/{uname}.txt","w") as file:
        file.write(data)

# bat-db -read uname
if args[1] == "-read":
    uname = args[2]

    with open(f"src/storage/{uname}.txt",'r') as file:
        data = file.readline()
        print(data)