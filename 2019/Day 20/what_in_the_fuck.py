def makeportals():
    global coords
    global portals
    global startend
    e=0
    while e < len(coords):
        if coords[e][2] == ".":
            for f in coords:
                if coords[e][0] == f[0] and coords[e][1] == (f[1]-1):
                    if str(f[2]).isalpha():
                        for g in coords:
                            if f[0] == g[0] and f[1] == (g[1]-1):
                                code = (str(f[2]) + str(g[2]))
                                temp = (f[0], f[1], code)
                                portals.append(temp)
                if coords[e][0] == f[0] and coords[e][1] == (f[1]+1):
                    if str(f[2]).isalpha():
                        for g in coords:
                            if f[0] == g[0] and f[1] == (g[1]+1):
                                code = (str(g[2]) + str(f[2]))
                                temp = (f[0], f[1], code)
                                portals.append(temp)
                if coords[e][0] == (f[0]-1) and coords[e][1] == f[1]:
                    if str(f[2]).isalpha():
                        for g in coords:
                            if f[0] == (g[0]-1) and f[1] == g[1]:
                                code = (str(f[2]) + str(g[2]))
                                temp = (f[0], f[1], code)
                                portals.append(temp)
                if coords[e][0] == (f[0]+1) and coords[e][1] == f[1]:
                    if str(f[2]).isalpha():
                        for g in coords:
                            if f[0] == (g[0]+1) and f[1] == g[1]:
                                code = (str(g[2]) + str(f[2]))
                                temp = (f[0], f[1], code)
                                portals.append(temp)
        e+=1
    for e in portals:
        if e[2] == "AA" or e[2] =="ZZ":
            temp = (e[0], e[1])
            startend.append(e)
        

def makecrossroads():
    global coords
    global crossroads
    e=0
    while e < len(coords):
        counter = 0
        if coords[e][2] == ".":
            for f in coords:
                if coords[e][0] == f[0] and coords[e][1] == (f[1]-1):
                    if f[2] == ".":
                        counter += 1
                if coords[e][0] == f[0] and coords[e][1] == (f[1]+1):
                    if f[2] == ".":
                        counter += 1
                if coords[e][0] == (f[0]-1) and coords[e][1] == f[1]:
                    if f[2] == ".":
                        counter += 1
                if coords[e][0] == (f[0]+1) and coords[e][1] == f[1]:
                    if f[2] == ".":
                        counter += 1
                if counter > 2:
                    temp = (coords[e][0], coords[e][1], "@")
                    coords[e] = temp
                    if temp not in crossroads:
                        crossroads.append(temp)
        e+=1


def makewalls():
    global coords
    switch = False
    e=0
    while e < len(coords):
        counter = 0
        if coords[e][2] == ".":
            for f in coords:
                if coords[e][0] == f[0] and coords[e][1] == (f[1]-1):
                    if f[2] == "#":
                        counter += 1
                if coords[e][0] == f[0] and coords[e][1] == (f[1]+1):
                    if f[2] == "#":
                        counter += 1
                if coords[e][0] == (f[0]-1) and coords[e][1] == f[1]:
                    if f[2] == "#":
                        counter += 1
                if coords[e][0] == (f[0]+1) and coords[e][1] == f[1]:
                    if f[2] == "#":
                        counter += 1
                if counter == 3:
                    temp = (coords[e][0], coords[e][1], "#")
                    coords[e] = temp
                    switch = True
        e+=1
    if switch == True:
        visible()
        makewalls()
                
def visible():
    visual = ""
    e=0
    while e < len(coords):
        visual += coords[e][2]
        e+=1
    print(visual)
                
def makecoords():
    global coords
    h = open("test-1.txt")
    lines = h.readlines()
    a=0
    b=0
    maxlen = 0
    for p in lines:
        if len(p) > maxlen:
            maxlen = len(p)
    e=0  
    while e < len(lines):
        if len(lines[e]) < maxlen:
            templine = maxlen - len(lines[e])
            lines[e] = lines[e] + (templine * " ")
        a=0
        for f in lines[e]:
            temp = (a, b, f)
            coords.append(temp)
            a+=1
        b+=1
        e+=1

