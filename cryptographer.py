import os
print('Установка дополнительных модулей...')
os.system('pip install --upgrade pip')
os.system('pip install colorama')
os.system('pip install requests')
print('Импортирую модули...')
import requests
import threading
import time
import colorama
from colorama import Fore
colorama.init()
print('Запуск программы...')
version = 'v2.0'
print(version)
print(Fore.GREEN + 'Created by SKATT')
time.sleep(1)
print(Fore.BLUE + 'Проверяю соединение с интернетом')
try:
    requests.get("https://google.com", timeout=4)
    print('Проверка завершена успешно!')
except:
    print(
        f"{Fore.RED}[!] {Fore.MAGENTA}Вы не подключены к интернету \n пожалуйста проверте соединение с интернетом \n и запустите программу заново{Fore.RESET}"
    )
    time.sleep(1)
    sys.exit()
time.sleep(1)
print(Fore.YELLOW + 'Проверка Обновлений')
VERSION_URL = 'https://api.github.com/repos/POHel/The-word-cipher/releases/latest'
DOWNLOAD_URL = 'https://github.com/POHel/The-word-cipher/archive/refs/heads/main.zip'

def update_program(owner, repo, file):
    response = requests.get(VERSION_URL.format(owner=owner, repo=repo)).json()
    latest_version = response['tag_name']

    if latest_version >= version:
        print(Fore.MAGENTA + '[!]' + Fore.YELLOW + 'Доступно обновление')
        print(Fore.BLUE + 'Загружаю обновление')
        download_url = DOWNLOAD_URL.format(owner=owner, repo=repo, file=file)
        r = requests.get(download_url, allow_redirects=True)
        open(file, 'wb').write(r.content)
        print(Fore.MAGENTA + '[!]' + Fore.GREEN + 'Обновление Загружено')

    if latest_version <= version:
        print(Fore.MAGENTA + '[!]' + Fore.GREEN + 'Установлена самая последняя версия')

if __name__ == '__main__':
    update_program('POHel', 'The-word-cipher', 'main.zip')
time.sleep(1)

print(Fore.BLUE + 'Определяю OS...')
time.sleep(1)
print('Ваша ос: ', os.name)
time.sleep(3)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

while True:
    lang = input('RU or ENG? ')
    if lang == 'RU':
        whatru = input('расшифровка или шифровка? [1;2] ')
        if whatru == '1':
            encrypted_word = input("Введите зашифрованное слово: ")
            decryption_key = {'@': 'а', '%': 'б', '#': 'в', '&': 'г', '*': 'д', '^': 'е', '$': 'ё', '!': 'ж', '~': 'з',
                              '+': 'и', '=': 'й', '?': 'к', '<': 'л', '>': 'м', '|': 'н', '/': 'о', '≣': 'п', '`': 'р',
                              '-': 'с', '_': 'т', ':': 'у', ';': 'ф', '"': 'х', '[': 'ц', '{': 'ч', ']': 'ш', '√': 'щ', '✔': 'Ъ', '♟': 'ы', '☠': 'ь', '☣': 'э', '❄': 'ю', '☢': 'я'}
            decrypted_word = ''.join(
                [decryption_key[letter] if letter in decryption_key else letter for letter in encrypted_word])
            print("Расшифрованное слово:", decrypted_word)

        elif whatru == '2':
            word = input("Введите слово: ")  # Получаем слово от пользователя
            encryption_key = {'а': '@', 'б': '%', 'в': '#', 'г': '&', 'д': '*', 'е': '^', 'ё': '$', 'ж': '!', 'з': '~',
                              'и': '+', 'й': '=', 'к': '?', 'л': '<', 'м': '>', 'н': '|', 'о': '/', 'п': '≣', 'р': '`',
                              'с': '-', 'т': '_', 'у': ':', 'ф': ';', 'х': '"', 'ц': '[', 'ч': '{', 'ш': ']', 'щ': '√', 'Ъ': '✔', 'ы': '♟', 'ь': '☠', 'э': '☣', 'ю': '❄', 'я': '☢'}
            encrypted_word = ''.join(
                [encryption_key[letter] if letter in encryption_key else letter for letter in word.lower()])
            print("Зашифрованное слово:", encrypted_word)

    elif lang == 'ENG':
        whateng = input('decoding or encryption? [1;2]')
        if whateng == '1':
            encrypted_word = input("Enter the encrypted word: ")
            decryption_key = {'@': 'a', '%': 'b', '#': 'c', '&': 'd', '*': 'e', '^': 'f', '$': 'g', '!': 'h', '~': 'i',
                              '+': 'j', '=': 'k', '?': 'l', '<': 'm', '>': 'n', '|': 'o', '/': 'p', '☢': 'q', '`': 'r',
                              '-': 's', '_': 't', ':': 'u', ';': 'v', '"': 'w', '[': 'x', '{': 'y', ']': 'z'}

            decrypted_word = ''.join(
                [decryption_key[letter] if letter in decryption_key else letter for letter in encrypted_word])

            print("The deciphered word:", decrypted_word)

        elif whateng == '2':
            word = input("Enter the word: ")
            encryption_key = {'a': '@', 'b': '%', 'c': '#', 'd': '&', 'e': '*', 'f': '^', 'g': '$', 'h': '!', 'i': '~', 'j': '+', 'k': '=', 'l': '?', 'm': '<', 'n': '>', 'o': '|', 'p': '/', 'q': '☢', 'r': '`', 's': '-', 't': '_', 'u': ':', 'v': ';', 'w': '"', 'x': '[', 'y': '{', 'z': ']'}

            encrypted_word = ''.join([encryption_key[letter] if letter in encryption_key else letter for letter in word.lower()])

            print("The encrypted word:", encrypted_word)
