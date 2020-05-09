from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
from django.views.decorators.csrf import csrf_exempt
from speech_recognition import Microphone
from textblob import TextBlob
import speech_recognition as sr
import pyrebase
from django.contrib import auth
import nltk
from nltk.stem.lancaster import LancasterStemmer
from aurnag import settings
from django.core.mail import send_mail
stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow
import random
import json
import speech_recognition as sr

r = sr.Recognizer()
import pyrebase
from django.core.mail import send_mail
import pickle
x,y = 0,0







with open("intents.json") as file :
    data = json.load(file)
try:
    with open("./data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))
    print(words)
    labels = sorted(labels)









    training, output = [], []
    out_empty = [0 for _ in range(len(labels))]
    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [stemmer.stem(w.lower()) for w in doc]
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1
        training.append(bag)
        output.append(output_row)
    training = numpy.array(training)
    output = numpy.array(output)
    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)
tensorflow.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)
model = tflearn.DNN(net)
try:
    model.load("model.tflearn")
except:
    model = tflearn.DNN(net)
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")












def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            print(se, w)
    for i in range(len(words)) :
        print(bag[i], words[i])
    return numpy.array(bag)














config = {
    'apiKey': "AIzaSyC4cTT6pMJEgRJkFppofg2mTT7OB9j1M7U",
    'authDomain': "suraksha3630.firebaseapp.com",
    'databaseURL': "https://suraksha3630.firebaseio.com",
    'projectId': "suraksha3630",
    'storageBucket': "suraksha3630.appspot.com",
    'messagingSenderId': "307276178334",
    'appId': "1:307276178334:web:9f54433327e01a49c3ec8f",
    'measurementId': "G-3BGDJT7PME"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
db  =firebase.database()

def signIn(request):
    if "uid" not in request.session.keys():
        request.session['uid'] = None
        request.session['email'] = None
    # print(request.session['uid'])
    if request.session['uid'] != None:

        currentuserrid = request.session['email']
        print("Email ", currentuserrid)
        users = db.child('users').get().val()
        print(users)
        list2 = []
        for i in users:
            if currentuserrid == str(db.child('users').child(i).child('email').get().val()):
                pincode = db.child('users').child(i).child('pincode').get().val()
                print("Pincode")
                feeds = database.child('Feeds').get().val()
                print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                print(feeds)
                if feeds:
                    for i in feeds:
                        print(i)
                        print(str(database.child('Feeds').child(i).child('pincode').get().val()))
                        print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                        if str(database.child('Feeds').child(i).child('pincode').get().val()) == str(400058) :
                            print("jjjjjjj")
                            id = database.child('Feeds').child(i).child('VictimId').get().val()
                            print("WWWWWWWWWWWWWWWWWWWWWWWW")
                            print(id)
                            #print(database.child('users').child(id).child('name').get().val())
                            print("4444444")
                            list2.append({
                                "VictimName": database.child('users').child(id).child('name').get().val(),
                                "HospitalCalled": database.child('Feeds').child(i).child('HospitalCalled').get().val(),
                                "Pincode": database.child('Feeds').child(i).child('pincode').get().val()
                            })
                    print(list2)
                    break

        return render(request, "welcome.html", {"e": request.session['email'], 'feeds': list2})
    return render(request, "signIn.html")


def postsign(request):
    for key, value in request.POST.items():
        print('{} => {}'.format(key, value))
    if "uid" not in request.session.keys():
        request.session['uid'] = None
    if request.session['uid'] == None:
        if request.POST.get('email') == None or request.POST.get("pass1") == None:
            return redirect('http://127.0.0.1:8000/')
        request.session['email'] = request.POST.get('email')
        email = request.POST.get('email')
        passw = request.POST.get("pass1")
        print(email)
        print(passw)
        try:
            user = authe.sign_in_with_email_and_password(email, passw)
            session_id = user['idToken']
            request.session['uid'] = session_id
            request.session['email'] = email
            return render(request, "welcome.html", {"e": request.session['email']})
        except:
            message = "Please check your emailID / Password"
            return render(request, "signIn.html", {"msg": message})
    else:
        print("****************************************")
        currentuserrid = request.session['email']
        print("Email ", currentuserrid)
        users = db.child('users').get().val()
        print(users)
        list2 = []
        for i in users:

            if currentuserrid == str(db.child('users').child(i).child('email').get().val()):
                pincode = db.child('users').child(i).child('pincode').get().val()
                print("Pincode", pincode)
                feeds = database.child('Feeds').get().val()
                print(feeds)
                print("rrrrrrrrrrrrrrrrr")
                if feeds:
                    for i in feeds:
                        if str(database.child('Feeds').child(i).child('pincode').get().val()) == pincode:
                            id = database.child('Feeds').child(i).child('VictimId').get().val()
                            list2.append({
                                "VictimName": database.child('users').child(id).child('name').get().val(),
                                "HospitalCalled": database.child('Feeds').child(i).child('HospitalCalled').get().val(),
                                "Pincode": database.child('Feeds').child(i).child('pincode').get().val()
                            })
                    print(list2)
        return render(request, "welcome.html", {"e": request.session['email'], 'feeds': list2})


def logout(request):
    if "uid" in request.session.keys():
        print(request.session['uid'])
        if request.session['uid'] != None:
            request.session['uid'] = None
            request.session['email'] = None
            # request.session['uid']=None
        else:
            message = "user is not logged in"
            return render(request, "signin.html", {"msg": message})
        auth.logout(request)
    return render(request, 'signin.html')


def signUp(request):
    return render(request, "signup.html")


def postsignup(request):
    name = request.POST.get('name')
    bloodgrp = request.POST.get('bloodgrp')
    birthdate = request.POST.get('birthday')
    healthissue = request.POST.get('healthissue') if request.POST.get('healthissue') else "None"

    emergencycontactname = request.POST.get('ename')
    emergencycontactno = request.POST.get('emobileno')
    emergencyemail = request.POST.get('emergencyemail')
    mobileno = request.POST.get('mobileno')

    email = request.POST.get('email')
    passw = request.POST.get('password')
    language = request.POST.get('language')
    address = request.POST.get('address')
    print(name)
    print(email)
    print(passw)
    try:
        user = authe.create_user_with_email_and_password(email, passw)
        print("123")
        print(user)
        uid = user['localId']
        data = {"name": name, "email": email, "bloodgrp": bloodgrp,
                "mobileno": mobileno,
                "language": language,
                "birthdate": birthdate, "healthissue": healthissue,
                "emergencycontactname": emergencycontactname,
                "emegencycontactno": emergencycontactno,
                "emergencyemail": emergencyemail,
                "address": address,
                }
        print("456")
        database.child("users/" + uid).set(data)
    except:
        message = "Invalid Credentials"
        return render(request, "signup.html", {"messg": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    request.session['email'] = email
    return render(request, "signIn.html")

def first_aid(request,input):
    results = model.predict([bag_of_words(input, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']

    print(responses)
    db = firebase.database()
    userss = db.child("users").get().val()
    usermail = request.session['email']
    lang = ""
    for i in userss:
        mail = db.child("users").child(i).child("email").get().val()
        if mail == usermail:
            lang = db.child("users").child(i).child("language").get().val()
            print(lang)
            break

    word = TextBlob(responses[0])
    f = word.translate(from_lang='en-IN', to=lang)
    f = (str(f))

    return render(request, 'home.html', {"text": responses[0], "textlang": str(f)})

    

def audio(request):
    with sr.Microphone() as source:
        print('Say Something:')
        audio = r.listen(source, phrase_time_limit=5)
        print(audio)
        print('Done!')
    db = firebase.database()
    userss = db.child("users").get().val()
    usermail = request.session['email']
    lang = ""
    for i in userss:
        mail = db.child("users").child(i).child("email").get().val()
        if mail == usermail:
            lang = db.child("users").child(i).child("language").get().val()
            print(lang)
    try:
        text = r.recognize_google(audio, language=lang)
    except:
        return render(request, 'type.html',{"message":'Sorry We could not get your audio'})
        
    wordzz = TextBlob(text)
    if lang != "en-IN":
        f = wordzz.translate(from_lang=lang, to='en-IN')
    else:
        f = wordzz
    print("************************************")
    print(str(f))
    inp = str(f)
    return first_aid(request,inp)
    # results = model.predict([bag_of_words(inp, words)])
    # results_index = numpy.argmax(results)
    # tag = labels[results_index]
    # for tg in data["intents"]:
    #     if tg['tag'] == tag:
    #         responses = tg['responses']
    # word = TextBlob(responses[0])
    # if lang != "en-IN":
    #     f = word.translate(from_lang="en-IN", to=lang)
    # else:
    #     f = word
    # # f = "HI"
    # # print(str(f))


    # return render(request, 'home.html', {"text": responses[0], "textlang": str(f)})


def text1(request):
    if request.method == "POST":
        text = request.POST.get("textinput1")
        inp = str(text)
        return first_aid(request,inp)
        # results = model.predict([bag_of_words(inp, words)])
        # results_index = numpy.argmax(results)
        # tag = labels[results_index]
        # for tg in data["intents"]:
        #     if tg['tag'] == tag:
        #         responses = tg['responses']

        # print(responses)
        # db = firebase.database()
        # userss = db.child("users").get().val()
        # usermail = request.session['email']
        # lang = ""
        # for i in userss:
        #     mail = db.child("users").child(i).child("email").get().val()
        #     if mail == usermail:
        #         lang = db.child("users").child(i).child("language").get().val()
        #         print(lang)
        #         break

        # word = TextBlob(responses[0])
        # f = word.translate(from_lang='en-IN', to=lang)
        # f = (str(f))

        # return render(request, 'home.html', {"text": responses[0], "textlang": f})


def text2(request):
    if request.method == "POST":
        l = []
        # from django.views.decorators.csrf import csrf_exempt
        # @csrf_exempt
        # def radio(request):
        #if request.method == "POST":
        val = request.POST["radiobutton"]
        print(val)
        val2 = request.POST["radiobutton2"]
        print(val2)
        if val2 == "Fire":
            l = val2
        else:
            # l = val +" "+ val2
            l= val2
        print(l)
        return first_aid(request,l)
        ###################################################### SAME for text1  and text2
        # results = model.predict([bag_of_words(l, words)])
        # results_index = numpy.argmax(results)
        # tag = labels[results_index]

        # for tg in data["intents"]:
        #     if tg['tag'] == tag:
        #         responses = tg['responses']
        # db = firebase.database()
        # userss = db.child("users").get().val()
        # usermail = request.session['email']
        # lang = ""
        # for i in userss:
        #     mail = db.child("users").child(i).child("email").get().val()
        #     if mail == usermail:
        #         lang = db.child("users").child(i).child("language").get().val()
        #         print(lang)
        #         break

        # word = TextBlob(responses[0])
        # # print(word)
        # f = word.translate(from_lang='en-IN', to=lang)
        # f = (str(f))
        # # f = "HI"
        
        # return render(request, 'home.html', {"text": responses[0], "textlang": str(f)})



# useremail = request.session['email']
#                     users = db.child('users').get().val()
#                     for i in users :
#                         receivers_mail = db.child("users").child(i).child("email").get().val()
#                         if receivers_mail == useremail :




#                             receiverlist = db.child("users").child(i).child("emergencyemail").get().val()
#                             send_mail( subject, Address, email_from, receiverlist, fail_silently=False )
#                     break

import reverse_geocoder as rg
def notify_emergencycontact(request) :
    print("Hello from latlongi")
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    coordinates = (latitude,longitude)
    if request.method == "POST":
        currentuserrid = request.session['email']
        print(currentuserrid)
        databaseuser = db.child('users').get().val()
        for l in databaseuser:
            if str(db.child('users').child(l).child('email').get().val()) == currentuserrid:
                emergencyemail = db.child('users').child(l).child('emergencyemail').get().val()
                nameofuser = db.child('users').child(l).child('name').get().val()
                print (rg.search(coordinates))
                result = rg.search(coordinates)
                t = ""
                addr = result[0]
                for add in addr.items() :
                    t += str(add[1]) + " "
                Address = str(db.child('users').child(l).child('name').get().val()) + " is not feeling comfortable at location :" + t + " Please look after them"
                print(Address)
                email_from = settings.EMAIL_HOST_USER
                subject = str(db.child('users').child(l).child('name').get().val()) + " is in an Emergency!!!"
                recipient_list = []
                recipient_list.append(emergencyemail)
                send_mail(subject, Address, email_from, recipient_list, fail_silently=False)
                print("Message Sent")
                break
    return render(request,'welcome.html',{"e": request.session['email']})
@csrf_exempt
def latlongi(request):
    print("Hello from latlongi")
    print(request.method)
       
    if request.method == "GET":
        print(request)
        print("555555555555555555555555555555555")

        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        print("ddddddddddddddddddddddddddd")
        print(latitude)
        print(longitude)
        print("Hello from latlongi", latitude, longitude)
        # CODE TO BE ADDED
        # from geopy.geocoders import GoogleV3

        # geolocator = GoogleV3(api_key='')
        # latlong = latitude + ',' + longitude
        # locations = geolocator.reverse(latlong)
        # if locations:

        #     i = locations[0].address.rfind(',')
        #     print( " sdfghgf", locations[0].address)
        #     print(locations[0].address[i - 6:i])
        #     pincode = str(locations[0].address[i - 6:i])


        #Temporory lets consider pincode to be
        pincode='400058'

        currentuserrid = request.session['email']


        hospitaltype = "Maternity"
        data = db.child('Pincode').child(pincode).get().val()


        k = 0
        databaseuser = db.child('users').get().val()
        for i in data:
            print(i)
            hospitalname=i
            hospital = str(db.child('Pincode').child(pincode).child(i).child('type').get().val()).split(',')
            print(hospital)
            for j in hospital:
                print("From j", j)
                if j == hospitaltype:
                    print("Hospital Mil-Gaya")
                    k = 1

                    for l in databaseuser:
                        userid=l
                        if str(db.child('users').child(l).child('email').get().val()) == currentuserrid:
                            hospitalemail = str(db.child('Pincode').child(pincode).child(i).child('email').get().val())
                            emargencyemail = db.child('users').child(l).child('emergencyemail').get().val()

                            CurrentAddress = "Rahul Soni 123."
                            print(l)
                            Address = str(db.child('users').child(l).child(
                                'name').get().val()) + " is not feeling comfortable. Please look after him ASAP."
                            print(Address)
                            email_from = settings.EMAIL_HOST_USER
                            subject = "Emergency Found"
                            recipient_list = []
                            recipient_list.append(hospitalemail)
                            recipient_list.append(emargencyemail)
                            #send_mail(subject, Address, email_from, recipient_list, fail_silently=False)
                            print("Message Sent")
                            break

                    # send email to hospital

                    break

            if k == 1:
                break
        if k == 0:
            databaseuser = db.child('users').get().val()
            for i in data:
                for j in databaseuser:
                    userid=j
                    if db.child('users').child(j).child('email').get().val() == currentuserrid:
                        print(i)
                        print("Hospital Nahi mila ")
                        print(db.child('Pincode').child(pincode).child(i).child('email').get().val())
                        print(db.child('Pincode').child(pincode).child(i).child('contactno').get().val())
                        hospitalemail = str(db.child('Pincode').child(pincode).child(i).child('email').get().val())
                        emargencyemail = db.child('users').child(j).child('emergencyemail').get().val()
                        print("Hospital Email ", hospitalemail)
                        print("Emergency Email ",emargencyemail)
                        CurrentAddress = "Rahul Soni 123."
                        print(db.child('users').child(j).child('name').get().val())
                        Address = db.child('users').child(j).child('name').get().val() +  "is not feeling comfortable. Please look after him ASAP."

                        email_from = settings.EMAIL_HOST_USER
                        subject = "Emergency Found"
                        recipient_list = []
                        recipient_list.append(hospitalemail)
                        recipient_list.append(emargencyemail)
                        # hospital =str(db.child(pincode).child(i).child('type').get().val()).split(',')
                        #send_mail(subject, Address, email_from, recipient_list, fail_silently=False)
                        break

                break

        #users = db.child('users').child('7g6ZdpFJDIbUwBk2S7NbkaPDh9o2')

        feeddata = {
                "VictimId":userid,
                "pincode":pincode,
                "HospitalCalled":hospitalname
        }

        p = db.child('Feeds').push(feeddata)

        # print(users)
        # print(db.child('users').child('7g6ZdpFJDIbUwBk2S7NbkaPDh9o2').child('emergencycontactname').get().val())
        # print(db.child('users').child('7g6ZdpFJDIbUwBk2S7NbkaPDh9o2').child('emergencycontactname').get().val())

        print("Message Sent To ")
    else:
        print("nnnnnnnnnnnnnnnnnnnnnnnnpooooooooooooooooooo")
    return HttpResponse("DOne")


def get_latlong(request):
    bin = db.child("Bin").get().val()
    lat, lon, cap = [], [], []
    cap_70, cap_20, cap_20_70 = [], [], []
    print(bin)
    
    for i in bin:
        height = (int(db.child("Bin").child(i).child("height").get().val()))
        lati = (float(db.child("Bin").child(i).child("latitude").get().val()))
        long = (float(db.child("Bin").child(i).child("longitude").get().val()))

        var = db.child("BinPerLevel").child('19-312251|72-8513579').child("2020-01-12").get().val()
        print(next(reversed(var)))
        height2 = db.child("BinPerLevel").child('19-312251|72-8513579').child("2020-01-12").child(
            next(reversed(var))).child(
            "height").get().val()

        # for i in var :
        #     print(i)
        # from datetime import date, datetime
        # today = date.today()
        # now = datetime.now()
        # dt_string = now.strftime("%H:%M")
        # height2 = (int(db.child("BinPerLevel").child(data).child("height").get().val()))
        perc = (int(height2) /int(height)) * 100
        if perc >= 70:
            cap_70.append([lati, long])
        elif perc <= 20:
            cap_20.append([lati, long])
        else:
            cap_20_70.append([lati, long])
    cap_20 = json.dumps(cap_20)
    cap_20_70 = json.dumps(cap_20_70)
    cap_70 = json.dumps(cap_70)
    print(cap_20,cap_20_70,cap_70)
    return render(request,'latlong.html')
#    return render(request,'latlong.html',{"cap_20":cap_20,"cap_70":cap_70,"cap_20_70":cap_20_70})
def type(request):

    return render(request, "type.html",{"message":''})
"""

"""