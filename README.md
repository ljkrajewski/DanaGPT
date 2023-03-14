# DanaGPT
A (future) FLASK application to give a ChatGPT-like experience without the hassle of OpenAI's content policy.

## Requirements
- (optional) Python [virtual environment](https://python.land/virtual-environments/virtualenv) (always recommended)
- An [OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key).
- Install OpenAI python module `pip3 install openai`

## File descriptions
| Filename | Description |
| --- | --- |
| secrets.py-example | Sample Python file that holds your OpenAI API key |
| scrap/ | Pieces used for development and testing |
| scrap/proto.py | Command line-based demo of DanaGPT |

## How to use
- Copy _secrets.py-example_ to _secrets.py_.
- Get OpenAI API key & insert it into _secrets.py_.

## To do:
~~- Write the base README~~
- Change prompt/message to an array of strings (instead of one large string).
- Experiment between [text completion](https://platform.openai.com/docs/guides/completion) and [chat](https://platform.openai.com/docs/guides/chat) to see difference of responses.
- Construct a better prompt (see [Chat Completions/Introduction](https://platform.openai.com/docs/guides/chat/introduction))
~~- Add logging to prototype~~
~~- Use [_OpenAI.tiktoken_](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb) to count tokens.~~
- Write summarizing routine for when number of tokens exceed the maximum allowed.

## Misc. info
- [OpenAI chat API info](https://platform.openai.com/docs/guides/chat/introduction)
