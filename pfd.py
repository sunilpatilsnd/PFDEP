#!/usr/bin/env python


#reading the file
filename = 'input.txt'
file = open(filename, "r")

task, rule = file.readline().split()
print task, rule

#converting the data type of the input to integers
task = int(task)
rule = int(rule)
idegree = {}
for i in range(1, task + 1):
    idegree[i] = 0
    #print idegree
itask = {}
while rule:
    rule -= 1
    tmpLst = map(int, file.readline().split())
    #print tmpLst
    idegree[tmpLst[0]] = tmpLst[1]
    for i in range(2, len(tmpLst)):
        if tmpLst[i] not in itask:
            itask[tmpLst[i]] = [tmpLst[0]]
        else:
            itask[tmpLst[i]].append(tmpLst[0])
#print itask
#print idegree
queue = []
while True:
    for i in range(1, task + 1):
        if i in idegree and idegree[i] == 0:
            queue.append(i)
            if i in itask:
                for j in itask[i]:
                    idegree[j] -= 1
            del idegree[i]
            break
    if len(queue) == task:
        break
for i in queue:
    print i,

file.close()