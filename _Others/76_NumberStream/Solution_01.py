# // For this challenge you will determine if a stream of digits occurs in a string.
# /*
# have the function NumberStream(str) take the str parameter being passed which will contain the numbers 2 through 9, 
# and determine if there is a consecutive stream of digits of at least N length where N is the actual digit value. 
# If so, return the string true, otherwise return the string false.
#  For example: if str is "6539923335" then your program should return the string true 
# because there is a consecutive stream of 3's of length 3. The input string will always contain at least one digit.
# */

# #include <iostream>
# #include <string>
# using namespace std;

# /*
# traverse the string
# have a temp string that will increase if values are consecutive
# if the next value is not the same as current consecutive values
# break and analyze the length of the temp string
# if the length matches the digit value than return true
# else continue until the string has been fully traversed
# */
def NumberStream(s:str)->bool:
    left = 0
    right = 0
    while left < len(s)-1:          
        stream_end = False
        stream_cpt = 0
        right = left
        while not stream_end:
            if right < len(s)-1 and s[left] == s[right]:
                stream_cpt += 1
                right += 1
            else:
                if stream_cpt == int(s[left]):
                    return True
                else:
                    stream_end = True                
        left = right +1       

    return False;
	
	
print(NumberStream("5556293383563665"))
print(NumberStream("5788888888882339999"))
print(NumberStream("6539923335"))

# cout << NumberStream("5556293383563665") << endl; // false
# cout << NumberStream("5788888888882339999") << endl; // true -> erreur dans l'énoncé?
# cout << NumberStream("6539923335") << endl; // true
# return 0;
