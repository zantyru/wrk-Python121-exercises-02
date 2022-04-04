N = int(input("Вв ц число: "))


def compute_loops_in_digit_glyphs(n):
    s = str(n)
    result = 0

    mapping = {
        "0": 1, "6": 1, "8": 2, "9": 1,
    }

    for digit in s:
        result += mapping.get(digit, 0)

    return result


K = compute_loops_in_digit_glyphs(N)
print(f"Кол-во замкнутых обл в знаках цифр: {K}")