class PrimeNumber():

    '''
        This function has linear time complexity
        Respresented by N(O)
    '''

    def generate_prime_numbers(self, number):
        prime_numbers = []
        try:
            if number < 0:
                return "Only positive integers allowed"
            if number == 1:
                return 'Empty list of prime numbers'
            if number == 2:
                prime_numbers.append(number)
                return prime_numbers
            for x in range(number):
                flag = 0
                for i in range(2, x):
                    if x % i == 0 and x != 2:
                        flag = 1
                        break
                if flag == 0 and x > 1:
                    prime_numbers.append(x)
            return prime_numbers
        except TypeError:
            raise "Not integer"