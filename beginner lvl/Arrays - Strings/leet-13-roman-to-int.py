class Solution:
    def romanToInt(self, s: str) -> int:
        # map all given integers to their corresponding roman characters
        roman_dict = {
            "I": 1,
            'V': 5,
            'X': 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        size = len(s)
        i = 0
        integer = 0

        if size == 1: # if a single roman number is inputted return it from the dictionary
            return roman_dict[s]

        while i < size:
            j = i + 1
            if j < size and str(s[i] + s[j]) in roman_dict: #use two pointers to find if two consectutive roman numbers have a corresponding integer in the map
                integer += roman_dict[str(s[i] + s[j])]
                i = j+1
            else: # if two consecutive roman characters do not match any of the characters in the dictionary then a single one is
                integer += roman_dict[s[i]]
                i += 1

        return integer
