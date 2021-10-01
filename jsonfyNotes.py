from copy import deepcopy
import json
import os
import re
import sys




file = open(sys.argv[1],"r", encoding="utf8")  #memos/notes file
creationFile = open(sys.argv[2])      #the file containing the creation time 
modificationFile = open(sys.argv[3])    #the file containing the modification time 


ff = open("backup.json","w",encoding="utf-8")  #the output file
ff.write("{\"version\":4,\"notes\":")
i = 0
tempStr = ""
dic = {}
list = []
newReading = False
for line in file:
    
    if line.find("Text|")>-1:
            newReading = True  #line starts with "Text|"
            line = line.replace('Text|','')
            if i>0:  #not the first read
                    list.append(deepcopy(dic))  #append the previous completed dictionary
    if newReading:
                i+=1
                dic['title'] = line.replace("\n",'')[0:43] + "..."
                tempStr = line
                newReading = False
                dic['creationDate'] = int(creationFile.readline()[0:10].replace("\n",''))   #read a line consider just the first 10 "chars" get ride of the "\n" convert the result into an integer -- in's the unix timestamp of the note.
                dic['modifiedDate'] = int(modificationFile.readline()[0:10].replace("\n",''))
                dic['id']= i

    else:
                tempStr = tempStr + line
                 
    dic['content'] = tempStr

print("\nNumber of converted notes = "+str(i))

list.append(deepcopy(dic)) # to write the last dictionary into the list

ff.write(json.dumps(list))

ff.write("}")

ff.close()
file.close()
creationFile.close()
modificationFile.close()

