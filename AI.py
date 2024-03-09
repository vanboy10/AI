import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    try:
        
        engine.setProperty('rate', 150)  
        engine.setProperty('volume', 0.9)  

        
        engine.say(text)
        engine.runAndWait()

    except RuntimeError as e:
        raise RuntimeError(f"Error occurred during text-to-speech conversion: {e}")




input_text = "My name vanboy im mentee Infinit Learning ."


text_to_speech(input_text)


