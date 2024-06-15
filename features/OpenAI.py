chatStr = ""

def chat(order):
    global chatStr
    print(chatStr)
    openai.api_key = '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'
    chatStr += f"Boss: {order}\n Jarvis: "
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]




#Define a function to recognize speech from the microphone

chat(order)

