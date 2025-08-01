from django.db import models

# Create your models here.
class CaseQueryLog(models.Model):
    case_type = models.CharField(max_length=10)
    case_number = models.CharField(max_length=20)
    filing_year = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    status = models.CharField(max_length=20, choices=[('success', 'Success'), ('failed', 'Failed')])
    error_message = models.TextField(blank=True, null=True)
    raw_response = models.TextField()  # Store full HTML or JSON response here

    def __str__(self):
        return f"{self.case_type} {self.case_number}/{self.filing_year} at {self.timestamp}"