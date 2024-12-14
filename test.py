@client.event
async def on_ready():
    print(f"Бот {client.user} успешно запущен!")
    send_message.start()  # Запускаем задачу для отправки сообщений

@tasks.loop(seconds=15)  # Указываем интервал в 15 секунд
async def send_message():
    channel = client.get_channel(CHANNEL_ID)  # Получаем объект канала
    if channel:
        # Упоминание пользователя
        await channel.send(f"<@{USER_ID}>, привет! Проверка работы бота.")
    else:
        print("Канал не найден. Проверьте ID.")

# Запуск бота
client.run(DISCORD_TOKEN)