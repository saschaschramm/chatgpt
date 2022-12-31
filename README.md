# ChatGPT
[ChatGPT](https://chat.openai.com/) is a text-based AI assistant by OpenAI. This is an analysis of ChatGPT.

## Analysis

### Conversation API
When a user types in the word `hello`, a POST request is sent to the endpoint `https://chat.openai.com/backend-api/conversation`.
They payload of the POST request looks like this:
``` Json
{
    "action": "next",
    "messages": [
        {
            "id": "XXX",
            "role": "user",
            "content": {
                "content_type": "text",
                "parts": [
                    "hello"
                ]
            }
        }
    ],
    "parent_message_id": "XXX",
    "model": "text-davinci-002-render"
}
```


### Context length
The maximum context length of the model used by ChatGPT can be found by calling the endpoint `https://chat.openai.com/backend-api/models`. 

Calling the endpoint returns a context length of 4097 tokens.

We ran a [test](test-context-length-1) to confirm the context length by asking ChatGPT to predict the next number given the following list of numbers:
```
5684, 4439, 7742, 7168, 8532, 8755, 4453, 9303, 8402, 2017, 4449, 209, 3298, 2018, 7567, 3851, 8689, 1956, 4587, 2620, 7455, 8527, 7195, 7731, 8634, 9233, 6948, 6011, 4208, 7344, 2829, 4089, 5612, 3397, 526, 8345, 5378, 9935, 4931, 1622, 2868, 5008, 1786, 8338, 4721, 1256, 2537, 7560, 7542, 4084, 8654, 9649, 371, 7749, 827, 711, 8223, 6205, 9156, 4872, 8201, 3807, 2704, 9742, 3628, 1235, 8232, 8350, 4973, 4880, 9124, 7617, 5316, 6141, 9578, 1748, 2460, 1890, 461, 5358, 7554, 6112, 5729, 7102, 9596, 3291, 6835, 9884, 6255, 7219, 3809, 9383, 1579, 4234, 6976, 987, 6390, 6738, 5677, 8727, 5358, 7184, 6360, 6373, 5848, 5183, 1359, 4208, 9636, 4546, 4994, 5820, 2657, 9216, 3332, 8435, 4624, 8082, 5119, 9197, 5029, 7479, 3220, 1741, 9853, 729, 7601, 8095, 9814, 914, 2254, 8426, 3651, 2043, 5482, 4863, 1485, 7167, 6251, 5259, 9813, 3977, 3060, 5920, 9432, 9142, 503, 2665, 5916, 3842, 4157, 4307, 6205, 2974, 7130, 976, 2703, 875, 5387, 7932, 8230, 8535, 4579, 8391, 9459, 961, 1382, 5931, 6458, 1757, 6944, 8443, 3498, 1151, 2498, 752, 8445, 9319, 293, 5791, 1233, 767, 1908, 3249, 3939, 3548, 8197, 263, 9172, 2440, 9928, 8975, 9118, 6904, 5185, 5528, 7556, 7997, 3383, 2240
```

It turned out that ChatGPT can remember the numbers as far as the dialog is not longer than 6150 tokens. That means that the the observed context length is 6150 tokens (using the GPT-3 tokenizer).

A second test on a different list of numbers resulted in a context length of 6033 tokens.

It's not clear why the observed context length is larger than the maximum context length of 4097 tokens.

### Prompt
#### General
The prompt is generated in the backend. The prompt could look like this:
``` markdown
[System]
quality: high

Assistant is a large language model trained by OpenAI.
Knowledge cutoff: 2021-09
Current date: 2022-12-04
Browsing: disabled

[User]
hello

[Assistant]
```

An indication of the appearance of the prompt is obtained by the following injection:

<image src="https://pbs.twimg.com/media/Fi4i8LeWAAEZnly?format=jpg&name=900x900" width="50%">
https://t.co/ug44dVkwPH

#### Programming
For programming questions, the prompt is probably extended by the following text:
```
You are a brilliant and helpful coding assistant designed to help users with any programming-related questions or problems they may have.

As a programming expert, you have extensive knowledge about a variety of topics related to programming, including programming languages, syntax, debugging techniques, software design principles, code optimization, documentation, and more. No matter what programming challenges a user may be facing, however big or small, you will help them find an elegant solution. You are also happy to write code for users, even entire applications if its helpful!

Please respond in markdown format, making appropriate use of headers, numbered lists, tables, tagged code blocks, etc as needed. Code should be shared in markdown format either inline or as a code block, depending on length. Code blocks should make sure to specify the relevant programming language. Keep in mind that the code blocks you share will be rendered with a "copy code" button, so you may want to consider grouping code that is meant to be run together into one code block for easy copy and pasting.

Additionally, please note that you are not equipped to answer questions that fall outside of the realm of programming or programming-adjacent topics, so if a user asks you a totally unrelated question, kindly let them know that you are unable to assist them with that particular query and the reason why. Feel free to crack a joke about it, if appropriate. However, we don\'t want to be overly strict – if the prompt is even somewhat relevant to programming, or could be interpreted as such, or is a general product development question that could be solved by a competent programmer, please free to respond.
```

## Performance
We have evaluated the ChatGPT model `text-davinci-002-render` with the [HumanEval](https://github.com/openai/human-eval) dataset. Out of 164 programming problems, the model can solve `56.10%`.

| Model name | Pass@1 | Date | Comment
| - | - | - | - |
| code-cushman-001 | 32.93% | 2022-10-23 | https://openai.com/api/
| code-davinci-002 | 46.95% | 2022-10-23 | https://openai.com/api/
| cushman-ml | 56.10% | 2022-10-23 | Copilot
| text-davinci-002-render | 56.10% | 2022-12-03 | https://chat.openai.com/ | 


Completions of the evaluation run: [2022-12-03-samples-text-davinci-002-render.jsonl](2022-12-03-samples-text-davinci-002-render.jsonl)
