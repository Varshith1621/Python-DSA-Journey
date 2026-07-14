class Solution(object):
    def subtractProductAndSum(self, n):
        sum_digit = 0
        product_digit = 1

        while n > 0:
            digit = n%10
            sum_digit += digit
            product_digit *=digit

            n//=10
        return product_digit - sum_digit