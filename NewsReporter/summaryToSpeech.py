import requests
import os
from IPython.display import Audio
import soundfile as sf

API_URL = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech"
headers = {"Authorization": ""}
folder_path = "./audio_files/"

def getTextToSpeech(payload,title):
    req = {"inputs" : payload}
    response = requests.post(API_URL,headers=headers, json=req)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, title + ".wav")
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Audio saved at {file_path}")
getTextToSpeech("A US man has been found guilty of lying to investors and lenders and stealing billions of dollars from a crypto-currency exchange.","test_file")

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response


#
# response = query({
#     "inputs": "The answer to the universe is 42",
# })

# Save the audio to a folder




#
# # You can also display the audio using IPython.display
# Audio(file_path)

