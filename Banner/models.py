from django.db import models

class Banner(models.Model):
    banner1 = models.BinaryField(null=True, blank=True)
    banner2 = models.BinaryField(null=True, blank=True)
    banner3 = models.BinaryField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'collegebanner'

    def __str__(self):
        return f"Banner {self.id} - {self.uploaded_at}"

class HomeImage(models.Model):
    college_home = models.BinaryField(null=True, blank=True)
    intern_home = models.BinaryField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'homeimage'

    def __str__(self):
        return f"HomeImage {self.id} - {self.uploaded_at}"
    
class Events_update(models.Model):
    
    events = models.BinaryField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'eventsimage'

    def __str__(self):
        return f"Events_update {self.id} - {self.uploaded_at}"