def main():
    numbers = [[11, 12, 13, 14, 15],
               [21, 22, 23, 24, 25],
               [31, 32, 33, 34, 35]]

    rownum = int(input('Enter the row num: '))
    ##################################################
    # Comlete your code here
    ##################################################


if __name__ == '__main__':
    main()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_num = int(input("Enter a row number (0, 1, or 2): "))
row_sum = sum(matrix[row_num])
print("The summation of row", row_num, "is", row_sum)

