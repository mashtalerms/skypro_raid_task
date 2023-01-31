from django.db import models
from django.utils.translation import gettext_lazy as _


class FrameworkModel(models.Model):
    # pk = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = _("Фреймворк")
        verbose_name_plural = _("Фреймворки")
        ordering = ["id"]

    def __str__(self):
        return self.name

# FrameworkModel.objects.create(name="React", language="Javascript")
# FrameworkModel.objects.create(name="Vue", language="Javascript")
# FrameworkModel.objects.create(name="FastApi", language="Python")
# FrameworkModel.objects.create(name="Laravel", language="PHP")
# FrameworkModel.objects.create(name="Spring", language="Java")