def teleport(portalcoord):
    global coords
    e=0
    while e < len(coords):
        if (portalcoord[0]-1) == coords[e][0] and portalcoord[1] == coords[e][1]:
            if coords[e][2] == ".":
                return coords[e]
        if (portalcoord[0]+1) == coords[e][0] and portalcoord[1] == coords[e][1]:
            if coords[e][2] == ".":
                return coords[e]
        if portalcoord[0] == coords[e][1] and (portalcoord[1]-1) == coords[e][1]:
            if coords[e][2] == ".":
                return coords[e]
        if portalcoord[0] == coords[e][1] and (portalcoord[1]+1) == coords[e][1]:
            if coords[e][2] == ".":
                return coords[e]
        e+=1

def findlengthcrossroads():
    global coords
    global crossroads
    global portals
    global steps
    global pastcoords
    global paststeps
    global portallength
    global pastportalcoords
    for e in coords:
        if e[2] == "@":
            f = 0
            while f < len(coords):
                if e[0] == coords[f][0] and e[1] == (coords[f][1]-1) and coords[f][2] == ".":                  
                    if coords[f] not in pastportalcoords:
                        pastcoords.append(e[:])
                        paststeps.append(steps)
                        portallength.append(walk(e[:], 0))
                        pastportalcoords.append(coords[f])
                        steps = 0
                        pastcoords.clear()
                        paststeps.clear()
                        pastportals.clear()
                if e[0] == coords[f][0] and e[1] == (coords[f][1]+1) and coords[f][2] == ".":
                    if coords[f] not in pastportalcoords:
                        pastcoords.append(e[:])
                        paststeps.append(steps)
                        portallength.append(walk(e[:], 0))
                        pastportalcoords.append(coords[f])
                        steps = 0
                        pastcoords.clear()
                        paststeps.clear()
                        pastportals.clear()
                if e[0] == (coords[f][0]-1) and e[1] == coords[f][1] and coords[f][2] == ".":
                    if coords[f] not in pastportalcoords:
                        pastcoords.append(e[:])
                        paststeps.append(steps)
                        portallength.append(walk(e[:], 0))
                        pastportalcoords.append(coords[f])
                        steps = 0
                        pastcoords.clear()
                        paststeps.clear()
                        pastportals.clear()
                if e[0] == (coords[f][0]+1) and e[1] == coords[f][1] and coords[f][2] == ".":
                    if coords[f] not in pastportalcoords:
                        pastcoords.append(e[:])
                        paststeps.append(steps)
                        portallength.append(walk(e[:], 0))
                        pastportalcoords.append(coords[f])
                        steps = 0
                        pastcoords.clear()
                        paststeps.clear()
                        pastportals.clear()
                    
                f+=1
                
    print(portallength)
                    
    
    
