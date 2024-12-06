from django.db import models

# Library Model
class Library(models.Model):
    library_id = models.AutoField(primary_key=True)
    library_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.library_name


# Member Model
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Staff Model
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='books/covers/')
    isbn = models.CharField(max_length=13, unique=True)
    copies_available = models.PositiveIntegerField()

    def __str__(self):
        return self.title

from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, help_text="Title of the event")
    description = models.TextField(help_text="Detailed description of the event")
    date = models.DateField(help_text="Date of the event")
    time = models.TimeField(help_text="Time of the event")
    location = models.CharField(max_length=255, help_text="Location of the event")
    organizer = models.CharField(max_length=255, help_text="Name of the event organizer")
    cover_image = models.ImageField(
        upload_to='events/covers/', 
        blank=True, 
        null=True, 
        help_text="Optional image for the event"
    )
    is_free = models.BooleanField(default=True, help_text="Is the event free to attend?")
    
    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        ordering = ['date', 'time']
        verbose_name = "Event"
        verbose_name_plural = "Events"

# Transaction Model
class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Transaction {self.transaction_id}"


# Reservation Model
class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("Completed", "Completed")])
    pickup_deadline = models.DateField()

    def __str__(self):
        return f"Reservation {self.reservation_id}"


