from .openai import text_response, image_response
from .data import messages, push

while True:
    user_input = input("\nYou: ")
    if user_input == "q":
        break
    push("user", user_input)
    response = text_response(messages)
    push("assistant", response)
    if "use-dalle-system-prompt" in response:
        prompt = response.replace("use-dalle-system-prompt:", "")
        response = image_response(prompt)
        print(f"\n{response}")
    else:
        print(f"\nAssistant: {response}")
