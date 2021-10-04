import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = language_translator.translate(
    text = textToTranslate,
    model_id = 'en-fr').get_result()
    translated_text = textToTranslate['translations'][0]['textToTranslate']
    return "Translated text to English " + translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = language_translator.translate(
    text = textToTranslate,
    model_id = 'fr-en').get_result()
    translated_text = textToTranslate['translations'][0]['textToTranslate']
    return "Translated text to English " + translated_text

@app.route("/")
def renderIndexPage():
    return render_template ('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)