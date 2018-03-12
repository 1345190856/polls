from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """model admin class"""
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # fields = ['pub_date', 'question_text'] # customize order
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': 'collapse'}),
    ] # the first element of each tuple is title of the fieldset
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)