class DecimalToBinary:
    
    @staticmethod
    def convert(n: int) -> str:
        return bin(n)[2:]
        # return '{0:b}'.format(int(decimal_number))