import random
import string #содержит все возможные символы, которые могут быть использованы в пароле


#генерация пароля
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
