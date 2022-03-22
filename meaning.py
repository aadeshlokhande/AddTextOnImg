from PyDictionary import PyDictionary
# from textblob import TextBlob
dict = PyDictionary()

file = open("word.txt",'r')
words = file.read().split('\n')
file.close()

for word in words: 
    # dictionary=PyDictionary()
    # word = str(TextBlob(word).correct())
    # mean = dictionary.meaning(word)
    # ac, vc, nc = 1,1,1

    # full_sentense = ""

    # if str(dictionary.meaning(word))!="None":
    #     try:
    #         full_sentense = full_sentense + "Noun : "
    #         for noun in mean["Noun"]:
    #             full_sentense = full_sentense + "\n"+ str(nc)+") "+noun
    #             nc = nc + 1
    #         full_sentense = full_sentense + "\n"
    #     except:
    #         full_sentense = full_sentense + "N\\A\n"
    #     try:
    #         full_sentense = full_sentense + "\n"+ "Adjective : "
    #         for ad in mean["Adjective"]:
    #             full_sentense = full_sentense + "\n"+ str(ac)+") "+ad
    #             ac = ac + 1
    #         full_sentense = full_sentense + "\n"
    #     except:
    #         full_sentense = full_sentense + "N\\A\n"
    #     try:
    #         full_sentense = full_sentense + "\n"+ "Verb : "
    #         for verb in mean["Verb"]:
    #             full_sentense = full_sentense + "\n"+ str(vc)+") "+verb
    #             vc = vc + 1
    #         full_sentense = full_sentense + "\n"
    #     except:
    #         full_sentense = full_sentense + "N\\A\n"
    #     meaing = f"Word : {word.upper()}\n\n{full_sentense}"
    # else:
    #     # meaning = f"\"{word}\" \nWord not Found"
    #     pass

    # file = open("meaning.txt",'a')
    # file.write(meaing)
    # file.close()






    file = open("meaning.txt",'a')
    file.write(f"{word} : \n")
    try:
        meaning = dict.meaning(word)
        mean = meaning['Noun']
        for i in range(len(mean)):
            file.write(f"{i+1}) {mean[i]}\n")
        file.write("\n")  
    except:
        pass 

    file.close()    

