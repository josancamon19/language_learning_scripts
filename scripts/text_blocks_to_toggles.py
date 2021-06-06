from gtts import gTTS
from notion.block import TextBlock
import utils


def execute_script():
    source = 'https://www.notion.so/josancamon19/Jules-4-review-132169422bbb4fbe97599ee191acc1f3'
    source = 'https://www.notion.so/b5494a47374646f0b9ada8097f370a45'
    page = utils.notion.get_source(source)
    for text_block in filter(lambda x: isinstance(x, TextBlock) and x.title_plaintext, page.children):
        text = text_block.title
        print(text)
        translation = utils.translation.translate_text(text)
        audio_file = utils.audio.generate_target_audio(translation)
        utils.notion.write_toggle(text, translation, audio_file, page)


if __name__ == '__main__':
    execute_script()
