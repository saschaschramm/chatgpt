# ChatGPT
[ChatGPT](https://chat.openai.com/) is a text-based AI assistant by OpenAI. This is an analysis of ChatGPT.

## Analysis of the ChatGPT API
ChatGPT can used 2 different models:
* gpt-3.5-turbo
* gpt-4

### gpt-3.5-turbo
The model `gpt-3.5-turbo` is different from previous models. The model uses a new vocabulary with 100.000 tokens and the [Chat Markup Language](https://github.com/openai/openai-python/blob/main/chatml.md).

If we send the message `[{"role": "user", "content": "13+37="}]` to the model, we get the following chat completion response:

```json
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "\n\n50",
        "role": "assistant"
      }
    }
  ],
  "created": 1679066912,
  "id": "chatcmpl-XXX",
  "model": "gpt-3.5-turbo-0301",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 2,
    "prompt_tokens": 11,
    "total_tokens": 13
  }
}
```

The number of prompt tokens and completion tokens are computed as follows:
```python
prompt_tokens = ['<|im_start|>', 'user', '\n', '13', '+', '37', '=', '<|im_end|>', '\n', '<|im_start|>', 'assistant']
# len(tokens) is 11
```

```python
completion_tokens = ['\n\n', '50']
# len(tokens) is 2
```

## gpt-4
`gpt-4` seems to use a different vocabulary than `gpt-3.5-turbo`. If we send the message `[{"role": "user", "content": "13+37="}]` to the model, we get the following chat completion response:
```json
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "50",
        "role": "assistant"
      }
    }
  ],
  "created": XXX,
  "id": "chatcmpl-XXX",
  "model": "gpt-4-0314",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 2,
    "prompt_tokens": 10,
    "total_tokens": 12
  }
}
```

## Performance
We have evaluated the ChatGPT model `text-davinci-002-render-sha` with the [HumanEval](https://github.com/openai/human-eval) dataset. Out of 164 programming problems, the model can solve `70.12%`.

| Model name | Pass@1 | Date | Comment | Completions of evaluation run
| - | - | - | - | - |
| gpt-4-0314 | 78.66% | 2023-03-17 | https://openai.com/api/ | [2023-03-17-samples-gpt-4-0314.jsonl](2023-03-17-samples-gpt-4-0314.jsonl)
| gpt-3.5-turbo-0301 | 72.56% | 2023-03-01 | https://openai.com/api/ | [2023-03-01-samples-gpt-3.5-turbo-0301.jsonl](2023-03-01-samples-gpt-3.5-turbo-0301.jsonl)
| text-davinci-002-render-sha | 70.12% | 2023-02-19 | https://chat.openai.com/ |  [2023-02-19-samples-text-davinci-002-render-sha.jsonl](2023-02-19-samples-text-davinci-002-render-sha.jsonl)
| text-davinci-002-render | 56.10% | 2022-12-03 | https://chat.openai.com/ |
| cushman-ml | 56.10% | 2022-10-23 | Copilot
| code-davinci-002 | 46.95% | 2022-10-23 | https://openai.com/api/
| code-cushman-001 | 32.93% | 2022-10-23 | https://openai.com/api/