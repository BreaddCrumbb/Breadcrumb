colonCount = 0
finaldoc = ''
tabsList = []
crumbFile = open('main.yaml', 'r')
for line in crumbFile.readlines():
    spaceCount = 0
    tabCount = 0
    for i in line:
        if i == ' ':
            spaceCount += 1
    if ':' in line:
        colonCount +=1
        newLine = line.replace(':', '(')

    tabCount = spaceCount/4
    tabCount = int(tabCount)
    for i in tabsList:
        if tabsList[i] <= tabCount:
            newLine += '\n),'
            tabsList.pop(i)
    finaldoc += newLine
    tabsList.append(tabCount)

crumbFile.close()



builder = open('builder.js', 'w')

# builder.writelines(finalFile)

builder.close()