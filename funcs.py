import random,string

class Genrate_Password:
    def __init__(self, lenght=12, use_upper=True, use_Digits=True, use_Special=True):
        self.lenght = lenght
        self.use_upper = use_upper
        self.use_Digits = use_Digits
        self.use_Special = use_Special

    def generate_password(self):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase if self.use_upper else ''
        digits = string.digits if self.use_Digits else ''
        special = string.punctuation if self.use_Special else ''

        p = lower + upper + digits + special

        password = ''.join(random.choice(p) for _ in range(self.lenght)) 
        

        if not all:
            return 'Error: No characters to choose from'


        return password


    def save_Password(self, password):
        with open('password.txt', 'a') as file:
            file.write(password)

        return 'Password saved to password.txt'