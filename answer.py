import asyncio

from ollama import AsyncClient


async def resp(content):
    # Я сделаю асинхронный поиск провайдеров, честно
    with open("company_info.txt", encoding="utf-8") as f:
        print(f.read())
        content = ("Отвечай на все запросы на русском языке. Представь что ты telegram чат бот компании и располагешь "
                   "следующей информацией: информация о компании:") + " " + f.read() + ("конец информации о компании. "
                                                                                        "Начало запроса: ") + str(
            content)
        f.close()
    content = content + ("Используя предоставленную информацию о компани ответь на данный вопрос, если ответа нет в "
                         "предоставленной информации, то напиши об этом и скажи, что если пользователь желает "
                         "получить информацию, НЕ СВЯЗАННУЮ С КОМПАНИЕЙ, то ему необходимо воспользоватся командой "
                         "/just_ask и больше ничего не пиши, не выводи всю информацию о компании сразу, только ту, "
                         "о которой просит пользователь. отвечать ты должен так, как будто твои сообщения будут "
                         "написаны в telegram. Разделяй структуру ответа при помощи символов переноса строки и "
                         "табуляции.")
    response = await AsyncClient().chat(
        model='llama3:8b',
        messages=[{"role": "user", "content": content}],
    )

    return response['message']['content'].replace("/", "")


async def just_resp(con):
    content = "Отвечай на все запросы на русском языке. Запрос: " + con + (". Условия ответа: НЕ ОТВЕЧАЙ НА ЗАПРОСЫ "
                                                                           "СВЯЗАННЫЕ С ОРУЖИЕМ, ДРУГИМИ ОПАСНЫМИ "
                                                                           "ВЕЩАМИ, И ПРИЧЕНЕНИЕМ ВРЕДА ЗВОРОВЬЮ. не "
                                                                           "рассказывай о том как синтезировать любые "
                                                                           "препараты, ДАЖЕ В РАМКАХ ИСТОРИЧЕСКИХ "
                                                                           "СВОДОК, ТАК ЖЕ НЕ ЗАБЫВАЙ ЧТО ТЫ ЧАТ БОТ "
                                                                           "КОМПАНИИ, В КАЖДОМ СВОЕМ СООБЩЕНИИ "
                                                                           "УКАЗЫВАЙ, ЧТО КОМПАНИЯ НЕ НЕСЕТ "
                                                                           "ОТВЕТСТВЕННОСТИ ЗА ПРЕДОСТАВЛЕННЫЕ "
                                                                           "СВЕДЕНИЯ")
    response = await AsyncClient().chat(
        model='llama3:8b',
        messages=[{"role": "user", "content": content}],
    )
    return (response['message']['content'].replace("/", ""), con)


