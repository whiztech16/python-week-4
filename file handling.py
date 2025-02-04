import os

file=open("my data.txt","r") 
print(file.read())

# writing a new file
newfile= open("filename.txt","w")
newfile.write("we add the content of that file ")



#  error handling and exception
try:
    file= open("filename.txt","r")
    print(file.read())
except FileNotFoundError:
    print("oops file does not exist")    
finally:
    print("it was nice meeting you ")   