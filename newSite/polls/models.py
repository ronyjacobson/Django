import datetime

from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
    	return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
# list_display propetries:

    # Will order by date when trying to sort by recently published
    was_published_recently.admin_order_field = 'pub_date'
    # Will show a true/false icon
    was_published_recently.boolean = True
     # Will change the title of the field
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
    	return self.choice_text