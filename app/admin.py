from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Journal, JournalCategory, InfoSendJournal,Articles,Journal

@admin.register(JournalCategory)
class CategoryTranslationAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(InfoSendJournal)
class InfoSendJournalTranslationAdmin(TranslationAdmin):
    list_display = ("title",)
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(Journal)
class JournalTranslationAdmin(TranslationAdmin):
    list_display = ('name',)


admin.site.register(Articles)