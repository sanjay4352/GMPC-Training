import json
tasklist=[]
fileName="todoitems.json"



def getFileData():
    file=open(fileName,"r")
    # taskData= file.read()
    taskData = json.load(file)
    file.close()
    print(taskData)
    return list(taskData)

def writeIntoFile(dataItems):
    file=open(fileName,"w")
    # file.write(str(dataItems))
    json.dump(dataItems,file)
    file.close()


tasklist = getFileData()
    


def addItem(id,title,cat,priority,status="Pending"):
    item={
        "id":id,
        "title":title,
        "category":cat,
        "status":status,
        "priority":priority
    }
    tasklist.append(item)
    print("Tash has been added")

def deleteItem(id):
    index=-1
    for x in tasklist:
        index += 1
        if x["id"]==id:
            tasklist.pop(index)


def updateStatus(id,status):
    index=-1
    for x in tasklist:
        index += 1
        if x["id"]==id:
            tasklist[index]["status"]=status

def editItem(id,key,value):
    index=-1
    for x in tasklist:
        index += 1
        if x["id"]==id:
            tasklist[index][key]=value


addItem("1","To have a meeting with someone","Meeting","high")
addItem("2","To have a meeting with someone","Meeting","high")
addItem("3","To have a meeting with someone","Meeting","high")
addItem("4","To have a meeting with someone","Meeting","high")

# deleteItem("3")

# updateStatus("1","Completed")
# editItem("1","title","CHanged Value")
# addItem()

writeIntoFile(tasklist)

