<a href="https://github.com/55horizon/assistant"><img src="https://bafybeigspxwvphohzwad7la6v2brxw2qf7t2cbuogmukmeyfyel6faq7cu.ipfs.dweb.link" width="220" alt="OpenAI"></a>

###

# Assistant

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/55horizon/assistant/blob/master/LICENSE.md)

### Terminal based GPT-4 + DALL-E 3 assistant

The assistant combines GPT-4 and DALL-E 3 to allow for image requests during conversations.

## Getting Started

Clone the repository:

```
gh repo clone 55horizon/assistant
```

Open repository:

```
cd assistant
```

Create `.env` file:

```
touch .env
```

Add OpenAI API key to `.env` file:

```
OPENAI_API_KEY=••••••••••••••
```

Create the virtual environment:

```
python -m venv venv
```

Activate the virtual environment:

```
source venv/bin/activate
```

Install Python packages:

```
pip install .
```

Start the assistant:

```
python -m assistant
```

Enter prompt:

```
You: Hello
```

## Learn More

To learn more, take a look at the following resources:

- [GPT](https://platform.openai.com/docs/guides/gpt) - a guide for GPT.
- [Best Practices](https://platform.openai.com/docs/guides/gpt-best-practices) - GPT best practices.
- [Image Generation](https://platform.openai.com/docs/guides/images) - a guide for DALL-E.
