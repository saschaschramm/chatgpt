# ChatGPT
[ChatGPT](https://chat.openai.com/) is a text-based AI assistant by OpenAI. This is an analysis of ChatGPT.

## Analysis
### Models available via chat.openai.com

#### GPT-3.5
| title                      | slug                                         |   max_tokens | description                                       |
|:---------------------------|:---------------------------------------------|-------------:|:--------------------------------------------------|
| Default (GPT-3.5)          | text-davinci-002-render-sha                  |         8191 | Our fastest model, great for most everyday tasks. |
| Default (GPT-3.5) (Mobile) | text-davinci-002-render-sha-mobile           |         8191 | Our fastest model, great for most everyday tasks. |
| Code Interpreter           | text-davinci-002-render-sha-code-interpreter |          nan | nan                                               |
| Plugins                    | text-davinci-002-render-sha-plugin           |          nan | nan                                               |

#### GPT-4
| title              | slug                   |   max_tokens | description                                                                             |
|:-------------------|:-----------------------|-------------:|:----------------------------------------------------------------------------------------|
| GPT-4              | gpt-4                  |         4095 | Our most capable model, great for tasks that require creativity and advanced reasoning. |
| Plugins            | gpt-4-plugins          |         8192 | An experimental model that knows when and how to use plugins                            |
| GPT-4 (Mobile, V2) | gpt-4-mobile           |         4095 | Our most capable model, great for tasks that require creativity and advanced reasoning. |
| Code Interpreter   | gpt-4-code-interpreter |          nan | nan                                                                                     |

### Models available via platform.openai.com
| Model | Max tokens | Training data (pre-training) |
| --- | --- | --- |
| gpt-4-0613 | 8192 | Up to Sep 2021
| gpt-4-32k-0613 | 32768 | Up to Sep 2021
| gpt-3.5-turbo-0613 | 4096 | Up to Sep 2021
| gpt-3.5-turbo-16k-0613 | 16384 | Up to Sep 2021
| gpt-4-0314 | 8192 | Up to Sep 2021
| gpt-4-32k-0314 | 32768 | Up to Sep 2021
| gpt-3.5-turbo-0301 | 4096 | Up to Sep 2021

### Completion
If we send the message `[{"role": "user", "content": "13+37="}]` to the model, it returns the following chat completion response:
| Model | Completion |
| - | - |
| gpt-3.5-turbo-0613 | [Link](completions/gpt-3.5-turbo-0613.json) |
| gpt-4-0613 | [Link](completions/gpt-4-0613.json) |

### Vocabulary
The ChatGPT models employ a distinct vocabulary compared to their predecessors. The models use a `cl100k_base` vocabulary with `100,000` tokens, where each token encodes an average of `3.7` characters in English. For a detailed analysis, see [vocab.ipynb](vocab.ipynb). 

Additionally, these models employ the [Chat Markup Language](https://github.com/openai/openai-python/blob/main/chatml.md).

### Tokenizer
The number of prompt tokens and completion tokens are computed as follows (see [OpenAI-Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb) for details):
```python
prompt_tokens = ['<|im_start|>', 'user', '\n', '13', '+', '37', '=', '<|im_end|>', '\n', '<|im_start|>', 'assistant',  '<|message|>']
# len(tokens) is 12
```

```python
completion_tokens = ['50']
# len(tokens) is 1
```

> It's unclear why the model returns 11 prompt tokens instead of 12. Maybe there is no `\n` after the role `user`.

## Performance
We have evaluated the ChatGPT model `gpt-4-0613` with the [HumanEval](https://github.com/openai/human-eval) dataset. Out of 164 programming problems, the model can solve `86.59%`.
| Model name | Pass@1 | Date | Comment | Results | Prompt
| - | - | - | - | - | - | 
| gpt-4-0613 | 86.59% | 2023-06-13 | https://platform.openai.com/ | [Link](2023-06-13-samples-gpt-4-0613.jsonl_results.jsonl) | Complete the following code. Use ```python to put the completed Python code in markdown quotes:\n{code}
| gpt-3.5-turbo-0613 | 71.34% | 2023-06-13 | https://platform.openai.com/ | [Link](2023-06-13-samples-gpt-3.5-turbo-0613.jsonl_results.jsonl) | Complete the following code. Use ```python to put the completed Python code in markdown quotes:\n{code}
| gpt-4-0314 | 78.66% | 2023-03-17 | https://platform.openai.com/ | [Link](2023-03-17-samples-gpt-4-0314.jsonl_results.jsonl) | Complete the following code:\n{code}
| gpt-3.5-turbo-0301 | 74.39% | 2023-04-24 | https://platform.openai.com/ | [Link](2023-04-24-samples-gpt-3.5-turbo-0301.jsonl_results.jsonl) | Complete the following code. Use ```python to put the Python code in markdown quotes:\n{code}
| text-davinci-002-render-sha | 70.12% | 2023-02-19 | https://chat.openai.com/ |  
| text-davinci-002-render | 56.10% | 2022-12-03 | https://chat.openai.com/ |
| cushman-ml | 56.10% | 2022-10-23 | Copilot
| code-davinci-002 | 46.95% | 2022-10-23 | https://platform.openai.com/
| code-cushman-001 | 32.93% | 2022-10-23 | https://platform.openai.com/