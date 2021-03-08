from google.cloud import translate


def fr_to_en(text="YOUR_TEXT_TO_TRANSLATE", project_id="notion-duolingo"):
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"
    
    # noinspection PyTypeChecker
    response = client.translate_text(request={
        "parent": parent,
        "contents": [text],
        "mime_type": "text/plain",
        "source_language_code": "fr",  # change the source language as needed
        "target_language_code": "en-US",  # change the target language as needed
    }
    )
    
    if response.translations:
        return response.translations[0].translated_text
    return text
