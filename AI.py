import pyttsx3

def text_to_speech(text):
    """
    Function to convert text to speech using pyttsx3 library.

    Parameters:
    - text: str
        The input text that needs to be converted to speech.

    Returns:
    - None
        This function does not return anything, it just speaks out the input text.

    Raises:
    - RuntimeError:
        Raises an error if there are issues with the pyttsx3 library or the speech engine.
    """

    # Initialize the pyttsx3 engine
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

# Example of using the text_to_speech function:

# Input text for conversion
input_text = "This is a simple AI program that converts text to speech for long English conversations."

# Convert the text to speech
text_to_speech(input_text)