
file = open ("words.txt","r")
textRead = file.read()
print(textRead)
file.close()

fileWrite = open ("words.txt","a")
print("保存する文字列\n")


while True:
    str = input()
    if str != "F":
        fileWrite.write(str+"\n")
    else:
        break
    
fileWrite.close()
