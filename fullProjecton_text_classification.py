
import pyttsx3
import speech_recognition as sr
import wikipedia as wk
import webbrowser as wb
import os
engine  = pyttsx3.init ('sapi5')

engine.setProperty ('voice', voices [0].id)

def speak (audio):
    engine.say (audio)
    engine.runAndWait ()


def analysis(text):
    

def detect_language(text):
    # Set up your Google Cloud project credentials
    translate_client = translate.Client.from_service_account_json('path/to/your/credentials.json')

    # Detect the language of the text
    result = translate_client.detect_language(text)

    # Get the detected language code
    language_code = result['language']
    return language_code, text

def translated_language(text, lang_code):
    from googletrans import Translator
    def translate_hindi_to_english(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src=lang_code, dest='en')
    return translation.text

def takeCommand ():
    '''
    it takes microphone input
    '''
    print ('Please wait')
    r = sr.Recognizer ()
    with sr.Microphone() as source:
        print ('ask about anything')
        r.pause_threshold = 1
    try:
        print ('Recognizing')
        query = r.recognize_google (audio, language = 'en-in')
        print (f'user said: {query}')
        query = query.lower()
        
        text_data = query
        #left_direction = 'left'
        #right_direction = 'right'
        #forward_direction = 'forward'
        
       # if left_direction in query:
            #text_classification
        #elif right_direction in query:
            #t be done
        #elif forward_direction in query:
            #to be done
        #elif backward_direction in query:
            #to be done
        
#         if 'search' in query:
#             if 'search' in query: query = query.replace ('search', '')
#             elif 'open' in query: query = query.replace ('open', '')
#         elif 'the time' in query: 
#             search (query)
#         elif 'folder' in query:
#             lst = string.split ('')
#             i = lst.index ('folder')
#             try:
#                 searchString = lst [i - 1]
#                 if ('minor' in searchString) and ('major' in searchString) and 
#                 (('researchpaper') or ('research paper') in searchString):
#                     OpenFolder ('minor and major project research paper')
#                 elif 
                    
#             except:
# #         if query == 'wikipedia':
# #             results = wk.summary (query, sentences = 2)
# #             speak ('According to wikipedia')
# #             speak (results)
    lang_code, text = detect_language(text_data)
    translated_text = translated_language(text, lang_code)
    analysis(translated_text)
        
        
    except Exception as e:
        print (e)
        print ("Say that again please")
        return 'None'
    if query == 'pause':
        return 
    speak (query)
    return query

