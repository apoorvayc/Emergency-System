
# # import speech_recognition as sr
# #
# # r = sr.Recognizer()
# # print("start")
# # with sr.Microphone() as source:
# #     audio = r.listen(source, phrase_time_limit=10)
# #
# # lang = 'en-IN'
# # text = sr.recognize_google(audio, language=lang)
# # print(text)
# # # word = TextBlob(text)
# # # f = word.translate(from_lang=lang, to='en-IN')
# # # print(str(f))
# #
# #
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source,phrase_time_limit=10)
    print('Done!')

text = r.recognize_google(audio, language='mr-IN')


print(text)
word = TextBlob(text)
f = word.translate(from_lang='mr-In', to='en-IN')
print(str(f))
#
# print(r.recognize_google(audio))
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

# def getLocation():
#     options = Options()
#     options.add_argument("--use-fake-ui-for-media-stream")
#     timeout = 20
#     driver = webdriver.Chrome(executable_path = 'chromedriver.exe', chrome_options=options)
#     driver.get("https://mycurrentlocation.net/")
#     wait = WebDriverWait(driver, timeout)
#     time.sleep(3)
#     longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
#     longitude = [x.text for x in longitude]
#     longitude = str(longitude[0])
#     latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
#     latitude = [x.text for x in latitude]
#     latitude = str(latitude[0])
#     driver.quit()
#     return (latitude,longitude)
# print(getLocation())