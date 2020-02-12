# from rake_nltk import Rake
# #
# # r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
# # text = "Protect the burned person from further harm. If you can do so safely, make sure the person you're helping is not in contact with the source of the burn. For electrical burns, make sure the power source is off before you approach the burned person.Make certain that the person burned is breathing. If needed, begin rescue breathing if you know how.Remove jewelry, belts and other restrictive items, especially from around burned areas and the neck. Burned areas swell rapidly.Cover the area of the burn. Use a cool, moist bandage or a clean cloth.Don't immerse large severe burns in water. Doing so could cause a serious loss of body heat (hypothermia).Elevate the burned area. Raise the wound above heart level, if possible.Watch for signs of shock. Signs and symptoms include fainting, pale complexion or breathing in a notably s hallow fashion."
# # r.extract_keywords_from_text(text)
# # l = []
# # for i in r.get_ranked_phrases() :
# #     l.append(i)
# # print(l)
from textblob import TextBlob
import speech_recognition as sr
# import nltk
# from nltk.stem.porter import *
#
# r = sr.Recognizer()
# print("start")
# with sr.Microphone() as source:
#     audio = r.listen(source,phrase_time_limit=10)
#
# text = r.recognize_google(audio, language='gu-IN')
#
# word = TextBlob(text)
# f = word.translate(from_lang='gu-IN', to='en-IN')
# print(f, str(f))
#
# r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
# r.extract_keywords_from_text(str(f))
# l = []
# for i in r.get_ranked_phrases() :
#     l.append(i)
#
#     porterStemmer = PorterStemmer()
#     wordList = nltk.word_tokenize(i)
#
#     stemWords = [porterStemmer.stem(word) for word in wordList]
#
#     print(' '.join(stemWords))
# print(l)
# fire_maj = ['fire', "person", 'huge']
#
# fire_minor = ["fire", "person", "small"]
#
# accident = ["vehilce", "accident", "road", "family", "bridge", "hit", "fell", "drive"]
#
# collapse =["dizzi", "dizzy"]
#
# asthama = ["trouble breathing", "breathlesness"]
#
#
#
# bleeding = ["cut", "bleed", "accident", "accid", "limb"]
#
# heart_attack = ["heart attack", "chest pain", "sweat", "sweating"]
#
# shock = ["light pole", "current", "open wires", "electricity", "electric"]
#
# snake = ["snake bit", "leg", "snake bitten"]
#
# dog = ["dog"]
text = "make sure theyâ€™re in a safe, comfortable position. Preferably, this should be lying on one side with their head slightly raised and supported in case they vomit. Check to see if theyâ€™re breathing. If theyâ€™re not breathing, perform CPR loosen any constrictive clothing, such as a tie or scarf. Cover them with a blanket to keep them warm. Donâ€™t give them anything to eat or drink. Dont move them if they feel weakness in limbs. . Be prepared to tell the emergency operator about their symptoms and when they started. Be sure to mention if the person fell or hit their head."
word = TextBlob(text)
f = word.translate(from_lang='en-IN', to='hi-IN')
print(f, str(f))
#
# from django.shortcuts import render
# from django.contrib import auth
#
# import json
#
# import pyrebase
#
#
# config = {
# 	'apiKey': "AIzaSyB6s7DSe9M6MZk7g77cMTuoqIO6d-ebKwI",
#     'authDomain' : "garbage-truck-monitoring.firebaseapp.com",
#     'databaseURL' : "https://garbage-truck-monitoring.firebaseio.com",
#     'projectId' : "garbage-truck-monitoring",
#     'storageBucket' : "garbage-truck-monitoring.appspot.com",
#     'messagingSenderId' : "549306067582",
#     'appId' : "1:549306067582:web:bbaeac9ec829045099c62f",
#     'measurementId' : "G-X9JCRW3TR0"
# }
# firebase = pyrebase.initialize_app(config)
#
#
# db = firebase.database()
# bin = db.child("Bin").get().val()
# lat, lon, cap = [], [], []
# cap_70, cap_20, cap_20_70 = [],[],[]
# print(bin)
# for i in bin:
#     height = (int(db.child("Bin").child(i).child("height").get().val()))
#     lati = (float(db.child("Bin").child(i).child("latitude").get().val()))
#     long = (float(db.child("Bin").child(i).child("longitude").get().val()))
#
#
#     var = db.child("BinPerLevel").child('19-312251|72-8513579').child("2020-01-12").get().val()
#     print(next(reversed(var)))
#     height2 = db.child("BinPerLevel").child('19-312251|72-8513579').child("2020-01-12").child(next(reversed(var))).child(
#         "height").get().val()

from textblob import TextBlob
import speech_recognition as sr

r = sr.Recognizer()
print("start")
with sr.Microphone() as source:
    audio = r.listen(source, phrase_time_limit=10)

lang = 'hi-IN'
text = sr.recognize_google(audio, language=lang)
print(text)
word = TextBlob(text)
f = word.translate(from_lang=lang, to='en-IN')
