class Matrix:
    def __init__(self, a, b, c, d):
        self.dim = 2
        self.values = ((a, b), (c, d))

    def add(self, rhs):
        newA = self.values[0][0] + rhs.values[0][0]
        newB = self.values[0][1] + rhs.values[0][1]
        newC = self.values[1][0] + rhs.values[1][0]
        newD = self.values[1][1] + rhs.values[1][1]
        return Matrix(newA, newB, newC, newD)

    def multip(self, rhs):
        if self.dim != rhs.dim:
            print ("Matrices can not be multiplied! \n")
            return

        newA = self.values[0][0] * rhs.values[0][0] + self.values[0][1] * rhs.values[1][0]
        newB = self.values[0][0] * rhs.values[0][0] + self.values[0][1] * rhs.values[1][1]
        newC = self.values[1][0] * rhs.values[0][0] + self.values[1][1] * rhs.values[1][0]
        newD = self.values[0][1] + rhs.values[0][0] + self.values[0][1] + rhs.values[1][1]
        return Matrix(newA, newB, newC, newD)

    def __str__(self):
        returnVal = []

        for i in self.values:
            temp = []
            temp.append(i[0])
            temp.append(i[1])

            returnVal.append(temp)
        return str(returnVal[0][0]) + ' ' + str(returnVal[0][1]) + '\n' + str(returnVal[1][0]) + ' ' + str(returnVal[1][1]) + '\n'


matr1 = Matrix(4, 5, 6, 7)
print (matr1)
matr2 = Matrix(2, 2, 2, 1)

print (matr2)

matr3 = matr1.add(matr2)
print(matr3)

matr4 = matr1.multip(matr2)

print(matr4)