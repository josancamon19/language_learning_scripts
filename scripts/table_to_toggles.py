from notion.block import TextBlock
import utils


def execute_script():
    page = utils.notion.get_source("https://www.notion.so/josancamon19/Prepositions-5d5bcaad30dc481eb71151afb503d079", )
    table = utils.notion.get_source(
        "https://www.notion.so/josancamon19/037ed44dc9954d31b03467efae636267?v=fe91064fbde54798a1f20c82710980ee", )
    for row in table.collection.get_rows():
        french = row.french.replace('__', '')
        english = row.english
        comments = row.comments
        audio_file = utils.audio.generate_fr_audio(french, file_name_pre='preposition-')
        utils.notion.write_toggle(english, french, audio_file, page, extra_text=comments)


if __name__ == '__main__':
    execute_script()
