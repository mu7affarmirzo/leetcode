class Solution(object):
    def intToRoman(self, num):
        roman_nums = [
            {
                "I": "1",
                "II": "2",
                "III": "3",
                'IV': "4",
                "V": "5",
                'VI': "6",
                'VII': "7",
                'VIII': "8",
                "IX": "9"
            },
            {
                "X": "10",
                "XX": "20",
                "XXX": "30",
                "XL": "40",
                "L": "50",
                "LX": "60",
                "LXX": "70",
                "LXXX": "80",
                "XC": "90",
            },
            {
                "C": "100",
                "CC": "200",
                "CCC": "300",
                "CD": "400",
                "D": "500",
                "DC": "600",
                "DCC": "700",
                "MCCC": "800",
                "CM": "900"
            },
            {
                "M": "1000",
                "MM": "2000",
                "MMM": "3000",
            }
        ]
        """
        :type num: int
        :rtype: str
        """
        temp = 1
        result = ''
        for i in range(len(str(num))):
            # print(str(num)[-i-1])
            if str(num)[-i-1] == '0':
                temp *= 10
                continue
            target_digit = int(str(num)[-i-1])*temp

            temp1 = roman_nums[i]
            value = [j for j in temp1 if temp1[j] == str(target_digit)]
            # print(value)
            result = value[0] + result
            temp *= 10
        print(f"------: {result}")


s = Solution()

s.intToRoman(800)

# for i in range(1, 4000):
#     try:
#         s.intToRoman(i)
#     except:
#         print(f"------\n---------"
#               f"EXCEPTION: {i}")

# CMXLVII