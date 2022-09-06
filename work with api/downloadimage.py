import requests


def save_results(file_name, text):
    with open(file_name, mode='wb') as file:
        file.write(text)
        file.close()


request = requests.get("https://api.telegram.org/file/bot5565142493:AAGslA8qqKs6wtfhjR5aJ_F2dqXQX0VH5GU/photos/file_0.jpg")
save_results("img.jpg",request.content)

