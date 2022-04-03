from englisttohindi.englisttohindi import EngtoHindi


file = open('words.txt','r')
data = file.read().split()
file.close()

for word in data:
    file = open("translate.txt",'a')
    trans = EngtoHindi(message=word)
    trans = trans.convert
    file.write(f"{word} : {trans}\n")
    file.close()
