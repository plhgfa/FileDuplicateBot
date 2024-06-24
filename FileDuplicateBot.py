import telebot

# Токен вашего бота
TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(TOKEN)

# Хранение информации о файлах
file_storage = {}

# Обработка входящих файлов
@bot.message_handler(content_types=['document'])
def handle_file(message):
    file = message.document
    file_name = file.file_name
    chat_id = message.chat.id
    message_id = message.message_id

    # Создаем ссылку на сообщение с файлом

    file_message_link = f'https://t.me/c/{str(chat_id)[4:]}/{message_id}'

    # Проверка наличия файла с таким же именем в словаре
    if file_name in file_storage:
        previous_links = file_storage[file_name]
        links = '\n'.join(previous_links)
        bot.send_message(айди вашего чата/группы, f'Файл с таким же именем уже существует.\n{links}')
        file_storage[file_name].append(file_message_link)
    else:
        file_storage[file_name] = [file_message_link]

# Запуск бота
bot.polling(non_stop=True)