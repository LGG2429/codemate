# pulls in requests library, a bundle of prewritten code for making HTTP requests
import requests
print("Sending request to the model, please wait...")

# "send a POST request" Everything in the parentheses tells it the specifics
response = requests.post(
    "http://localhost:11434/api/generate",
    json= {
        "model" :"qwen3:8b",
        "prompt":"Write a python function that adds two numbers.",
        "stream":False # the server holds the whole thing and hands it over as one finished block
    }
)

data = response.json()
print(data["response"])

