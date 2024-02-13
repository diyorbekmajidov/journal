from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from .models import JournalCategory, Journal,InfoSendJournal,Articles
from django.views.generic import DetailView,ListView


class JournalCategoryView(View):
    def get(self, request, *args, **kwargs):
        category_id = kwargs.get('category_id')
        journal_category = JournalCategory.objects.get(pk=category_id)
        journals = Journal.objects.filter(journal_category=journal_category)
        context = {
            'journal_category': journal_category,
             
        }
        return render(request, 'det_page/journal_category.html', context)


class ListJournalDetailView(DetailView):
    model = JournalCategory
    template_name = 'det_page/list_ar.html'

    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super(ListJournalDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['category_journals'] = Journal.objects.filter(journal_category_id=pk)
        return context


class InfoSendJournalDetailView(DetailView):
    model = InfoSendJournal
   
    template_name = 'det_page/infosend.html'
    context_object_name = 'journal_info'
    
    


class IndexListView(ListView):
    model = Journal
    template_name = 'index.html'
    context_object_name = 'journals'
    
    def get_queryset(self):
            # Get the last 6 journals
        return Journal.objects.all().order_by('-id')[:6]
    
class ArticlesListView(View):
    model =Articles
    # template_name = 'det_page/art_list.html'
    # context_object_name='list_arts'
    def get(self,request, **kwargs):
        category_id = kwargs.get('art_id')
        journal_category = Journal.objects.get(pk=category_id)
        list_arts = Articles.objects.filter(journal_category=category_id)
        context = {
            'list_arts': list_arts,
             'journal':journal_category
             
        }
        return render(request, 'det_page/art_list.html', context)

class Detail_articlsDetView(DetailView):
    model = Articles
    template_name = 'det_page/det_art.html'
    context_object_name = 'det_obj'







# def base(request):
#     return render(request, 'index.html')

def sign_in(request):
    return render(request, 'sign-in.html')

def about(request):
    return render(request, 'about-us.html')

def course_l(request):
    return render(request, 'course-list.html')

def course(request):
    return render(request, 'course.html')

def course_d(request):
    return render(request, 'course-details.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')