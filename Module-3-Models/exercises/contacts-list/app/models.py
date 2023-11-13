from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_favorite = models.BooleanField(default=False)


def create_contact(name, email, phone, is_favorite):
    contact = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    contact.save()
    return contact


def delete_contact(name):
    Contact.objects.filter(name=name).delete()


def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except Contact.DoesNotExist:
        return None


def update_contact_email(name, new_email):
    contact = find_contact_by_name(name)
    if contact:
        contact.email = new_email
        contact.save()


def all_contacts():
    return list(Contact.objects.all())


def favorite_contacts():
    return list(Contact.objects.filter(is_favorite=True))
