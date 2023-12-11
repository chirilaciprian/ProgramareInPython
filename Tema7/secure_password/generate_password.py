import random
import string
def create_password(length=12, use_special_chars=True, use_numbers=True, use_mixed_case=True):
    characters = string.ascii_letters if use_mixed_case else string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Check if the requested length is valid
    if length < 1:
        raise ValueError("Password length must be greater than or equal to 1")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password