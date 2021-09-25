# -*- coding: utf-8 -*-
"""
Created on 9/25/2021

@author: Charles Wang
"""

import azure.cognitiveservices.speech as speechsdk
apiKey = ""

speech_config = speechsdk.SpeechConfig(subscription=apiKey,region="eastasia")
speech_config.speech_recognition_language = "en-US" # zh-TW for traditional Chinese
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Please say something...")

result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("speech recognized as: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("speech not recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("speech recognition cancelled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details)) 