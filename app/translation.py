from modeltranslation.translator import register, TranslationOptions
from .models import JournalCategory,Journal,InfoSendJournal

@register(JournalCategory)
class JournalCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'info') 

@register(Journal)
class JournalTranslationOptions(TranslationOptions): 
    fields = ('name',)

@register(InfoSendJournal)
class  InfoSendJournalTranslationOptions(TranslationOptions):
    fields = ('title','body',)