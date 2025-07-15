import re

def normalize_phone(phone_number):
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())
    if cleaned.startswith("+380"):
        return cleaned
    elif cleaned.startswith("380"):
        return "+" + cleaned
    elif cleaned.startswith("0"):
        return "+38" + cleaned
    else:
        return cleaned # Or handle other cases as needed

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "   +38(050)123-32-34",
    "0502341234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

