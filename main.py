"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    for i in range(2,number):
        if number % i == 0:
            return False
    return True    


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    list = []
    if number == 1:
        return list
    if is_prime(number):
        list.append(number)
        return list
    else:
        n = 2
        while n <= number:
            if is_prime(n) and number % n == 0:
                list.append(n)
                number = number / n
            else:
                n += 1
        return list
