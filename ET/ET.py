sccoare = 0

file = open('text.txt','r')
text = file.readlines()

for count in range( len(text)):
    if count % 2 == 0:

        word = input("次の単語を英訳せよ："+text[count])
        print(text[count+1])

        if word == text[count+1]:
            print("\nWell Done!!")
            sccoare += 1
        else:
            print("\nDon't Worry!!")
    else:
        print("\n答え："+text[count])

print('\n'+"="*150)    
print("スコア: "+str(sccoare)+"/"+str(len(text)/2))
