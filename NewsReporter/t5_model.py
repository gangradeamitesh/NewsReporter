import requests

API_URL = "https://api-inference.huggingface.co/models/minhtoan/t5-finetune-bbc-news"
headers = {"Authorization": ""}


# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()[0]['summary_text']

def summarize_text(paragraph):
    req = {"inputs":paragraph}
    response = requests.post(API_URL, headers=headers, json=req)
    print(response.json()[0]['summary_text'])
    return response.json()[0]['summary_text']

#
# output = query({
#     "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
# })
# print(output)