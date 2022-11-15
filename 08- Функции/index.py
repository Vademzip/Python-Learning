def say_hello(username, age=24):
    """Функция приветствия пользователя"""
    print(f'hello {username}!')
    print(f'your age - {age}')


say_hello("Vitaliy", 21)
say_hello(username="Joe", age=14)
say_hello("Nick")

