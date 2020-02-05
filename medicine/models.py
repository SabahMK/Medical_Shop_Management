from django.db import models
from django.utils.translation import ugettext as _
from customer.models import Customer
# from employee.models import Bill

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    customer = models.ForeignKey(Customer, verbose_name=_("Get") ,related_name="meds", on_delete=models.CASCADE)
    # bill = models.ForeignKey(Bill, verbose_name=_("Bill"), on_delete=models.CASCADE)
    quantity =  models.IntegerField(_("Quantity"))
    weight = models.CharField(_("Weight"), blank=True, null=True, max_length=50)
    price = models.IntegerField(_("Price"))
    mfd = models.DateField(_("Manufactured on"), auto_now=False, auto_now_add=False)
    exp = models.DateField(_("Expires on"), auto_now=False, auto_now_add=False)
    mfd_by=  models.CharField(_("Manufactured by"), blank=True, null=True, max_length=50)
    placed_at = models.CharField(_("Placed at"), max_length=40, blank=True, null=True)
    contains = models.CharField(_("Contains"), max_length=40, blank=True, null=True)
    body = models.TextField(_("Body"),blank=True, null=True, max_length=500)
    

    class Meta:
        verbose_name = _("Medicine")
        verbose_name_plural = _("Medicines")

    def __str__(self):
        return f'{self.name}'
            