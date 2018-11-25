from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
