import subprocess
import ollama
#llama3.2
def add_to_list(item, items=[]):
    items.append(item)
    return items
print(add_to_list(1))
print(add_to_list(2))
with open("a.txt") as f:
    content = ""
    for x in f.readlines():
        content = content + " " + x
print(content)
response = ollama.chat(model='llama3:8b', messages=[
    {
        'role': 'user',
        'content': 'Сделаймне доклад на русском по следующему тексту:' + content,
    },
])

print(response['message']["content"])
