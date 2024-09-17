import speech_recognition as sr

def main():
    r = sr.Recognizer()  # Corrected recognizer class
    
    with sr.Microphone() as source:  # Corrected Microphone class
        r.adjust_for_ambient_noise(source)  # Fixed typo in adjust_for_ambient_noise
        
        print("Please say something")
        
        audio = r.listen(source)
        
        print("Recognizing Now...")
        
        # Recognize speech using Google API
        try:
            print("You have said:\n" + r.recognize_google(audio))
            print("Audio recorded successfully\n")
        except Exception as e:
            print("Error: " + str(e))
    
        # Write audio to a file
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

if __name__ == "__main__":  # Corrected typo
    main()