def walk(globalcrossroad=0, num=1):
    global coords
    global crossroads
    global portals
    global steps
    global pastcoords
    global paststeps
    global pastportals
    global portallength
    global startend
    global pastportalcoords
    global levelsdeep
    e = num
    print(pastcoords)
    print(paststeps)
    try:
        while e < len(pastcoords):
            if paststeps[e] >= 0:
                f = 0
                while f < len(coords):
                    if coords[f] not in pastcoords and coords[f] not in pastportals and coords[f] not in pastportalcoords:
                        if coords[f][0] == pastcoords[e][0] and (coords[f][1]-1) == pastcoords[e][1]:
                            if coords[f][2] == ".":
                                pastcoords.append(coords[f])
                                steps += 1
                                paststeps.append(steps)
                                f = len(coords)
                            elif coords[f][2] == "@":
                                pastportalcoords.append(pastcoords[e])
                                steps +=  1
                                temp = (globalcrossroad, coords[f], steps, levelsdeep)
                                levelsdeep = 0
                                return temp   
                            elif str(coords[f][2]).isalpha():
                                if coords[f][2] == "A" or coords[f][2] == "Z":
                                    print(coords[f])
                                    u = 0
                                    while u < len(coords):
                                        if coords[f][0] == coords[u][0] and coords[f][1] == (coords[u][1]-1):
                                            print(coords[u])
                                            if coords[u][2] == "A" or coords[u][2] == "Z":
                                                print(coords[f],coords[u])
                                                temp = (globalcrossroad, coords[f], steps)
                                                return temp
                                        u+=1
                                h=0
                                while h < len(portals):
                                    if coords[f][0] == portals[h][0] and coords[f][1] == portals[h][1]:
                                        temp = (portals[h][0], portals[h][1], portals[h][2])
                                        if (portals[h][0] > 5 and portals[h][0] < 120) and (portals[h][1] > 5 and portals[h][1] < 120):
                                            levelsdeep -= 1
                                        elif (portals[h][0] < 5 or portals[h][0] > 120) or (portals[h][1] < 5 or portals[h][1] > 120):
                                            levelsdeep += 1
                                        pastportals.append(coords[f])
                                        k=0
                                        while k < len(portals):
                                            if temp[0] != portals[k][0] or temp[1] != portals[k][1]:
                                                if temp[2] == portals[k][2]:
                                                    temp2 = (portals[k][0], portals[k][1], portals[k][2])
                                                    l=0
                                                    while l < len(coords):
                                                        if temp2[0] == coords[l][0] and temp2[1] == coords[l][1]:
                                                            pastportals.append(portals[h])
                                                            pastportals.append(portals[k])
                                                            pastcoords.append(coords[l][:])
                                                            
                                                            paststeps.append(steps)
                                                            l = len(coords)
                                                            k = len(portals)
                                                            h = len(portals)
                                                            f = len(coords)
                                                        l+=1
                                                        
                                            k+=1
                                    h+=1
                        elif coords[f][0] == pastcoords[e][0] and (coords[f][1]+1) == pastcoords[e][1]:
                            if coords[f][2] == ".":
                                pastcoords.append(coords[f])
                                steps += 1
                                paststeps.append(steps)
                                f = len(coords)
                            elif coords[f][2] == "@":
                                pastportalcoords.append(pastcoords[e])
                                steps +=  1
                                temp = (globalcrossroad, coords[f], steps, levelsdeep)
                                levelsdeep = 0
                                return temp
                            elif str(coords[f][2]).isalpha():
                                if coords[f][2] == "A" or coords[f][2] == "Z":
                                    print(coords[f])
                                    u = 0
                                    while u < len(coords):
                                        if coords[f][0] == coords[u][0] and coords[f][1] == (coords[u][1]+1):
                                            print(coords[u])
                                            if coords[u][2] == "A" or coords[u][2] == "Z":
                                                print(coords[f],coords[u])
                                                temp = (globalcrossroad, coords[f], steps)
                                                return temp
                                        u+=1
                                h=0
                                while h < len(portals):
                                    if coords[f][0] == portals[h][0] and coords[f][1] == portals[h][1]:
                                        temp = (portals[h][0], portals[h][1], portals[h][2])
                                        if (portals[h][0] > 5 and portals[h][0] < 120) and (portals[h][1] > 5 and portals[h][1] < 120):
                                            levelsdeep -= 1
                                        elif (portals[h][0] < 5 or portals[h][0] > 120) or (portals[h][1] < 5 or portals[h][1] > 120):
                                            levelsdeep += 1
                                        pastportals.append(coords[f])
                                        k=0
                                        while k < len(portals):
                                            if temp[0] != portals[k][0] or temp[1] != portals[k][1]:
                                                if temp[2] == portals[k][2]:
                                                    temp2 = (portals[k][0], portals[k][1], portals[k][2])
                                                    l=0
                                                    while l < len(coords):
                                                        if temp2[0] == coords[l][0] and temp2[1] == coords[l][1]:
                                                            #print(coords[l], 'b')
                                                            pastportals.append(portals[h])
                                                            pastportals.append(portals[k])
                                                            pastcoords.append(coords[l][:])
                                                            
                                                            paststeps.append(steps)
                                                            l = len(coords)
                                                            k = len(portals)
                                                            h = len(portals)
                                                            f = len(coords)
                                                        l+=1
                                                        
                                            k+=1
                                    h+=1
                        elif (coords[f][0]-1) == pastcoords[e][0] and coords[f][1] == pastcoords[e][1]:
                            if coords[f][2] == ".":
                                pastcoords.append(coords[f])
                                steps += 1
                                paststeps.append(steps)
                                f = len(coords)
                            elif coords[f][2] == "@":
                                pastportalcoords.append(pastcoords[e])
                                steps +=  1
                                temp = (globalcrossroad, coords[f], steps, levelsdeep)
                                levelsdeep = 0
                                return temp
                            elif str(coords[f][2]).isalpha():
                                if coords[f][2] == "A" or coords[f][2] == "Z":
                                    #print(coords[f])
                                    u = 0
                                    while u < len(coords):
                                        if coords[f][0] == (coords[u][0]-1) and coords[f][1] == coords[u][1]:
                                            #print(coords[u])
                                            if coords[u][2] == "A" or coords[u][2] == "Z":
                                                #print(coords[f],coords[u])
                                                temp = (globalcrossroad, coords[f], steps)
                                                return temp
                                        u+=1
                                h=0
                                while h < len(portals):
                                    if coords[f][0] == portals[h][0] and coords[f][1] == portals[h][1]:
                                        temp = (portals[h][0], portals[h][1], portals[h][2])
                                        if (portals[h][0] > 5 and portals[h][0] < 120) and (portals[h][1] > 5 and portals[h][1] < 120):
                                            levelsdeep -= 1
                                        elif (portals[h][0] < 5 or portals[h][0] > 120) or (portals[h][1] < 5 or portals[h][1] > 120):
                                            levelsdeep += 1
                                        pastportals.append(coords[f])
                                        k=0
                                        while k < len(portals):
                                            if temp[0] != portals[k][0] or temp[1] != portals[k][1]:
                                                if temp[2] == portals[k][2]:
                                                    temp2 = (portals[k][0], portals[k][1], portals[k][2])
                                                    l=0
                                                    while l < len(coords):
                                                        if temp2[0] == coords[l][0] and temp2[1] == coords[l][1]:
                                                            pastportals.append(portals[h])
                                                            pastportals.append(portals[k])
                                                            pastcoords.append(coords[l][:])
                                                            
                                                            paststeps.append(steps)
                                                            l = len(coords)
                                                            k = len(portals)
                                                            h = len(portals)
                                                            f = len(coords)
                                                        l+=1
                                                        
                                            k+=1
                                    h+=1
                        elif (coords[f][0]+1) == pastcoords[e][0] and coords[f][1] == pastcoords[e][1]:
                            if coords[f][2] == ".":
                                pastcoords.append(coords[f])
                                steps += 1
                                paststeps.append(steps)
                                f = len(coords)
                            elif coords[f][2] == "@":
                                pastportalcoords.append(pastcoords[e])
                                steps +=  1
                                temp = (globalcrossroad, coords[f], steps, levelsdeep)
                                levelsdeep = 0
                                return temp
                            elif str(coords[f][2]).isalpha():
                                if coords[f][2] == "A" or coords[f][2] == "Z":
                                    #print(coords[f])
                                    u = 0
                                    while u < len(coords):
                                        if coords[f][0] == (coords[u][0]+1) and coords[f][1] == coords[u][1]:
                                            #print(coords[u])
                                            if coords[u][2] == "A" or coords[u][2] == "Z":
                                                #print(coords[f], coords[u])
                                                temp = (globalcrossroad, coords[f], steps)
                                                return temp
                                        u+=1
                                h=0
                                while h < len(portals):
                                    if coords[f][0] == portals[h][0] and coords[f][1] == portals[h][1]:
                                        temp = (portals[h][0], portals[h][1], portals[h][2])
                                        if (portals[h][0] > 5 and portals[h][0] < 120) and (portals[h][1] > 5 and portals[h][1] < 120):
                                            levelsdeep -= 1
                                        elif (portals[h][0] < 5 or portals[h][0] > 120) or (portals[h][1] < 5 or portals[h][1] > 120):
                                            levelsdeep += 1
                                        pastportals.append(coords[f])
                                        k=0
                                        while k < len(portals):
                                            if temp[0] != portals[k][0] or temp[1] != portals[k][1]:
                                                if temp[2] == portals[k][2]:
                                                    temp2 = (portals[k][0], portals[k][1], portals[k][2])
                                                    l=0
                                                    while l < len(coords):
                                                        if temp2[0] == coords[l][0] and temp2[1] == coords[l][1]:
                                                            pastportals.append(portals[h])
                                                            pastportals.append(portals[k])
                                                            pastcoords.append(coords[l][:])
                                                            
                                                            paststeps.append(steps)
                                                            l = len(coords)
                                                            k = len(portals)
                                                            h = len(portals)
                                                            f = len(coords)
                                                        l+=1
                                                        
                                            k+=1
                                    h+=1
                    f+=1
            print(pastcoords[e])
            print('eh:',paststeps[e])

            e+=1
    except Exception as o:
        print(o)

                        

from time import sleep
levelsdeep = 0
steps = 0
startend = []
portallength = []
coords = []
crossroads = []
portals = []
pastcoords = []
paststeps = []
pastportals = []
pastportalcoords = []

makecoords()
makewalls()
makecrossroads()
makeportals()
visible()
findlengthcrossroads()

    

sleep(1000)
