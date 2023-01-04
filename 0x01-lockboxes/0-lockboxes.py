#!/usr/bin/python3
"""unlocks alot"""

def canUnlockAll(boxes):
    """unlock boxes"""
    x = True
    unlist = [boxes[0].copy()]
    if len(boxes) >= 2 and len(boxes[0]) == 0:
        return False
    while x is True:
        temp = []
        status = []
        for i in unlist[-1]:
            if i >= len(boxes):
                continue
            if 'u' not in boxes[i]:
                temp += boxes[i]
                boxes[i].append('u')
                status.append(0)
            else:
                status.append(1)
        if 0 not in status:
            x = False
        else:
            unlist.append(temp)
    flist = sum(unlist,[])
    y = True
    for i in range(1,len(boxes)):
        if i not in flist:
                y = False
                break
    return(y)

