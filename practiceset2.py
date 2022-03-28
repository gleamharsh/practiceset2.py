# IT WILL OPEN THE FILE AND WILL READ CONTENT
f = open("sample.txt","r") #OPENING FILE
data = f.read() # READING CONTENT
print(data) # PRINTING CONTENT
f.close() # CLOSING THE FILE

f = open("sample.txt","r")
data = f.readline() # READLINE WILL READ ONLY ONE(FIRST) LINE AT A TIME
print(data)
data = f.readline() # IT WILL READ SECOND LINE
print(data)
f.close()

# IT WILL OPEN THE FILE AND WILL READ CONTENT
f = open("sample.txt","rb") #OPENING FILE IN BINARY MODE "rb"
data = f.read() # READING CONTENT
print(data) # PRINTING CONTENT
f.close() # CLOSING THE FILE

# OPENING A FILE IN WRITE MODE A WRITTING SOME NEW ELEMENTS
f = open("another.txt","w")
f.write("Please write this text to another file.\nHarshaa is a good boy")
f.close()

# OPENING A FILE IN APPENDIN MODE AND ADDING ELEMENTS
f = open("sample.txt","a") # APPEND MODE "a"
f.write("\nI am new user here.") # ADDING TEXT
f.close()
# *************************************************************************************************
# CHAPTER-9 PRACTICE SET
# PROBLEM-1
f = open("poem.txt","r")
data = f.read()
# print(data)
if "twinkle" in data:
    print("Yes twinkle is present in file")
else:
    print("No twinkle is not present in file")
f.close()

# PROBLEM-2
def game():
    return 13
score = game()
with open("hiscore.txt") as f:
    hiscore = int(f.read())
if hiscore<score:
    with open("hiscore.txt","w")as f:
        f.write(str(score))

# # PROBLEM-3 PRINTING MULTIPLICATIONS TABLE OF 2-20
for i in range(2, 21):
    with open(f"tables/multiplications_tables_of{i}.txt","w") as f:
        for j in range(1, 11):
            f.write(f"{i}x{j}={i*j}")
            if j!=10:
                f.write('\n')

# PRACTICE TO PRINT TABLES 21-40 
for i in range(21,41):
    with open(f"newtables/Multiplication_tables_{i}.txt","w")as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}\n")
            if j!=10:
                f.write('\n')

# PROBLEM-4 
with open("donkey.txt","r")as f:
    data = f.read()
    # print(data)

# data = data.replace("donkey","love") # will replace donkey with love
# with open("donkey.txt","w")as f: # replacing function part
#     f.write(data)


with open("donkey.txt","a")as f: # adding new elements or appending elements
    data = f.write('''
I have a donkey
I have a donkey
I have a donkey
I have a donkey
I have a donkey
I have a pet
I have a pet
I have a pet''')

#PROBLEM-5 REPLACING ALL WORDS IN A LIST
words = ["harsh","gagan"]
with open("words.txt","r") as f:
    data = f.read()

for word in words:
    data = data.replace(word,"Babu")

with open("words.txt","w")as f:
    f.write(data)

# PROBLEM-6 CHECKING WHETHER PYTHON PRESENT IN A LOG FILE OR NOT
with open("logfile.txt","r")as f:
    data = f.read()
if "python" in data:
    print("Yes your logfile contain python")
else:
    print("No your logfile does not contain python")

# PROBLEM-7 GETTING THE LINE NUMBER FOR PYTHON IN LOG FILE
data = True
i = 1
with open("logfile.txt")as f:
    while data:
        data = f.readline()
        if 'python' in data.lower():
            print(data)
            print("Yes present")
            print(i)
        i+=1

# PROBLEM-8 COPYING A TXT FILE
with open("this.txt","r")as f:
    data = f.read()

with open("copy_of_this.txt","w")as f:
    f.write(data)

# PROBLEM-9  IDENTICAL MEANS BOTH FILES HAVE SAME CONTENT
file1 = "this.txt" # if file1 = "logfile.txt" than will display not identical
file2 = "copy_of_this.txt"

with open(file1)as f:
    data1 = f.read()

with open(file2)as f2:
    data2 = f2.read()

if data1==data2:
    print("Files are identical")
else:
    print("Files are not identical")

# PROBLEM-10 WAP to empty a file
with open("sample.txt","w")as f:
    f.write("")

# or we can also do
filename = "sample.txt"
with open(filename,"w")as f:
    f.write("")

# PROBLEM-11 RENAMING A EXISTING FILE
import os
oldname = "sample.txt"
newname = "newsample.txt"
with open(oldname,"r")as f:
    data = f.read()
with open(newname,"w")as f:
    f.write(data)

os.remove(oldname)








    

