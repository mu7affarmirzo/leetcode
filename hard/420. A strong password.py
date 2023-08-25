import re


class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)

        # Calculate the number of missing conditions
        missing_conditions = 3 - has_lower - has_upper - has_digit

        # Calculate the length difference required for password to be at least 6 characters
        length_difference = max(0, 6 - len(password))

        # Calculate the maximum steps required to eliminate repeating characters
        repeating_steps = 0
        for c in set(password):
            repeating_steps = min(repeating_steps, password.count(c) // 3)

        # Calculate the minimum steps required to satisfy all conditions
        return max(missing_conditions, length_difference, repeating_steps)


a = Solution()
a = a.strongPasswordChecker('1337C0d3')
print(a)