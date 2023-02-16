from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to='portfolio/images/',blank=True)
    url = models.URLField(blank=True)
    github_repo = models.URLField(blank=True)
    descriptoin = models.TextField()
    data = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
