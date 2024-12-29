# Program to parse a prompt and generate a list of menu options

def find_indices(prompt:str) -> tuple:
    """
    Purpose: Finds the indices of periods (end of sentences) and numbers in the prompt
    Parameters: A string of text which is the prompt
    Return: A tuple of two lists - end_indices for sentence endings and num_indices for numbers
    """

    #Initializing empty lists
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

def main(prompt:str) -> None:
    """
    Purpose: Main function to generate and print menu options from the given prompt
    Parameters: The string of text (prompt)
    Return: None
    """
    
    end_indices, num_indices = find_indices(prompt)
    options = make_options(prompt, end_indices, num_indices)
    for option in options:
        print(option)

# Example Input prompt
prompt = ("Please listen carefully as our menu options have changed. "
          "For residential sales, please press 1. For installer and integrator sales, press 2. "
          "For product questions or technical support, please press 3. If you have a question about an existing order, "
          "or for any other customer service inquiries, press 4. If you are a current supplier, please press 5. "
          "If you are a freight carrier and need to schedule a delivery appointment, press 6. "
          "All other calls, press 7.")

# Execute the program
main(prompt)