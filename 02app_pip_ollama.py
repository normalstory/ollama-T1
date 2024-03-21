## 예제 01 # ollama-mistral for basic chat
# import ollama

# stream = ollama.chat(
#     model='mistral',
#     messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
#     stream=True,
# )

# for chunk in stream:
#   print(chunk['message']['content'], end='', flush=True)

# print(ollama.embeddings(model='mistral', prompt='They sky is blue because of rayleigh scattering'))



## 예제 02 # ollama-llava for multiModal
# import ollama

# with open('images/media_sample.png', 'rb') as file:
#     response = ollama.chat(
#         model='llava:13b',
#         messages=[
#             {
#                 'role': 'user',
#                 'content':'what is strange about this image?',
#                 'images':[file.read()],
#             },
#         ],
#     )

# print(response['message']['content'])


## 예제 03 # ollama - All commands
import ollama

# Chat function
response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])
print("Chat response:", response['message']['content'])

# Generate function
generate_response = ollama.generate(model='mistral', prompt='Why is the sky blue?')
print("Generate response:", generate_response['response'])

# List function
models_list = ollama.list()
print("List of models:", models_list)

# Show function
show_response = ollama.show('mistral')
print("Show model response:", show_response)

# Create function
modelfile = '''
FROM mistral
SYSTEM You are Mario from Super Mario Bros.
'''
create_response = ollama.create(model='example', modelfile=modelfile)
print("Create model response:", create_response)

# Copy function
copy_response = ollama.copy('mistral', 'user/mistral')
print("Copy model response:", copy_response)

# Delete function
delete_response = ollama.delete('example')
print("Delete model response:", delete_response)

# Pull function
pull_response = ollama.pull('mistral')
print("Pull model response:", pull_response)

# Push function
push_response = ollama.push('user/mistral')
print("Push model response:", push_response)

# Embeddings function
embeddings_response = ollama.embeddings(model='mistral', prompt='The sky is blue because of Rayleigh scattering')
print("Embeddings response:", embeddings_response)