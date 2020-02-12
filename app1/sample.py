"""
from rake_nltk import Rake

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
text = "Protect the burned person from further harm. If you can do so safely, make sure the person you're helping is not in contact with the source of the burn. For electrical burns, make sure the power source is off before you approach the burned person.Make certain that the person burned is breathing. If needed, begin rescue breathing if you know how.Remove jewelry, belts and other restrictive items, especially from around burned areas and the neck. Burned areas swell rapidly.Cover the area of the burn. Use a cool, moist bandage or a clean cloth.Don't immerse large severe burns in water. Doing so could cause a serious loss of body heat (hypothermia).Elevate the burned area. Raise the wound above heart level, if possible.Watch for signs of shock. Signs and symptoms include fainting, pale complexion or breathing in a notably shallow fashion"
print(r.extract_keywords_from_text(text))
for i in r.get_ranked_phrases() :
    print(i)
text1 = "Major burns near Amboli andheri we need fire brigade urgently many people are hurt"
print(r.extract_keywords_from_text(text1))
for i in r.get_ranked_phrases() :
    print(i)
"""
import speech_recognition as sr
import enchant

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source)
    print ('Done!')
d = enchant.Dict("en_US")
if (d.check(r.recognize_google(audio, language='en-IN')[0])) :
	print(r.recognize_google(audio, language='en-IN'))
else :
	print ("not in eng")
