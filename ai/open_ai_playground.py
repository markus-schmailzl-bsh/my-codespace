import openai

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

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSuyRKKLEOmsMkwiyKZQG22z3BhyUbp8LuTmKp7N_BkL82Y3NozpMRBduDwz_wSG_7CiHaM6OrTdE26aE5sdERFucbCkqzBc9fGdxwntkYl7ACCAbdTN_gIgeI",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])

