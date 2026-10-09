# // For this challenge you will be merging two different strings together.
# /*
# have the function StringMerge(str) 
# read the str parameter being passed which will contain a large string of alphanumeric characters
#  with a single asterisk character splitting the string evenly into two separate strings.
#   Your goal is to return a new string by pairing up the characters in the corresponding locations in both strings. 
# For example: if str is "abc1*kyoo" then your program should return the string akbyco1o because a pairs with k, b pairs with y, etc.
# The string will always split evenly with the asterisk in the center.
# */

# #include <iostream>
# #include <string>
# using namespace std;

# /*
# split the string into 2
# after combine the 2 strings into one doing a step by step merge alternating between the 2
# */

def stringMerge(s:str) -> str :
    result = []
    splitted = s.split("*")
    for i,left_char in enumerate(splitted[0]):        
        result.append(left_char)
        result.append(splitted[1][i])
    return "".join(result)
print(stringMerge("abc1*kyoo"))
print(stringMerge("aaa*bbb"))
print(stringMerge("123hg*aaabb"))
 
# int main() 
# {
# 	cout << StringMerge("abc1*kyoo") << endl; // akbyco1o
# 	cout << StringMerge("aaa*bbb") << endl; // ababab
# 	cout << StringMerge("123hg*aaabb") << endl; // 1a2a3ahbgb
# 	return 0;

# }