import discord
from discord.ext import tasks, commands
import random
import asyncio
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 697738721260339250
USER_IDS = [
    682238628147364043,
    485368001026195458,
    911187496237420575,
    398490899929235457,
    485440437520171029,
    364710509737541634
]

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


async def send_message_at_random_time():
    await bot.wait_until_ready()
    while True:
        random_hour = random.randint(0, 23)
        random_minute = random.randint(0, 59)

        now = datetime.now(timezone.utc)
        next_send_time = now.replace(hour=random_hour, minute=random_minute, second=0, microsecond=0)

        if next_send_time < now:
            next_send_time += timedelta(days=1)

        delay = (next_send_time - now).total_seconds()
        print(f"Следующее сообщение будет отправлено в: {next_send_time} (через {delay:.2f} секунд)")

        await asyncio.sleep(delay)

        random_user_id = random.choice(USER_IDS)
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            try:
                await channel.send(f"<@{random_user_id}>, привет, самое время понюхать свои пальцы")
            except Exception as e:
                print(f"Ошибка отправки сообщения: {e}")


@bot.event
async def on_ready():
    print(f"Bot {bot.user} готов к работе!")
    bot.loop.create_task(send_message_at_random_time())


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        random_responses = [
            "не отвлекай меня, я занят!",
            "что опять? 🙄",
            "привет-привет!",
            "как твои дела? 😊",
            "почему ты всегда зовёшь меня?",
            "эй, зачем тревожишь мой покой?"
            "пошел нахуй"
            "я не хочу болтать с тобой"
            "я тебя услышал, иди нахуй"
        ]
        response = random.choice(random_responses)
        await message.channel.send(f"<@{message.author.id}>, {response}")


bot.run(DISCORD_TOKEN)

