N = int(input("Вв ц число: "))


def compute_loops_in_digit_glyphs(n):
    s = str(n)
    result = 0
    for digit in s:
        if digit in ("0", "6", "9"):
            result += 1
        elif digit == "8":
            result += 2
    return result


K = compute_loops_in_digit_glyphs(N)
print(f"Кол-во замкнутых обл в знаках цифр: {K}")