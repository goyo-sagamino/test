while True:

	print("単語帳の登録：w\n")
	print("単語帳の新規作成：nw\n")
	print("タイピング：p\n")
	print("終了：f\n")
	print("_"*80)

	mode = input("モードを選択")

#____________________________________________________________________モード選択_________________________________________________________________________________


	if mode == "p":
	    
	    point = 0

	    fileName = input("単語帳の名前を入力")
	    file = open(fileName+".txt","r")
	    
	    text = file.read()

	    text = text.splitlines()

	    for count in range(len(text)):

	        if count % 2 == 0:

	            print("次の語句を英訳せよ："+ text[count]+"\n")
	            ans = input()

	            if ans == text[count+1]:
	                print ("well Done!!"+"\n")
	                point += 1

	            else:
                        print("don't worry"+"\n")

	        else:
                        print("answer:"+text[count])
                        print("_"*80 + "\n")

	    print("得点："+str(point)+"/"+str(len(text)/2))

	    file.close()

#_____________________________________________________________________単語練習______________________________________________________________________________________


	elif mode == "w":
	    fileName = input("単語帳の名前を入力")
	    file = open(fileName+".txt","a")

	    while True:

	        print("保存する単語\n")
	        
	        strJa = input("日本語")
	        strEn = input("英語")
	        print("")

	        if strJa != "F" and strEn != "F": 
	        
	            file.write(strJa+"\n")
	            file.write(strEn+"\n")


	        else:
                        print("_"*80)
                        break

	    file.close()

#___________________________________________________________________単語帳の更新______________________________________________________________________________________________
	  
	    
	elif mode == "nw":
                fileName = input("単語帳の名前を入力")
                file = open(fileName+".txt","w+")

                while True:

                        print("保存する単語\n")
                        
                        strJa = input("日本語")
                        strEn = input("英語")
                        print("")

                        if strJa != "F" and strEn != "F": 
                        
                            file.write(strJa+"\n")
                            file.write(strEn+"\n")


                        else:
                                print("_"*80)
                                break

                file.close()
	    
#____________________________________________________________________新規作成_________________________________________________________________________________________
                
	    
	elif mode == "f":
		break
		
	else:
                print("Error:許可されていないキーです。\n")
                print("_"*80)

#___________________________________________________________________例外処理____________________________________________________________________________________________________

