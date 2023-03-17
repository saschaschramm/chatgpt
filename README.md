# ChatGPT
[ChatGPT](https://chat.openai.com/) is a text-based AI assistant by OpenAI. This is an analysis of ChatGPT.

## Analysis of the ChatGPT API
ChatGPT can used 2 different models:
GPT-3.5 and GPT-4.

### GPT-3.5
The ChatGPT model is different from previous models. ChatGPT uses a new vocabulary with 100.000 tokens and a [Chat Markup Language](https://github.com/openai/openai-python/blob/main/chatml.md).

If we send the following message `[{"role": "user", "content": "13+37="}]`, we get the following chat completion response:

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

## GPT-4
GPT-4 seems to use a different vocabulary than GPT-3.5. If we send the following message `[{"role": "user", "content": "13+37="}]`, we get the following chat completion response:
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
| code-cushman-001 | 32.93% | 2022-10-23 | https://openai.com/api/
| code-davinci-002 | 46.95% | 2022-10-23 | https://openai.com/api/
| cushman-ml | 56.10% | 2022-10-23 | Copilot
| text-davinci-002-render | 56.10% | 2022-12-03 | https://chat.openai.com/ |
| text-davinci-002-render-sha | 70.12% | 2023-02-19 | https://chat.openai.com/ |  [2023-02-19-samples-text-davinci-002-render-sha.jsonl](2023-02-19-samples-text-davinci-002-render-sha.jsonl)
| gpt-3.5-turbo-0301 | 72.56% | 2023-03-01 | https://openai.com/api/ | [2023-03-01-samples-gpt-3.5-turbo-0301.jsonl](2023-03-01-samples-gpt-3.5-turbo-0301.jsonl)


