from django.db import models

# Create your models here.


class Topics(models.Model):
    topic_name = models.CharField(max_length=200, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic_name
