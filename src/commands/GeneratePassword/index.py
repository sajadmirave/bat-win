from random import randint
import pyperclip
import sys
# copy password

# bat-create-pass -l 20
args = sys.argv

if len(args) == 3:
    password_length = int(args[2])
else:
    password_length = 8

small_letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
simbol = "*&^%$#@!?"
number = "1234567890"
char = small_letters + capital_letters + simbol + number

result = ""
for i in range(password_length):
    x = randint(0,len(char) - 1)
    result += char[x]

print(result)
print("password copied...")
pyperclip.copy(result)