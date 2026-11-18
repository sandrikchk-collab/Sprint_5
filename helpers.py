import random
import string

from data import UserData


def generate_email():
    """Логин (email) в формате имя_фамилия_когорта_3цифры@домен."""
    digits = random.randint(100, 999)
    return f"{UserData.EMAIL_PREFIX}{digits}@{UserData.EMAIL_DOMAIN}"


def generate_password(length=8):
    """Пароль из букв и цифр. По умолчанию 8 символов (минимум для сайта — 6)."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))
