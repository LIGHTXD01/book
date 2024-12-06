from django.contrib import admin
from .models import Library, Member, Staff, Book, Transaction, Reservation,Event

admin.site.register(Library)
admin.site.register(Member)
admin.site.register(Staff)
admin.site.register(Book)
admin.site.register(Transaction)
admin.site.register(Reservation)
admin.site.register(Event)
