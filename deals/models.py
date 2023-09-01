# from django.db import models
# from django.utils import timezone
# from django.conf import settings


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Post(models.Model):

#     class PostObjects(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset() .filter(status='published')

#     options = (
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#     )

#     category = models.ForeignKey(
#         Category, on_delete=models.PROTECT, default=1)
#     title = models.CharField(max_length=250)
#     excerpt = models.TextField(null=True)
#     content = models.TextField()
#     slug = models.SlugField(max_length=250, unique_for_date='published')
#     published = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
#     status = models.CharField(
#         max_length=10, choices=options, default='published')
#     objects = models.Manager()  # default manager
#     postobjects = PostObjects()  # custom manager

#     class Meta:
#         ordering = ('-published',)

#     def __str__(self):
#         return self.title


from django.db import models

class Deal(models.Model):
    when = models.DateField()
    company = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    funding_round = models.CharField(max_length=255)
    investors = models.TextField()
    source = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    company_slug = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    publish = models.CharField(max_length=1, blank=True, null=True)
    valuation_note = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    quarter = models.CharField(max_length=45, blank=True, null=True)
    selected_country = models.CharField(max_length=45, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'investments'