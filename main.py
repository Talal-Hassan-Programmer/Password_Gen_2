from funcs import Genrate_Password


def Main():
    length = int(input('Enter the length of the password: '))
    use_upper = input('Do you want to use uppercase letters? (y/n): ').lower() == 'y'
    use_digits = input('Do you want to use digits? (y/n): ').lower() == 'y'
    use_special = input('Do you want to use special characters? (y/n): ').lower() == 'y'

    password = Genrate_Password(length, use_upper, use_digits, use_special)

    print(f'Generated password: {password.generate_password()}')

    save = input('Do you want to save the password to a file? (y/n): ').lower() == 'y'

    if save:
        print(password.save_Password(password.generate_password()))



if __name__ == '__main__':
    Main()