from django.db import models

# model for IPO information
class IPO(models.Model):
    company_name = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='company_logos/')
    price_band = models.CharField(max_length=50)
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=50)
    listing_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Open', 'Open'), ('Closed', 'Closed')])
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_gain = models.DecimalField(max_digits=10, decimal_places=2)
    current_market_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_return = models.DecimalField(max_digits=10, decimal_places=2)
    rhp_pdf = models.FileField(upload_to='rhps/')
    drhp_pdf = models.FileField(upload_to='drhps/')
    
    def __str__(self):
        return self.company_name
