import uuid

from django.db import models

from api_auth.models import User, Profile


class Hood(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    hood_name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    occupants = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        User,
        related_name='assigned_user',
        on_delete=models.DO_NOTHING
    )

    def save_hood(self):
        self.save()


class Business(models.Model):
    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    business_name = models.CharField(max_length=32)
    description = models.TextField(default="")
    business_email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_business(self):
        self.save()

    def delete_business(self):
        self.is_active = False
        self.save()

    @classmethod
    def get_active_set(cls):
        return cls.objects.filter(is_active=True)

    @classmethod
    def search_by_name(cls):
        return cls.objects.filter(business_name__icontains).all()


class Department(models.Model):
    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    department_name = models.CharField(max_length=32)
    description = models.TextField(default="")
    phone_number = models.CharField(max_length=16)
    neighborhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def save_department(self):
        self.save()

    @classmethod
    def get_active_set(cls):
        return cls.objects.filter(is_active=True)


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()