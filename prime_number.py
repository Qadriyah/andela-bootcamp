class PrimeNumber():

    def generate_prime_number(self, n):
        try:
            if n < 0:
                return "Only positive integers allowed"
            if n == 2 or n == 3:
                return n
            flag = 0
            for i in range(2, n):
                if n % i == 0:
                    flag = 1
                    break
            if flag == 0 and n > 1:
                return n
            else:
                return "Not prime number"
        except TypeError:
            raise "Not integer"