from .models import JournalCategory

def journal_categories(request):
    categories = JournalCategory.objects.all()
    return {'journal_categories': categories}
