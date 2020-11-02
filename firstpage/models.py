from django.db import models

class yes_of_first_page(models.Model):
    title = models.CharField(("Title"), max_length=50)
    confirmation = models.CharField(("Yes!!!"), max_length=10)
    