
from gtts import gTTS
import os
import inquirer

# filename = "answer"

filename = input("Enter your file name: ")

# What you would like the voice to say
text = "Greetings, You have reached the voicemail of Brandon King. Sorry I could not answer your call... Please leaves a message after the beep."

# Different languages offered
languages = [
    # Chinese
    'zh-cn',
    'zh-tw',
    # English
    'en',
    'en-ca',
    'en-uk',
    'en-gb',
    'en-au',
    'en-gh',
    'en-in',
    'en-ie',
    'en-nz',
    'en-ng',
    'en-ph',
    'en-za',
    'en-tz',
    # French
    'fr-ca',
    'fr-fr',
    # Portuguese
    'pt-br',
    'pt-pt',
    # Spanish
    'es-es',
    'es']

questions = [
    inquirer.List('text',
                  message="What language?",
                  choices=languages,
                  ),
]
answers = inquirer.prompt(questions)

#print(answers['text'])

lang = answers['text']

speech = gTTS(text, lang)

# Name of directory where you would like to save the file
os.chdir('/Users/brandonking/Desktop')
# Save as "mp3" file
speech.save(filename + ".mp3")