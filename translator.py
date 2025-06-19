from deep_translator import GoogleTranslator

# 3. Translate transcript to target language
def translate_text(text, target_lang, chunk_size=4000):
    print("[INFO] Translating text...")
    translated_chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        translated = GoogleTranslator(source='auto', target=target_lang).translate(chunk)
        translated_chunks.append(translated)
    return " ".join(translated_chunks)

