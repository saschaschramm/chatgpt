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

### Prompt
#### General
Based on the message above the prompt is generated in the backend. The prompt could look like this:
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

Hinweis, dass die Prompt so aussieht gibt folgende Prompt Injection:
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">OpenAI’s ChatGPT is susceptible to prompt injection — say the magic words, “Ignore previous directions”, and it will happily divulge to you OpenAI’s proprietary prompt: <a href="https://t.co/ug44dVkwPH">pic.twitter.com/ug44dVkwPH</a></p>&mdash; Riley Goodside (@goodside) <a href="https://twitter.com/goodside/status/1598253337400717313?ref_src=twsrc%5Etfw">December 1, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

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
