import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix-like systems (Linux, macOS)
    else:
        _ = os.system('clear')

# Define a function to clear previous chats in the terminal window
def clear_previous_chats():
    # Print enough empty lines to push previous chats out of view
    print('\n' * 50)  # Adjust the number of lines as needed


#clear_screen()
#clear_previous_chats()