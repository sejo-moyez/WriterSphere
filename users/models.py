from django.db import models
from django.contrib.auth.models import AbstractUser
#from orders.models import Order

# Create your models here.
class User(AbstractUser):
  ROLE_CHOICES =[
    ('admin', 'admin'),
    ('writer', 'writer')
  ]
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='writer')

  def __str__(self):
      return self.username

 
class Writer(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='writer_profile')
   bio = models.TextField(blank=True, null=True)
   hourly_rate= models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
   profile_picture =models.ImageField(upload_to='profiles/', blank=True, null=True)

   def __str__(self):
      return self.user.username





class Order(models.Model):
  STATUS_CHOICES = [
      ('pending','pending'),
      ('in_progress','in_progress'),
      ('completed','completed'),
      ('rejected','rejected'),
   ]
  writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
  title = models.CharField(max_length=255)
  description = models.TextField()
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
  deadline = models.DateTimeField()
  submitted_at = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
     return self.title


class Invoice(models.Model):
   writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='invoices')
   order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name='invoices')
   amount = models.DecimalField(max_digits=8, decimal_places=2)
   issued_at = models.DateTimeField(auto_now_add=True)
   paid = models.BooleanField(default=False)

   def __str__(self):
      return f"Invoices for{self.writer.user.username} on {self.order.title}"
  

class Report(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='reports')
    content = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.writer.user.username}"


class Fine(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='fines')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='fines')
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    reason = models.CharField(max_length=255)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fine for {self.writer.user.username} on {self.order.title}"