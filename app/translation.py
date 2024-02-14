from modeltranslation.translator import register, TranslationOptions
from .models import JournalCategory

@register(JournalCategory)
class JournalCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'info') 