from modeltranslation.translator import register, TranslationOptions
from .models import JournalCategory,Journal,InfoSendJournal,Articles

@register(JournalCategory)
class JournalCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'info') 

@register(Journal)
class JournalTranslationOptions(TranslationOptions): 
    fields = ('name',)

@register(InfoSendJournal)
class  InfoSendJournalTranslationOptions(TranslationOptions):
    fields = ('title','body',)


@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ('title_art','abstract','Keywords','author_1','info_auth1','author_2','info_auth2',
              'author_3','info_auth3','author_4','info_auth4'
              )