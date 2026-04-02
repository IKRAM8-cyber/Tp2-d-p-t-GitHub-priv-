# sum_list.py
def sum_list(numbers):
    """Calcule la somme des nombres dans une liste"""
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("Tous les éléments doivent être des nombres")
    return sum(numbers)

# Test rapide
if __name__ == "__main__":
    print(sum_list([1, 2, 3, 4]))
