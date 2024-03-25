class Solution:
    def isPalindrome(self, x: int) -> bool:
        #habdle negative numbers
        if x < 0:
            return False
        
        #convert the string into an integer
        str_x = str(x)
        #returns a reverse string
        return str_x == str_x[::-1] or str_x == "0"
