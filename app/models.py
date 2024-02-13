from django.db import models
import os
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
# Create your models here.
from django.db import models

class JournalCategory(models.Model):
    name = models.CharField(max_length=255)
    images = models.ImageField()
    info = RichTextField()

    def __str__(self):
        return self.name

class Journal(models.Model):
    name = models.CharField(max_length=255)
    journal_category = models.ForeignKey(JournalCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='journals/', validators=[FileExtensionValidator(allowed_extensions=['doc','pdf','docx','rtf'])])
    images = models.ImageField()
    upload_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

class InfoSendJournal(models.Model):
    title = models.CharField(max_length=255, verbose_name="")
    body = RichTextField()
    journal_category = models.ForeignKey(JournalCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Articles(models.Model):
    TYPE = (
    ("maqola", "Maqola"),
    ("tezis", "Tezis"),
    
)
    title_art = models.CharField(max_length=255)
    journal_category = models.ForeignKey(Journal, on_delete=models.CASCADE)
    abstract = models.TextField(help_text='Annotatsiya')
    Keywords = models.TextField(help_text='Kalit sozlar')
    type_art =  models.CharField(max_length=50, choices=TYPE,default='maqola')
    author_1 = models.CharField(max_length=255, null=True, blank=True)
    info_auth1= models.TextField(null=True, blank=True)
    author_2 = models.CharField(max_length=255, null=True, blank=True)
    info_auth2= models.TextField(null=True, blank=True)
    author_3 = models.CharField(max_length=255, null=True, blank=True)
    info_auth3= models.TextField(null=True, blank=True)
    author_4 = models.CharField(max_length=255, null=True, blank=True)
    info_auth4= models.TextField(null=True, blank=True)
    create_data = models.DateField()
    firs_page = models.IntegerField(help_text='Birinchis sahifa')
    last_page = models.IntegerField(help_text='Oxirgi sahifa')
    count_page = models.IntegerField(help_text='Maqola sahifalar soni')
    file_articles = models.FileField(upload_to='Articles/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['doc','pdf','docx','rtf'])])
    
    def __str__(self):
        return f"{self.title_art} \n {self.journal_category.name}"