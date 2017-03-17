from django.db import models, IntegrityError
from django.conf import settings
from uuid import uuid4


class Meme(models.Model):
    class Meta:
        app_label = 'memerator'
        
    id = models.CharField(max_length=10, primary_key=True) 
    template = models.CharField(max_length=30)
    text = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid4().hex[:8]

        while True:
            try:
                return super(Meme, self).save(*args, **kwargs)
            except IntegrityError:
                self.id = uuid.uuid4().hex[:8]