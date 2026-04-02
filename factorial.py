# factorial.py
def factorial(n):
    """Calcul la factorielle d'un nombre n (avec validation)"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n doit être un entier positif")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Test rapide
if __name__ == "__main__":
    print(f"Factorial of 5 is {factorial(5)}") 