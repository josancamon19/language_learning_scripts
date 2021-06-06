from gtts import gTTS
import utils
from playsound import playsound
import random
import time
import datetime


def random_date():
    start_date = datetime.date(1900, 1, 1)
    end_date = datetime.date(2021, 4, 1)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def parsed_str_date():
    date_str = random_date().strftime("%d %B, %Y")
    if date_str[0] == '0':
        date_str = date_str[1:]
    return date_str


def execute_script(practice_type=0, wait_time=3.0):
    while True:
        date_str = parsed_str_date()
        file = utils.audio.generate_target_audio(date_str)
        if practice_type == 0:
            playsound(f'../audios/{file}')
            time.sleep(wait_time)
            print(date_str)
        elif practice_type == 1:
            print(date_str)
            time.sleep(wait_time)
            playsound(f'../audios/{file}')
        else:
            break


if __name__ == '__main__':
    execute_script(practice_type=1, wait_time=10)
