f = open("links.txt", "r")


for line in f:


   newstr = line
   newstr = newstr[35:-10]
   if newstr[0].isdigit():
       newstr = newstr[2:]


   elif newstr[0] == '/':
       newstr = newstr[1:]


   newstr = newstr.replace('-', ' ')


   print(newstr + '\n')


