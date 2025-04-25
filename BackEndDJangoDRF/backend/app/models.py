from django.db import models

class InvestmentFund(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=50)
    quota_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.ticker})"

class Transaction(models.Model):
    FUND_OPERATION_CHOICES = (
        ('aporte', 'Aporte'),
        ('resgate', 'Resgate'),
    )
    fund = models.ForeignKey(InvestmentFund, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=FUND_OPERATION_CHOICES)

    def __str__(self):
        return f"{self.type.capitalize()} - {self.value} - {self.date}"
