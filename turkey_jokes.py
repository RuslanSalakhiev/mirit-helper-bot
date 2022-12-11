import schedule
from time import sleep

from bot import send_to_channel
import config
import datetime


def send_to_channel_job():
    jokes = [
        "А я буду развлекать вас смешными шутками про индейку. Начнем: What key has legs and can't open a door? A "
        "tur-key.",
        "What's the best dance to do on Thanksgiving? The turkey trot.",
        "What do you call a turkey the day after Thanksgiving? Lucky!",
        "What side of a turkey grows more feathers? The outside!",
        "Why did they let the turkey join the band? Because he had his own drumsticks.",
        "What do turkeys like to do on sunny days? Have peck-nics!",
        "Why do turkeys lay eggs? Because if they dropped them, they would break.",
        "Why did the turkey cross and then recross the road? To prove he wasn’t chicken.",
        "What do you call a ghost of a turkey? A poultry-geist.",
        "Why did the turkey cross the road? He wanted people to think he was a chicken.",
        "Fruit comes from a fruit tree, so where does turkey come from? A poul-tree.",
        "Can a turkey jump higher than a house? Yes, because houses can't jump!",
        "What’s the difference between a turkey and a chicken? Chickens celebrate Thanksgiving.",
        "What sound does a turkey’s phone make? Wing, wing! Wing, wing!",
        "What kind of weather does a turkey like? Fowl weather.",
        "What do turkeys give thanks for on Thanksgiving? Vegetarians.",
        "Why did the turkey get detention? He used fowl language.",
    ]

    # date diff for counting
    today = datetime.date.today()
    first_day = datetime.date(2022, 12, 11)

    counter = (today - first_day).days

    if counter <= len(jokes) :
        sent_message = jokes[counter]
        send_to_channel(text=sent_message, chat_id=config.turkey_chat_id)


schedule.every().day.at("16:46").do(send_to_channel_job)

while True:
    schedule.run_pending()
    sleep(1)
