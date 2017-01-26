
todo1 = input("what do you do now? : ")
print ('      thanks',todo1,' I will do that')
with open('asciiart/dragon1') as dragon:
    for line in dragon:
        print (line, end='')
