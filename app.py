from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    output = ""
    sentence = ""
    source_lang = ""
    destination_lang = ""
    pronunciation = ""

    if request.method == 'POST':
        sentence = request.form.get('sentence')
        language = request.form.get('inputvalue')

        if sentence and language:  # Check if sentence and language are not empty
            try:
                translator = Translator()
                translation = translator.translate(sentence, dest=language)
                source_lang = translation.src
                destination_lang = translation.dest
                pronunciation = translation.pronunciation if translation.pronunciation else "No pronunciation available"
                output = translation.text
            except Exception as e:
                output = f"Translation Error: {str(e)}"

    return render_template('home.html', output=output, sentence=sentence, source_lang=source_lang,
                           destination_lang=destination_lang, pronunciation=pronunciation)

if __name__ == '__main__':  # Corrected the main block condition
    app.run(debug=True)



    
    


