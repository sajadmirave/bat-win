import subprocess
import sys

# bat-explore .
args = sys.argv
path = args[1]

subprocess.Popen(['explorer',path])
