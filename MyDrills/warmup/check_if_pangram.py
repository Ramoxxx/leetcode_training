"""
CHECK IF THE SENTENCE IS PANGRAM
Pattern: Set membership

A pangram contains every letter of the English alphabet at least once.
Given a string containing only lowercase English letters, return True
if it is a pangram, otherwise False. Letter order does not matter.

Examples:
    is_pangram("thequickbrownfoxjumpsoverthelazydog") -> True
    is_pangram("leetcode") -> False

Contract: input contains only a-z; repeated letters are allowed.
As a local extension, an empty string returns False. Return a bool.
Uppercase letters, accents, spaces, and punctuation are out of scope.

Think about: how many distinct letters does a complete alphabet have?

Source: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
"""

from testkit import check, report


def is_pangram(sentence):
    letters = {*()}
    for letter in sentence:
        letters.add(letter)
        if len(letters) >= 26:
            return True
    return False



if __name__ == "__main__":
    check("classic", is_pangram("thequickbrownfoxjumpsoverthelazydog"), True)
    check("incomplete", is_pangram("leetcode"), False)
    check("alphabet", is_pangram("abcdefghijklmnopqrstuvwxyz"), True)
    check("reverse alphabet", is_pangram("zyxwvutsrqponmlkjihgfedcba"), True)
    check("missing z", is_pangram("abcdefghijklmnopqrstuvwxy"), False)
    check("26 characters are not 26 letters", is_pangram("a" * 26), False)
    check("repetitions allowed", is_pangram("abcdefghijklmnopqrstuvwxyzabc"), True)
    check("empty extension", is_pangram(""), False)
    report()
