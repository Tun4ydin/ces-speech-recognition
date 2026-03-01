import speech_recognition as sr
import subprocess
import os
import time

insta_image = "/ces/insta_image.jpeg"
x_image = "/ces/x_image.jpeg"
linkedin_image = "/ces/linkedin_image.jpeg"
whatsapp_image = "/ces/whatsapp_image.jpeg"

def close_picture():
    os.system("pkill Preview")

recog = sr.Recognizer()
recog.energy_threshold = 200
recog.dynamic_energy_threshold = True


import os

def open_image(path):
    absolute_path = os.path.abspath(path)
    if os.path.exists(absolute_path):
        os.system("pkill Preview")
        time.sleep(0.5)
        subprocess.Popen(["open", absolute_path])
    else:
        print(f"Error: File not found at {absolute_path}")

with sr.Microphone() as source:
        recog.adjust_for_ambient_noise(source)
        while True:

            try:
                print("dinleniyor. ")
                audio = recog.listen(source)

                text = text = recog.recognize_google(audio).lower()
                print(text)

                if "instagram" in text or "insta" in text:
                    open_image(insta_image)

                elif "x" in text or "twitter" in text or "ex" in text:
                    open_image(x_image)
        
                elif "linkedin" in text or "lincol" in text:
                    open_image(linkedin_image)

                
                elif "whatsapp" in text:
                    open_image(whatsapp_image)
            except:
                print("anlaşılamaz")
