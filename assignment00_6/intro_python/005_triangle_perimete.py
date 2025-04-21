def main():
    print('** This program is used to calculate the Perimeter of a Triangle **\n')
    side1 :float = float(input('\033[1;3m What is the length of side 1 ? \033[0m'))
    side2 :float = float(input('\033[1;3m What is the length of side 2 ? \033[0m'))
    side3 :float = float(input('\033[1;3m What is the length of side 3 ? \033[0m'))

    perimeter = side1 + side2 + side3
    print(f'\n\033[1;3mThe perimeter of the triangle is {perimeter} units \033[0m')
    
if __name__ == '__main__':
    main()