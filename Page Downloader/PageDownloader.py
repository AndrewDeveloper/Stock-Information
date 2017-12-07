# Этот код будет скачивать веб-страницу
import urllib.request

def getDownloadedPage(url):
    # Начинаем создавать запрос
    req = urllib.request.Request(url)

    # Добавляем заголовки: User-Agent
    req.add_header('User-Agent',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')

    # Открываем соединение
    response = urllib.request.urlopen(req)

    # Возвращаем код страницы
    return response.read()

print(getDownloadedPage('https://github.com/freenetwork/investing.com.economic-calendar/blob/master/investing.py'))