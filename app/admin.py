from django.contrib import admin
from .models import Journal, JournalCategory, InfoSendJournal,Articles


class InfoSendJournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'journal_category')
    search_fields = ('title',)
    ordering = ('title',)


class JournalAdmin(admin.ModelAdmin):
    list_display = ('name', 'journal_category')
    search_fields = ('name',)
    ordering = ('name',)

class JournalCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(InfoSendJournal, InfoSendJournalAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(JournalCategory, JournalCategoryAdmin)
admin.site.register(Articles)