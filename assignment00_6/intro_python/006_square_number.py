def main():
    print('** This Program is Providing a Square of the number **\n')
    num:float = float(input('\033[1;3m Enter a number to see its Square : \033[0m'))
    square = num ** 2
    print(f'\t\n \033[1;3m The square of {num} is {square}\033[0m')
if __name__ == "__main__":
    main()