import openai
import requests

# # Define your question
# response = openai.ChatCompletion.create(
#   model="gpt-4o-mini",  # or use "gpt-4" if you have access
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Can you create me a list of 100 recipes in json format. Every recipe should contain the ingredients need to cook the recipe"}
#   ]
# )

# # Print the response
# print(response['choices'][0]['message']['content'].strip())

#python open_ai_playground.py && chafa /tmp/generated_image.png

from openai import OpenAI
import requests
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a electric car with a futuristic style",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

# Download the image
image_response = requests.get(image_url)

# Save the image to a file
with open('/tmp/generated_image.png', 'wb') as f:
    f.write(image_response.content)

print("Image downloaded successfully!")




exit(0)

# Create an image
response = openai.Image.create(
    prompt="A beautiful landscape with mountains and a river",
    n=1,
    size="1024x1024"
)

# Get the URL of the generated image
image_url = response['data'][0]['url']
print(f"Image URL: {image_url}")

# Download the image
image_response = requests.get(image_url)

# Save the image to a file
with open('generated_image.png', 'wb') as f:
    f.write(image_response.content)

print("Image downloaded successfully!")

exit(0)

# Generate an image using OpenAI API
response = openai.Image.create(
    prompt="A futuristic cityscape at sunset",
    n=1,
    size="1024x1024"
)

# Get the URL of the generated image
image_url = response['data'][0]['url']

# Download the image
image_response = requests.get(image_url)

# Save the image to a file
with open('generated_image.png', 'wb') as f:
    f.write(image_response.content)

print("Image downloaded and saved as 'generated_image.png'")

exit(0)

# from openai import OpenAI

# client = OpenAI()

# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {"type": "text", "text": "What’s in this image?"},
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSuyRKKLEOmsMkwiyKZQG22z3BhyUbp8LuTmKp7N_BkL82Y3NozpMRBduDwz_wSG_7CiHaM6OrTdE26aE5sdERFucbCkqzBc9fGdxwntkYl7ACCAbdTN_gIgeI",
#           },
#         },
#       ],
#     }
#   ],
#   max_tokens=300,
# )

# print(response.choices[0])


