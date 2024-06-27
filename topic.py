#text file = modes: Write, Read, Append
"""
file = open("sbc-d8-sample.txt", "w")   # mode = write

file = open("sbc-d8-sample.txt", "a")   # mode = append

#Read

file = open("storage.txt", "r")   # mode = read
print(file.read())                 #read all content

file = open("storage.txt", "r")   
var = file.read()
print(var[0:6])                 #slicing in reading text file

file = open("storage.txt", "r")   
var = file.readlines()              #readlines = text file content in list with new line
print(var[1])                       #indexing

lines = [line.strip() for line in open("storage.txt")]   #reading text file using for loop
for line in lines:  
    print(line)                         

#Write

wr = open("storage.txt", "w")           #writing text in a specific text file using write mode (w)
wr.write("hello")
wr.write("\nsummer")                #use new line ("\n") to avoid writing multiple text in 1 line
wr.write("\ngoodbye")
wr.close()

wrt = open("storage.txt", "w") 
print("Hello", file=wrt)
print("Summer", file=wrt)
print("Goodbye", file=wrt)
wrt.close()

fname = "aljieo"
lname = "tolibas"
wrt = open("storage.txt", "w") 
print(fname, file=wrt)
print(lname, file=wrt)
wrt.close()
"""
#Append

while True:
    app = open("storage.txt", "a")
    name = input("Name: ")
    print(name, file=app)
    app.close()
    if name == "quit":
        break



