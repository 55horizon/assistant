messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. You also have the ability to access DALL-E 3 by triggering a command that will run a prompt. If you are asked to do something that involves creating an image, repeat as follows: `use-dalle-system-prompt:` and the requested image prompt right after. You should not add any other text to that kind of response.",
    }
]


def push(role, content):
    messages.append({"role": role, "content": content})
