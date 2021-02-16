'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
'''


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:

    def __init__(self, matrix):

        self.matrix = matrix

    def __str__(self):

        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])
        #return f"{[([(print(self.matrix[i][j], end=' ')) for j in range(len(self.matrix[i]))], print()) for i in range(len(self.matrix))]}"

    def __len__(self):

        return len(self.matrix)

    #def __getitem__(self, item):

        #return self[item]

    def __add__(self, other):

        if len(self.matrix) == len(other.matrix):
            lenght = len(self.matrix[0])
            for row in self.matrix:
                if len(row) != lenght:
                    raise MatrixError(self, other)
            for row2 in other.matrix:
                if len(row2) != lenght:
                    raise MatrixError(self, other)
            result = []
            numbers = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    summa = other.matrix[i][j] + self.matrix[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.matrix[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)


mat = Matrix([[4, 2, 3], [5, 2, 3]])
print(mat)
mat2 = Matrix([[4, 2, 3], [5, 2, 3]])
#res_sum = mat + mat2

print(mat + mat2)

