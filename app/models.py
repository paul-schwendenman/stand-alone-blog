from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(editable=False)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
	if not self.id:
	    self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    display_fields = ["title", "created", 'slug']

admin.site.register(Post, PostAdmin)