import pprint

import requests

api_secret_key = ''

headers = {
    'Authorization': f"Bearer {api_secret_key}",
    "OpenAI-Organization": "org-NgAVjODe9GELEa9ptn4kH1AA"
}

api_url = 'https://api.openai.com/v1/models'

res = requests.get(api_url, headers=headers)

#pprint.pprint(res.json())

while True:
    prompt = input(">>")
    prompt_data = {
      "model": "text-davinci-003",
      "prompt": prompt,
      "max_tokens": 70,
      # "temperature": 0,
      # "top_p": 1,
      # "n": 1,
      # "stream": False,
      # "logprobs": None,
      # "stop": "\n"
    }

    prompt_url = 'https://api.openai.com/v1/completions'
    res = requests.post(prompt_url, headers=headers, json=prompt_data)
    ans = res.json()['choices'][0]['text']
    #pprint.pprint(res.json())
    print("Output", ans)