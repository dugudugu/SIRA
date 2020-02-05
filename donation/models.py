from django.db import models
import datetime


# Model to store all donation location with the amount and date
class DonationInformation(models.Model):
    country = models.CharField(max_length=40, blank=False)
    amount_donated = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField(default=datetime.date.today, null=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.country, self.amount_donated, self.date)

# Model to store all information about each donation
class Donation(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=40, blank=False)
    email = models.CharField(max_length=100, blank=False)
    date = models.DateField(default=datetime.date.today, null=True)
    donation = models.DecimalField(max_digits=9, decimal_places=2, default='5.00')
    minDonation = models.DecimalField(max_digits=9, decimal_places=2, default='5.00')

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)  
        
# Model to store individual donations
class DonationLineItem(models.Model):
    donation_information = models.ForeignKey(DonationInformation, on_delete=models.CASCADE)
    donations = models.ForeignKey(Donation, on_delete=models.PROTECT)
    amount = models.IntegerField(blank=False)

    def __str__(self):
      return "{0} {1} @ {2}".format(self.amount, self.donations.full_name, self.donations.donation)  

