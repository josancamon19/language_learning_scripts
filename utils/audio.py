from gtts import gTTS
import os


def generate_target_audio(text, file_name_pre=''):
    if len(text) < 10:
        file_name = text.replace(' ', '')
    else:
        file_name = text[:10].replace(' ', '')
    
    file_name = f'audios/{file_name_pre}{file_name}.mp3'
    
    tts_fr = gTTS(text, lang='en')
    tts_fr.save(file_name)
    return file_name
