import whisper

def transcribe_audio(audio_file:str) -> str:
    '''
    Purpose: Use Whisper AI to transcribe the audio to text
    Parameter: A string representing the file path of the audio file
    Return: A string of transcribed text from the audio file
    '''

    # Base used for simple tasks, can be changed depending on size
    model = whisper.load_model('base') 
    result = model.transcribe(audio_file)
    return result['text']

def find_indices(prompt:str) -> tuple:
    """
    Purpose: Finds the indices of periods (end of sentences) and numbers in the prompt
    Parameters: A string of text which is the prompt
    Return: A tuple of two lists - end_indices for sentence endings and num_indices for numbers
    """

    # Initializing empty lists
    end_indices = []
    num_indices = []
    
    # Iterate through characters inthe prompt
    for i, char in enumerate(prompt):
        if char == ".":
            end_indices.append(i)
        elif char.isdigit():
            num_indices.append(i)
    return end_indices, num_indices

def make_options(prompt:str, end_indices:list, num_indices:list) -> list:
    """
    Purpose: Creates menu options based on the indices of numbers and sentence endings
    Parameters: The string of text (prompt), and the two generated lists from find_indices
    Return: A list of formatted options
    """

    #Initialize Empty List
    options = []

    #Iterate through the numbers in the num_indices list
    for num_index in num_indices:
        #Find the closest period before the number
        last_index = max(i for i in end_indices if i < num_index)
        #Extract and format the option text
        option = prompt[last_index + 1:num_index].strip()
        option = f"[{prompt[num_index]}] {option}".replace(", please press", "").replace(", press", "").strip()
        options.append(option)
    return options

def main(audio_file:str) -> None:
    """
    Purpose: Main function to print menu options from the given audio
    Parameters: The string of text (audio file)
    Return: None
    """

    # Generating the prompt using the helper
    prompt = transcribe_audio(audio_file)

    end_indices, num_indices = find_indices(prompt)
    options = make_options(prompt, end_indices, num_indices)
    for option in options:
        print(option)

'''
Things to Improve:
1) Add Edge Cases -> if not prompt (empty audio file), if not options (missing numbers)
2) Add resulting text flexability for parsing -> include "hit" or "choose" as precursors to options
3) Add an option for "stay/hold on the line"
'''