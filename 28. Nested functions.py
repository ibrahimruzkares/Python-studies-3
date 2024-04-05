def total_multiplication(*args):
    def total(numbers):
        return sum(numbers)
    def multiplication(numbers):
        multiple = 1
        for i in numbers:
            multiple *= i
        return multiple
    return f"Total: {total(args)}, Multiple: {multiplication(args)}"

print(total_multiplication(1,2,3,4))