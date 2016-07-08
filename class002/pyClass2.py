#coding:utf-8

import json ,help

book = 'string.txt'
date = 'stringJson.txt'


with open(book, "r") as ins:
    array = []
    for line in ins:
        array.append(line)


with open(date, 'w') as f:
    json.dump(array, f)


lines = []
with open(book) as f:
    lines = [line.rstrip('\n') for line in open(book)]

# print(lines)
textArray = []
for stingInTxt in lines:
    text = stingInTxt.split(' ')   # All str array
    textArray.append(text)
# print(textArray)

resultAcciArray = []

goodAcci = []
for newArray in  textArray:
    newacci = []
    for newStr in newArray:
        if newStr == "space":
            newStr = " "

        newStrAssci = help.convert_to_ascii(newStr) #转换
        newacci.append(newStrAssci)

# 补全 -1
    while len(newacci)<18:
        newacci.append('-1')

    goodAcci.append(newacci)


for abc123 in goodAcci:
    for cba321 in abc123:
        resultAcciArray.append(cba321)


with open(date, 'w') as f:
    json.dump(resultAcciArray, f)



