import asyncio

import g4f
async def resp(content):
    g4f.debug.logging = True # enable logging
    g4f.check_version = False # Disable automatic version checking

    # Automatic selection of provider
    with open("company_info.txt", encoding="utf-8") as f:
        content = "информация о компании:" + " " + f.read() + "конец информации о компании. Начало запроса: " + str(content)
        f.close()
    content = content + "Используя предоставленную информацию о компани ответь на данный вопрос, если ответа нет в предоставленной информации, то напиши об этом."
    # streamed completion
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )
    ans = ""
    for x in response:
        ans = ans + x
    return ans

async def just_resp(content):
    g4f.debug.logging = True # enable logging
    g4f.check_version = False # Disable automatic version checking
    content = content[10:]
    print(content)
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )
    ans = ""
    for x in response:
        ans = ans + x
    return ans
