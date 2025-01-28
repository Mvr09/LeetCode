class Solution:
    def countDigitOne(self,n: int) -> int:
        if n < 0:
            return 0

        count = 0
        factor = 1

        while factor <= n:
            lower_digits = n - (n // factor) * factor
            current_digit = (n // factor) % 10
            higher_digits = n // (factor * 10)


            if current_digit == 0:
                count += higher_digits * factor

            elif current_digit == 1:
                count += higher_digits * factor + lower_digits + 1

            else:
                count += (higher_digits + 1) * factor

            factor *= 10  

        return count
