# -*- coding: utf-8 -*-
"""
Created on 9/25/2021

@author: Charles Wang
"""

#!pip install SpeechRecognition
#!pip install pyaudio

import http.client,urllib.parse,json
from xml.etree import ElementTree
import wave
from IPython.display import Audio
import speech_recognition as sr

apiKey = ""
params = ""
headers = {"Ocp-Apim-Subscription-Key":apiKey}
AccessTokenURL = "https://eastasia.api.cognitive.microsoft.com/sts/v1.0/issuetoken";
AccessTokenHost = "eastasia.api.cognitive.microsoft.com" 
path = "/sts/v1.0/issueToken" 

print ("Connect to server to get the Access Token")
conn = http.client.HTTPSConnection(AccessTokenHost) 
conn.request("POST", path, params, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
conn.close()

accesstoken = data.decode("UTF-8")
body = ElementTree.Element('speak', version='1.0')
body.set('{http://www.w3.org/XML/1998/namespace}lang','zh-TW')

voice = ElementTree.SubElement(body, 'voice')
voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'zh-TW')
voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Female')
'''
ref: https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#neural-voices
voice options:

en-US-GuyNeural
en-US-EricNeural
en-US-BrandonNeural
en-US-ChristopherNeural
en-US-JacobNeural
en-GB-RyanNeural (uk)
en-IN-PrabhatNeural (india)
en-SG-WayneNeural (singapore)
'''
voice.set('name', 'en-SG-WayneNeural')
voice.text = ""

headers = {
    "Content-type": "application/ssml+xml",
    "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
    "Authorization": "Bearer " + accesstoken,
    "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA",
    "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960",
    "User-Agent":"225"
}

print ( "\nConnect to server to synthesize the wave" )
conn = http.client.HTTPSConnection("eastasia.tts.speech.microsoft.com")
conn.request("POST", "/cognitiveservices/v1", ElementTree.tostring(body), headers)
response = conn.getresponse()
print (response.status, response.reason)

data = response.read()
conn.close()
print ( "The synthesized wave length: %d" %(len(data)))

f_write = wave.open("output.wav", "wb")
f_write.setnchannels(1)
f_write.setframerate(24500)
f_write.setsampwidth(2)
f_write.writeframes(data)
f_write.close()

sound_file = './output.wav'
Audio(sound_file, autoplay=True)