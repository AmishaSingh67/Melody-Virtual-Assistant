import winreg  # for accessing the registry editor

# Specify the registry key path
key_path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"

# Function to change the theme mode in the registry
def change_theme(key_name, dword_value):
    try:
        # Open the registry key
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        # Set the registry value
        winreg.SetValueEx(key, key_name, 0, winreg.REG_DWORD, dword_value)
        print("Data written to the registry successfully.")
        # Close the registry key
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Error writing to registry: {e}")

# Function to take user input and change theme mode
def set_theme_mode():
    # Take user input for theme mode
    theme_mode = input("Enter '0' for dark mode or '1' for light mode: ")
    if theme_mode in ['0', '1']:
        change_theme("AppsUseLightTheme", int(theme_mode))
    else:
        print("Invalid input. Please enter '0' or '1'.")

# Check if this script is being executed directly
if __name__ == "__main__":
    # Run the function to set the theme mode
    while  True:
        set_theme_mode()
        # Ask the user if they want to change the theme mode again
        choice = input("Do you want to change the theme mode again? (y/n): ")
        if choice.lower() != 'y':
            break


