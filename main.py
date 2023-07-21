import wikipedia

def search_wikipedia(query, language='en'):
    wikipedia.set_lang(language)
    try:
        page = wikipedia.page(query)
        print("Заголовок статьи:", page.title)
        print("Содержание:")
        print(page.summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Уточните ваш запрос:", e.options)
    except wikipedia.exceptions.PageError:
        print("Страница не найдена.")

if __name__ == "__main__":
    search_query = input("Введите запрос для поиска на Википедии: ")
    search_language = input("Введите язык для поиска (например, 'en' для английского): ")
    search_wikipedia(search_query, search_language)
