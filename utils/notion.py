from notion.block import PageBlock, ToggleBlock, TextBlock, AudioBlock
from notion.client import NotionClient


def get_source(source):
    key = 'da7db07ed41248e9b00d581ea74b10a4d97f4c2429c9d7b8d6c12f1dac4e15f0ef727af4b268a988b324d1fe95b5b09028a344d7bc041c165791682eefaf221a4534503b581e7c0b77efab0edb51'
    client = NotionClient(token_v2=key)
    page = client.get_block(source)
    return page


def write_toggle(english, french, file_path, page, extra_text=''):
    try:
        toggle = page.children.add_new(ToggleBlock, title=english)
        print(f'Wrting {english} --> {french}')
        try:
            toggle.children.add_new(TextBlock, title=french)
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
