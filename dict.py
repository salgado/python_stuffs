name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
myemail=dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        myemail[words[1]] = myemail.get(words[1],0) + 1

mykey=None
myGT = -1
for key in myemail:
    if myemail[key] > myGT:
        myGT = myemail[key]
        myKey = key
        
print myKey, myemail[myKey]
        