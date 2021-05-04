from modeltranslation.translator import translator, TranslationOptions
from .models import HomePage

class HomePageTranslationOptions(TranslationOptions):
    fields = ('main_image_alt',
    'header',
    'about_us',
    'card_one',
    'card_one_description',
    'card_two',
    'card_two_description',
    'card_three',
    'card_three_description',
    'preporyka1',
    'preporyka2',
    'preporyka3'
    )

translator.register(HomePage, HomePageTranslationOptions)