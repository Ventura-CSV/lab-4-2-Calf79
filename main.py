def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    for i in range(1,6):
        num = int(input(f'number:+'))
        total +=  num
        print(total)
    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
