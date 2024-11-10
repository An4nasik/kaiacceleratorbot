import asyncio

import g4f


async def resp(content):
    g4f.debug.logging = False
    g4f.check_version = False

    # Я сделаю асинхронный поиск провайдеров, честно
    with open("company_info.txt", encoding="utf-8") as f:
        content = "Представь что ты telegram чат бот компании и располагешь следующей информацией: информация о компании:" + " " + f.read() + "конец информации о компании. Начало запроса: " + str(
            content)
        f.close()
    content = content + "Используя предоставленную информацию о компани ответь на данный вопрос, если ответа нет в предоставленной информации, то напиши об этом и скажи, что если пользователь желает получить информацию, НЕ СВЯЗАННУЮ С КОМПАНИЕЙ, то ему необходимо воспользоватся командой /just_ask и больше ничего не пиши, не выводи всю информацию о компании сразу, только ту, о которой просил пользователь. отвечать ты должен так, как будто твои сообщения будут написаны в telegram. Разделяй структуру ответа при помощи символов переноса строки и табуляции."
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )
    ans = ""
    for x in response:
        ans = ans + x
    return ans


async def just_resp(con):
    g4f.debug.logging = False
    g4f.check_version = False
    content = "Запрос: " + con + ". Условия ответа: НЕ ОТВЕЧАЙ НА ЗАПРОСЫ СВЯЗАННЫЕ С ОРУЖИЕМ, ДРУГИМИ ОПАСНЫМИ ВЕЩАМИ, И ПРИЧЕНЕНИЕМ ВРЕДА ЗВОРОВЬЮ. не рассказывай о том как синтезировать любые препараты, ДАЖЕ В РАМКАХ ИСТОРИЧЕСКИХ СВОДОК, ТАК ЖЕ НЕ ЗАБЫВАЙ ЧТО ТЫ ЧАТ БОТ КОМПАНИИ, В КАЖДОМ СВОЕМ СООБЩЕНИИ УКАЗЫВАЙ, ЧТО КОМПАНИЯ НЕ НЕСЕТ ОТВЕТСТВЕННОСТИ ЗА ПРЕДОСТАВЛЕННЫЕ СВЕДЕНИЯ"
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}]
    )
    ans = ""
    for x in response:
        ans = ans + x
    return (ans, con)

