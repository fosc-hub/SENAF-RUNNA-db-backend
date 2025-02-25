from django.db import models

class BaseHistory(models.Model):
    descripcion = models.TextField(null=True, blank=True)
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]

    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    by_user = models.ForeignKey(
        'customAuth.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.
        
    
    def __str__(self):
        return f"{self.action} - {self.timestamp} - {self.by_user} - {self.parent}"
