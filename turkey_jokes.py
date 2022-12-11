import schedule
from time import sleep

from bot import send_to_channel
import config
import datetime


def send_to_channel_job():


    # date diff for counting
    today = datetime.date.today()
    first_day = datetime.date(2022, 12, 11)

    counter = (today - first_day).days
    days_till = 21 - counter
    jokes = [
        f"А я буду развлекать вас смешными шутками про индейку. Начнем: What key has legs and can't open a door? A "
        "tur-key.",
        f"Дней до нового года:{days_till}\nWhat's the best dance to do on Thanksgiving? The turkey trot.",
        f"Дней до нового года:{days_till}\nWhat do you call a turkey the day after Thanksgiving? Lucky!",
        f"Дней до нового года:{days_till}\nWhat side of a turkey grows more feathers? The outside!",
        f"Дней до нового года:{days_till}\nWhy did they let the turkey join the band? Because he had his own drumsticks.",
        f"Дней до нового года:{days_till}\nWhat do turkeys like to do on sunny days? Have peck-nics!",
        f"Дней до нового года:{days_till}\nWhy do turkeys lay eggs? Because if they dropped them, they would break.",
        f"Дней до нового года:{days_till}\nWhy did the turkey cross and then recross the road? To prove he wasn’t chicken.",
        f"Дней до нового года:{days_till}\nWhat do you call a ghost of a turkey? A poultry-geist.",
        f"Дней до нового года:{days_till}\nWhy did the turkey cross the road? He wanted people to think he was a chicken.",
        f"Дней до нового года:{days_till}\nFruit comes from a fruit tree, so where does turkey come from? A poul-tree.",
        f"Дней до нового года:{days_till}\nCan a turkey jump higher than a house? Yes, because houses can't jump!",
        f"Дней до нового года:{days_till}\nWhat’s the difference between a turkey and a chicken? Chickens celebrate Thanksgiving.",
        f"Дней до нового года:{days_till}\nWhat sound does a turkey’s phone make? Wing, wing! Wing, wing!",
        f"Дней до нового года:{days_till}\nWhat kind of weather does a turkey like? Fowl weather.",
        f"Дней до нового года:{days_till}\nWhat do turkeys give thanks for on Thanksgiving? Vegetarians.",
        f"Дней до нового года:{days_till}\nWhy did the turkey get detention? He used fowl language.",
    ]
    if counter <= len(jokes) :
        sent_message = jokes[counter]
        send_to_channel(text=sent_message, chat_id=config.turkey_chat_id)


schedule.every().day.at("15:05").do(send_to_channel_job)

while True:
    schedule.run_pending()
    sleep(1)
