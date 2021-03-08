from gtts import gTTS
from notion.block import TextBlock
import utils


def execute_script():
    page = utils.notion.get_source("https://www.notion.so/josancamon19/Jules-1-review-e0d3beba5a5e41808948126b5a75be6b", )
    for text_block in filter(lambda x: isinstance(x, TextBlock) and x.title_plaintext, page.children):
        french = text_block.title
        audio_file = utils.audio.generate_fr_audio(french)
        english = utils.translation.fr_to_en(french)
        utils.notion.write_toggle(english, french, audio_file, page)


if __name__ == '__main__':
    execute_script()
