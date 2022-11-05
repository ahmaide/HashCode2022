f = open("input.txt", 'r')
data = f.readlines()
line1 = data[0].split(" ")
w = int(line1[0])
p = int(line1[1])
done = 0
workersList = []
projectsList = []
languageList = []
count = True

class worker:
    def __init__(self, name, l):
        self.name = name
        self.l = l
        self.list = []
        self.busy = False

class language:
    def __init__(self, name, level):
        self.level = level
        self.name = name
        m = 0
        exist = False
        if count == True:
            for m in range(languageList.__len__()):
                if languageList[m].name == self.name:
                    exist = True
                    if languageList[m].level < self.level:
                        languageList[m].level = self.level
                        break
            if (exist == False):
                languageList.append(self)



class project:
    def __init__(self, name,days, d1, d2, l):
        self.name = name
        self.days = days
        self.d1 = d1
        self.d2 = d2
        self.l = l
        self.list = []
        self.filled = False
        self.list2 = []
        self.order = 0
        self.workOn = 0
        self.daysWorked = 0

pointer = 1
for i in range(w):
    infoList = data[pointer].split(" ")
    cn = infoList[0]
    cl = int(infoList[1])
    workersList.append(worker(cn, cl))
    pointer+=1
    for j in range(cl):
        infoList = data[pointer].split(" ")
        cn = infoList[0]
        cl = int(infoList[1])
        workersList[i].list.append(language(cn, cl))
        pointer+=1
count = False
for i in range(p):
    infoList = data[pointer].split(" ")
    a0 = infoList[0]
    a1 = int(infoList[1])
    a2 = int(infoList[2])
    a3 = int(infoList[3])
    a4 = int(infoList[4])
    projectsList.append(project(a0, a1, a2, a3, a4))
    pointer+=1
    for j in range(a4):
        infoList = data[pointer].split(" ")
        cn = infoList[0]
        cl = int(infoList[1])
        projectsList.append(language(cn, cl))
        pointer+=1

def checkIfDone():
    d = True
    for pro in projectsList:
        if pro.workOn != 2:
            d = False
    return d

def setFilled(pro):
    if pro.list2.__len__() == pro.list.__len__():
        pro.filled = True

def checkExWorker(project0):
    for langage in project0.list:
        found = False
        for wo in workersList:
            if wo.busy == False:
                hasIt = False
                for lang in wo.list:
                    if (lang.name == langage.name) and (lang.level + 1 >= langage.level):
                        if (lang.level < language.level):
                            found2 = False
                            for inner in project0.list2:
                                hasIt2 = False
                                for ll in inner.list:
                                    if (ll.name == langage.name) and (ll.level >= language.level):
                                        hasIt2 = True
                                        found2 = True
                                        hasIt = True
                                        found = True
                                        project0.list2.append(wo)
                                        wo.busy = True
                                    if hasIt2:
                                        break
                            if found2:
                                break
                        else:
                            hasIt = True
                            found = True
                            project0.list2.append(wo)
                            wo.busy = True
                    if hasIt:
                        break

                if found:
                    break
    setFilled(project0)
    aaa = False
    if(project0.filled == True):
        aaa= True
    for jj in project0.list2:
        jj.busy = False
    project0.list2 = []
    project0.filled = False
    return aaa






