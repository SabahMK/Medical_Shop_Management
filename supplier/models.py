from django.db import models

from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Supplier(models.Model):
    contact_person = models.CharField(_("Contact Person"), max_length=150,  blank=True, null=True)
    company = models.CharField(_("Company"), max_length=50,  blank=True, null=True)
    phone = models.CharField(_("Phone Num"), max_length=15, blank=True, null=True)
    email = models.EmailField(_("Email"), max_length=254,  blank=True, null=True)
    address = models.TextField(_("Address"),  blank=True, null=True)

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return self.contact_person

    def get_absolute_url(self):
        return reverse("Supply_detail", kwargs={"pk": self.pk})
