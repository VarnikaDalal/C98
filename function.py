def wordCount():
    fileName=input("Enter file name:")
    wordCount=0
    file=open(fileName)
    for i in file:
        word=i.split()
        wordCount=wordCount+len(word)
    print("Number of words: ")
    print(wordCount)

wordCount()