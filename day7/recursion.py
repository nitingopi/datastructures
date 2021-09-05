class Recursion:
    def __init__(self):
        pass

    def factorialWithRecursion(self, value:int ) -> int:
        if value == 0:
            return 1

        return value * self.factorialWithRecursion(value-1)


recursion = Recursion()
result = recursion.factorialWithRecursion(5)
print(result)            