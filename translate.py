from googletrans import Translator, constants
from pprint import pprint


# init the Google API translator
translator = Translator()


word = "order"

# translate a spanish text to english text (by default)
translation = translator.translate(word,dest='hi')
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


