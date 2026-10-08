class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_letters_cpt = dict()
        for letter in ransomNote:
            note_letters_cpt[letter] = note_letters_cpt.get(letter,0) + 1
        mag_letters_cpt = dict()
        for letter in magazine:
            mag_letters_cpt[letter] = mag_letters_cpt.get(letter,0) + 1
        for letter in note_letters_cpt.keys():
            in_note = note_letters_cpt[letter]
            in_mag = mag_letters_cpt.get(letter,0)
            if in_mag < in_note:
                return False 
        return True