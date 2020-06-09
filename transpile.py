lineCount = 0
quoteCount = 0
finalFile = ''
crumbFile = open('main.yaml', 'r')
for line in crumbFile.readlines():
    newLine = line.replace(':', '(')
    if newLine != line:
        lineCount += 1
    for i in newLine:
        if i == "'" or i == '"':
            quoteCount += 1
    if quoteCount == 2:
        newLine = newLine.replace('\n', ',\n')
    quoteCount = 0
    finalFile += newLine

for i in range(lineCount-1):
    finalFile += '),'

crumbFile.close()
finalFile += ')'

print(finalFile)

builder = open('builder.js', 'w')

builder.writelines(finalFile)

builder.close()