from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Customer(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    email = models.EmailField(_("Email"), max_length=254)
    phone = models.IntegerField(_("Phone"))
    address = models.TextField(_("Address"), blank=True, null=True)


    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})
