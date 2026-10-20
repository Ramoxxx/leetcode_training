"""
CHALLENGE 17

A text effect for a banner reverses only the vowels of a caption while
leaving every other character exactly where it is. The vowels are
a, e, i, o, u in both lower and upper case; case is preserved as the
characters move.

Given the caption, return the new string with its vowels reversed.

Examples:
    flip_vowels("hello")    -> "holle"
    flip_vowels("computer") -> "cemputor"

Contract:
Input may be empty. Only the ten vowel characters listed above move;
y and accented letters are not treated as vowels here.

"""

from testkit import check, report


def flip_vowels(caption):
    vowels_lower = "aeiou"
    left = 0
    right = len(caption) - 1
    result = list(caption)
    while left < right:
        while left < right and caption[left].lower() not in vowels_lower:
            left += 1
        while left < right and caption[right].lower() not in vowels_lower:
            right -= 1  
            
        if left < right and caption[left] != caption[right]:
            result[left] = caption[right]
            result[right] = caption[left]
                
        left += 1
        right -= 1
    return "".join(result)


if __name__ == "__main__":
    check("simple", flip_vowels("hello"), "holle")
    check("several vowels", flip_vowels("computer"), "cemputor")
    check("case preserved", flip_vowels("aA"), "Aa")
    check("no vowels", flip_vowels("xyz"), "xyz")
    check("empty", flip_vowels(""), "")
    check("single vowel", flip_vowels("hi"), "hi")
    check('all vowels mixed case', flip_vowels("aEiOu"), 'uOiEa')
    report()
