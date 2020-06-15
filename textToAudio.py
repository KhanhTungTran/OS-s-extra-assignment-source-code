from gtts import gTTS   # vietnam's text to audio
from os import listdir

import os

folders = ['4Syllables', '5Syllables', '7Syllables', '10Syllables', '15Syllables', '20+Syllables']

for folder in folders:
    for textFile in listdir('./' + folder + '_vie'):
        if textFile.endswith('.txt'):
            f = open('./' + folder + '_vie' + '/' + textFile, 'r', encoding='utf-8')
            vietnameseAudio = gTTS(text = f.read(), lang = 'vi', slow = True)
            f.close()
            
            vietnameseAudio.save('./' + folder + '_vie' + '/' + textFile.split('.')[0] + '_slow' +'.mp3')
