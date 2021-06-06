from notion.block import PageBlock, ToggleBlock, TextBlock, AudioBlock
from notion.client import NotionClient
import requests


def get_source(source):
    josancamon19_key = 'da7db07ed41248e9b00d581ea74b10a4d97f4c2429c9d7b8d6c12f1dac4e15f0ef727af4b268a988b324d1fe95b5b09028a344d7bc041c165791682eefaf221a4534503b581e7c0b77efab0edb51'
    karen_key = 'd0b67a64f32f568b93d6c323dcd262c21a7e1fc18a9b9bdab1501479b3cbcf90b6a7f7338cbc2dd9bf17983e87c76fc5a5e18920f993dc544ebd5a09b3e3312f61ad7f6c9b62d565cc4c7e8243c9'
    client = NotionClient(token_v2=karen_key)
    page = client.get_block(source)
    return page


def write_toggle(source_text, translated_text, file_path, page, extra_text=''):
    try:
        toggle = page.children.add_new(ToggleBlock, title=source_text)
        print(f'Wrting {source_text} --> {translated_text}')
        try:
            toggle.children.add_new(TextBlock, title=translated_text)
            if extra_text:
                toggle.children.add_new(TextBlock, title=extra_text)
            audio_block = toggle.children.add_new(AudioBlock)
            audio_block.upload_file(file_path)
        except requests.exceptions.HTTPError as e:
            print('Error', e)
            toggle.remove()
            return False
        return True
    except requests.exceptions.HTTPError:
        print('Notion error writing, trying again')
        return False
