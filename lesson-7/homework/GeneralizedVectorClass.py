from math import sqrt


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        result = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*result)

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        result = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(*result)

    def __mul__(self, other):
        if isinstance(other, Vector):
            # Dot product
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for the dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            # Scalar multiplication
            result = tuple(a * other for a in self.components)
            return Vector(*result)
        else:
            raise TypeError("Unsupported operand type for *: Vector and {}".format(type(other).__name__))

    def __rmul__(self, other):
        # Handles scalar multiplication where scalar is on the left
        return self.__mul__(other)

    def magnitude(self):
        return sqrt(sum(x ** 2 for x in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        result = tuple(a / mag for a in self.components)
        return Vector(*result)


# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("v1, v2 : ", v1, v2)  # Output: Vector(1, 2, 3)
v3 = v1 + v2
print("v1 + v2 = ", v3)  # Output: Vector(5, 7, 9)
v4 = v2 - v1
print(v4)  # Output: Vector(3, 3, 3)
dot_product = v1 * v2
print(dot_product)  # Output: 32
v5 = 3 * v1
print(v5)  # Output: Vector(3, 6, 9)
print(v1.magnitude())  # Output: 3.7416573867739413
v_unit = v1.normalize()
print(v_unit)  # Output: Vector(0.2672612419124244, 0.5345224838248488, 0.8017837257372732)
