# DanaGPT
A (future) FLASK application to give a ChatGPT-like experience without the hassle of OpenAI's content policy.

## Requirements
- (optional) Python [virtual environment](https://python.land/virtual-environments/virtualenv) (always recommended)
- An [OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key).
- Install OpenAI and tiktoken python modules
    ```
    pip3 install openai
    pip3 install tiktoken
    ```

## File descriptions
| Filename | Description |
| --- | --- |
| secrets.py-example | Sample Python file that holds your OpenAI API key |
| scrap/ | Pieces used for development and testing |
| scrap/proto-text.py | Command line-based demo of DanaGPT |
| scrap/summary-test.py | A quick test of the summarizing routine (for when there are too many tokens in the prompt) |

## How to use
- Copy _secrets.py-example_ to _secrets.py_.
- Get OpenAI API key & insert it into _secrets.py_.

## To do:
- Change prompt/message to an array of strings (instead of one large string).
- Experiment between [text completion](https://platform.openai.com/docs/guides/completion) and [chat](https://platform.openai.com/docs/guides/chat) to see difference of responses.
- Construct a better prompt (see [Chat Completions/Introduction](https://platform.openai.com/docs/guides/chat/introduction))

## Misc. info
- [OpenAI chat API info](https://platform.openai.com/docs/guides/chat/introduction)
- [openai/openai-python module (github)](https://github.com/openai/openai-python)
