import speech_recognition as sr
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
insta_image = os.path.join(BASE_DIR, "insta_image.jpeg")
x_image = os.path.join(BASE_DIR, "x_image.jpeg")
linkedin_image = os.path.join(BASE_DIR, "linkedin_image.jpeg")
whatsapp_image = os.path.join(BASE_DIR, "whatsapp_image.jpeg")

recog = sr.Recognizer()

def open_image_windows(path):
    os.system("taskkill /f /im Microsoft.Photos.exe /t >nul 2>&1")
    time.sleep(0.5)
    
    if os.path.exists(path):
        os.startfile(path)
    else:
        print(f"File not found: {path}")

with sr.Microphone() as source:
    print("Calibrating microphone...")
    recog.adjust_for_ambient_noise(source, duration=1)
    
    while True:
        try:
            print("\nDinleniyor... (Listening)")
            audio = recog.listen(source, phrase_time_limit=3)
            text = recog.recognize_google(audio).lower()
            print(f"Heard: {text}")

            # Improved Logic with alias lists
            if any(word in text for word in ["instagram", "insta"]):
                open_image_windows(insta_image)

            elif any(word in text for word in ["x", "twitter", "ex", "axe", "acts"]):
                open_image_windows(x_image)
        
            elif any(word in text for word in ["linkedin", "linked", "link in", "lincol"]):
                open_image_windows(linkedin_image)

            elif "whatsapp" in text:
                open_image_windows(whatsapp_image)
                
            elif "close" in text or "kapat" in text:
                os.system("taskkill /f /im Microsoft.Photos.exe /t >nul 2>&1")

        except sr.UnknownValueError:
            pass
        except Exception as e:
            print(f"Error: {e}")