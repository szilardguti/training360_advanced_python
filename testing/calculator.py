class Calculator:
    def sum(self, a: int, b: int) -> int:
        return a + b

    def diff(self, a, b):
        return a - b

    def product(self, *nums):
        result = 1
        for num in nums:
            result *= num
        return result

    def power(self, base, exp):
        result = 1
        for _ in range(exp):
            result = self.product(result, base)
        return result
