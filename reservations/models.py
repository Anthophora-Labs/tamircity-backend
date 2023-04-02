from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    second_phone_number = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='reservations', blank=True, null=True)
    # modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='modified_by', blank=True, null=True)

    slug = models.SlugField(unique=True, max_length=150, editable=False) # Editable ile buna hiç bi şekilde endpoint dahil ulasamaz ekleme tyapalaz gormez
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} {self.email} {self.created_date}"

    def get_slug(self):
        slug = slugify(self.full_name.replace("ı", "i"))
        unique_slug = slug
        counter = 1
        while Reservation.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.id:
            pass
            #self.created_date = timezone.now() ## run when created objects
        #self.updated_date = timezone.now() ## run when updated objects
        self.slug = self.get_slug()
        return super(Reservation, self).save(*args, **kwargs)