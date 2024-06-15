import streamlit as st
import subprocess
import base64

def main():
    # Read the background image file and encode it to base64
    with open("Background.png", "rb") as f:
        image_data = f.read()
        base64_image = base64.b64encode(image_data).decode("utf-8")

    # Define the custom CSS with the background image
    custom_css = f"""
    <style>
    /* Custom CSS for the app background */
    .stApp {{
        background-image: url('data:image/png;base64,{base64_image}');  /* Use base64 encoded image */
        background-size: cover;  /* Cover the entire background */
        background-repeat: no-repeat;  /* Do not repeat the background image */
        position: fixed;
        width: 100%;
        height: 100%;
    }}

    /* Custom CSS for the output container */
    .output-container {{
        padding: 20px;  /* Add padding */
        background-color: rgba(255, 255, 255, 0.5);  /* Set background color with opacity */
        border-radius: 5px;  /* Add border radius */
    }}
    </style>
    """

    # Render the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Container for the output
    output_container = st.container(height=510, border=None)

    # Display GIF from local file
    file_ = open("./SiriWave.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True
    )

    # Execute a subprocess and capture its output
    process = subprocess.Popen(["python", "-u", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    output_lines = []

    # Display the output of the subprocess within the container
    for line in iter(process.stdout.readline, ''):
        output_lines.append(line)
        with output_container:
            st.text("".join(output_lines).encode('utf-8').decode('utf-8', 'ignore'))  # Display the output



if __name__ == "__main__":
    main()
