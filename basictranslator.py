from googletrans import Translator

def translate_text(text,src_lang,dest_lang):
    translator=Translator()
    translated=translator.translate(text,src=src_lang,dest=dest_lang)
    return translated.text

src_text=input("Enter the text which you want to translate: ")
src_lang=input("Enter the source language: ")
dest_lang=input("Enter the destination language: ")
translated_text=translate_text(src_text,src_lang,dest_lang)
print("The translated text is",translated_text)