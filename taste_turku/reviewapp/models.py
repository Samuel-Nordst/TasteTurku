import jsonfield
from django.db import models

class Reviews(models.Model):
    review = models.CharField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # Corrected to __str__
        return self.review

class Restaurant(models.Model):
    location = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()  # Fixed typo: 'desription' -> 'description'
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'restaurants'

    def __str__(self):  # Corrected to __str__
        return f"{self.name}"
