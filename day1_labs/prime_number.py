class PrimeNumber():

    def generate_prime_number(self, n):
        if n == 2 or n == 3:
            return n
        flag = 0
        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break
        if flag == 0 and n > 1:
            return n

'''
if __name__ == '__main__':
    objj = PrimeNumber()
    print(objj.generate_prime_number(1)) '''