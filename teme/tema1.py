import math

# 1. Suma numerelor de la 1 la 100
def sum_1_to_100():
    return sum(range(1, 101))

# 2. Afisarea primelor 20 de numere impare
def first_20_odd_numbers():
    return [num for num in range(2, 40, 2)]

# 3. Cel mai mare divizor comun pentru 2 numere citite de la tastatura
def greatest_common_divisor(num1, num2):
    return math.gcd(num1, num2)

# 4. Afisati daca un numar citit de la tastatura este prim
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 5. Afisati suma si media unei liste de numere citite de la tastatura
def sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

# 6. Se citesc 3 numere de la tastatura, verificati daca acestea pot reprezenta unghiurile unui triunghi
def is_triangle(angle1, angle2, angle3):
    return angle1 + angle2 + angle3 == 180

# 7. Sortati o lista de elemente citite de la tastatura, folosind orice metoda de sortare doriti (nu functia sort)
def bubble_sort(elements):
    for i in range(len(elements)):
        for j in range(0, len(elements) - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements

# 8. Scrieti un program care afiseaza ziua saptamanii pentru un numar citit de la tastatura (de la 1 la 7) unde  1=luni , 7 = duminica
def day_of_week(day_num):
    days_of_week = {
        1: "Luni",
        2: "Marti",
        3: "Miercuri",
        4: "Joi",
        5: "Vineri",
        6: "Sambata",
        7: "Duminica"
    }
    return days_of_week.get(day_num, "Invalid input")

# 9. Afisati maximul dintr-un vector de elemente citit de la tastatura
def max_in_list(elements):
    return max(elements)

# 10. Rezolvati ecuatia de gradul al doilea
def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"{real_part} ± {imaginary_part}i"

# Example usage:
print("#1 Suma numerelor de la 1 la 100:", "\033[92m" + str(sum_1_to_100()) + "\033[0m")
print("#2 Afisarea primelor 20 de numere impare:", first_20_odd_numbers())
print("#3 Cel mai mare divizor comun pentru 2 numere citite de la tastatura:", greatest_common_divisor(48, 18))
print("#4 Afisati daca un numar citit de la tastatura este prim", is_prime(29))
print("#5 Afisati suma si media unei liste de numere citite de la tastatura:", sum_and_average([10, 20, 30, 40]))
print("#6 Se citesc 3 numere de la tastatura, verificati daca acestea pot reprezenta unghiurile unui triunghi", is_triangle(60, 60, 60))
print("#7 Sortati o lista de elemente citite de la tastatura, folosind orice metoda de sortare doriti (nu functia sort):", bubble_sort([34, 23, 67, 100, 88, 2]))
print("#8 Scrieti un program care afiseaza ziua saptamanii pentru un numar citit de la tastatura (de la 1 la 7) unde  1=luni , 7 = duminica:", day_of_week(7))
print("#9 Afisati maximul dintr-un vector de elemente citit de la tastatura:", max_in_list([3, 67, 23, 45, 89]))
print("#10 Rezolvati ecuatia de gradul al doilea 1x^2 -5x + 6 = 0:", solve_quadratic(1, -5, 6))