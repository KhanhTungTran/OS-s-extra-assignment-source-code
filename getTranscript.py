import speech_recognition as sr # enlish's audio to text
from os import listdir

from googletrans import Translator  # english to vietnamese
translator = Translator()

folders = ['4Syllables', '5Syllables', '7Syllables', '10Syllables', '15Syllables', '20+Syllables']
r = sr.Recognizer()

for folder in folders:
    for audioFileDir in listdir('./' + folder):
        if audioFileDir.endswith('.wav'):
            audioFileSource = sr.AudioFile('./' + folder + '/' +audioFileDir)
            with audioFileSource as source:
                audio = r.record(source)
                englishResult = r.recognize_google(audio)
                f = open('./' + folder + '/' + audioFileDir.split('.')[0] + '.txt', 'x')
                f.write(englishResult)
                f.close()

                vietnameseResult = translator.translate(englishResult, src='en', dest ='vi')
                f = open('./' + folder + '_vie' + '/' + audioFileDir.split('.')[0] + '.txt', 'x', encoding='utf-8')
                f.write(vietnameseResult.text)
                f.close()