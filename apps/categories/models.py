from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(
        unique=True,
        max_length=255,
        verbose_name='Наименование'
    )
    slug = models.SlugField(
        max_length=100
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True, blank=True
    )

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return f"{self.title}"
