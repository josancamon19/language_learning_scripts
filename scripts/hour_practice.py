from gtts import gTTS
import utils
from playsound import playsound
import random
import time
import datetime


def random_time():
    hour = random.randint(0, 12)
    minute = random.randint(1, 59)
    part = ['AM', 'PM'][random.randint(0, 1)]
    rand_hour = f'{hour}:' + (f'{minute}'.rjust(2, '0')) + f' {part}'
    return rand_hour


def execute_script(practice_type=0, wait_time=3.0):
    while True:
        rand_time = random_time()
        file = utils.audio.generate_fr_audio(rand_time)
        if practice_type == 0:
            playsound(f'../audios/{file}')
            time.sleep(wait_time)
            print(rand_time)
        elif practice_type == 1:
            print(rand_time)
            time.sleep(wait_time)
            playsound(f'../audios/{file}')
        else:
            break


if __name__ == '__main__':
    execute_script(practice_type=1, wait_time=5)