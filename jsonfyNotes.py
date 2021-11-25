from copy import deepcopy
import json
import os
import re
import sys
import uuid
import datetime,time,pytz

#max preview_plain = 80 

italy = pytz.timezone("Europe/Rome")

file = open(sys.argv[2],"r", encoding="utf8")  #memos/notes file
creationFile = open(sys.argv[3])      #the file containing the creation time 
modificationFile = open(sys.argv[4])    #the file containing the modification time 


ff = open("backup.json","w",encoding="utf-8")  #the output file


i = 0
tempStr = ""
dic = {}
content_dic = {}

appData_dic = {}
update_info_dic = {}
list = []


def standardN():
    initializationString =  """{
      "version": "004",
      "items": """

    ff.write(initializationString)


    initializingdic = {
          "uuid": str(uuid.uuid4()),
          "content_type": "SN|UserPreferences",
          "content": {
            "references": [],
            "appData": {
              "org.standardnotes.sn": {
                "client_updated_at": "Wed Nov 24 2021 16:13:05 GMT+0100"
              }
            }
          },
          "created_at": "2021-11-24T15:13:05.417Z",
          "updated_at": "1970-01-01T00:00:00.000Z"
        }


    list.append(deepcopy(initializingdic))

    newReading = False
    for line in file:
        
        if line.find("Text|")==0:
                newReading = True  #line starts with "Text|"
                line = line.replace('Text|','')
                if i>0:  #not the first read
                        list.append(deepcopy(dic))  #append the previous completed dictionary
        if newReading:
                    i+=1
                    dic['uuid'] = str(uuid.uuid4()) #random uuid identifier
                    dic['content_type'] = "Note"
                    timestamp = int(creationFile.readline()[0:10].replace("\n",''))
                    dt = datetime.datetime.fromtimestamp(timestamp, italy)
                    isoformat = dt.isoformat()
                    dic['created_at'] = isoformat #----Date in ISO format (as a string)-----   ///////////////////////////
                    dic['updated_at'] = "1970-01-01T00:00:00.000Z" #fixed this way in all notes by Stanard notes developers..
                    dic['content'] = content_dic

                    content_dic['title'] = ""  #will be used preview_plain instead
                    content_dic['references'] =[]
                    if len(line)>80:
                        content_dic['preview_plain'] = line[0:80].rstrip("\n") + "..." #remove the last "\n" and considers only the first 80 characters 
                    else:
                        content_dic['preview_plain'] = line.rstrip("\n")



                    timestamp = int(modificationFile.readline()[0:10].replace("\n",''))
                    dt = datetime.datetime.fromtimestamp(timestamp, italy)
                    isoformat = dt.isoformat()
                    update_info_dic ['client_updated_at'] = isoformat #----Date in ISO format (as a string)-----   ///////////////////////////

                    appData_dic['org.standardnotes.sn'] = update_info_dic

                    content_dic['appData'] = appData_dic
                    

                    tempStr = line
                    newReading = False



                    #dic['title'] = line[0:80] + "..."
                    #dic['title'] = line.replace("\n",'')[0:80] + "..."
                    #dic['creationDate'] = int(creationFile.readline()[0:10].replace("\n",''))   #read a line consider just the first 10 "chars" get ride of the "\n" convert the result into an integer -- in's the unix timestamp of the note.
                    #dic['modifiedDate'] = int(modificationFile.readline()[0:10].replace("\n",''))
                    #dic['id']= i

        else:
                    tempStr = tempStr + line
                     
        content_dic['text'] = tempStr

        #dic['content'] = tempStr

    print("\nNumber of converted notes = "+str(i))

    list.append(deepcopy(dic)) # to write the last dictionary into the list
    ff.write(json.dumps(list,ensure_ascii = False)) # ensure_ascii = False--> to work with other letters than latin ones



def quilloN():
    ff.write("{\"version\":4,\"notes\":")
    
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
    ff.write(json.dumps(list,ensure_ascii = False)) # ensure_ascii = False--> to work with other letters than latin ones




if str(sys.argv[1]) == "quillo":
    quilloN()
elif str(sys.argv[1]) == "standard":
    standardN()



ff.write("}")

ff.close()
file.close()
creationFile.close()
modificationFile.close()

