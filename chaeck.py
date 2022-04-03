import pyautogui as pg 
from time import sleep
import pyperclip as pc

sleep(1)
# a = pg.position()
# print(a)
# exit()
file = open("poppp.txt",'r')
words = file.read().split("\n")
file.close()
num = 1
for word in words:
    pg.click(297,318)
    pg.hotkey('ctrl','a')
    pg.hotkey('ctrl','x')
    pg.typewrite(word,0.1)
    pg.press('enter')
    sleep(1)
    # pg.click()
    pg.click("copy.png")

    a = pc.paste()
    file = open("popp.txt",'a')
    file.write(f"\t'{word}' : '{a}'\t\t# {num}\n")
    print(f"{num}. {word} = {a}")
    num += 1
    file.close()



# file = open("pop.txt",'r')
# data = file.read()
# file.close()

# data = data.replace("\n'","'***")

# file = open("popp.txt",'w')
# data = file.write(data)
# file.close()


# file = open("popp.txt",'r')
# data = file.read().split("\n")
# file.close()


# file = open("poppp.txt",'w')
# for line in data:
#     if("***" in line):
#         file.write(f"{line}\n")
# file.close()