import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    try:
        # Setting properties for the speech
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 0.9)  # Volume level

        # Speaking out the input text
        engine.say(text)
        engine.runAndWait()

    except RuntimeError as e:
        raise RuntimeError(f"Error occurred during text-to-speech conversion: {e}")




input_text = "My name vanboy im mentee Infinit Learning ."


text_to_speech(input_text)
