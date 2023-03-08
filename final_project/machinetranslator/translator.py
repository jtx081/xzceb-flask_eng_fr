'''Modules.'''
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


APIKEY='0v8HyvDk5Z_K5DDHrFL8Lv-AoxPx1zVblHJ-fRR-xzgp'
URL='https://api.us-east.language-translator.watson.cloud.ibm.com/instances/2791865b-ac36-46d1-bc7e-badef22f7fc9'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    '''Convert english to french text.'''
    french_text= language_translator.translate(text=english_text,model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    '''Convert french to english text.'''
    english_text= language_translator.translate(text=french_text,model_id='fr-en').get_result()
    return english_text
