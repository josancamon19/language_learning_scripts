from gtts import gTTS
import utils
from playsound import playsound
import random
import time


def build_audio_files():
    for i in range(101):
        utils.audio.generate_target_audio(f'{i}', 'number-')


def execute_script(from_number=0, to_number=100, practice_type=0, wait_time=3.0):
    numbers = list(range(from_number, to_number + 1))
    while True:
        rand_number_id = random.randint(0, len(numbers))
        rand_number = numbers[rand_number_id]
        if practice_type == 0:
            playsound(f'../audios/number-{rand_number}.mp3')
            time.sleep(wait_time)
            print(f'Number is {rand_number}')
        elif practice_type == 1:
            print(f'Number {rand_number}')
            time.sleep(wait_time)
            playsound(f'../audios/number-{rand_number}.mp3')
        
        del numbers[rand_number_id]


if __name__ == '__main__':
    execute_script(practice_type=1, wait_time=2.5)