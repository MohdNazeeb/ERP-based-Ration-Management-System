from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, card_number, password=None, **extra_fields):
        if not card_number:
            raise ValueError("Card Number is required")
        user = self.model(card_number=card_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)  # was self.db, fix to self._db
        return user

    def create_superuser(self, card_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(card_number, password, **extra_fields)
