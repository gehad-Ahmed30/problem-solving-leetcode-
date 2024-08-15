class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary={
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        total_flag=0
        #Convert "MCMXCIV" to an integer
        for i in range(len(s)):    
            current_value=dictionary[s[i]] #Current character: 'M' (value 1000)
            if i+1 <len(s) and dictionary[s[i]] < dictionary[s[i+1]]:
                total_flag-=current_value
            else:
                total_flag+=current_value
        return total_flag


