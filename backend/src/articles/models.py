from django.db import models

class article(models.Model):
        title =models.CharField(max_length=50)
        content =models.TextField()
        description=models.TextField()

        def __str__(self):
                return self.title
