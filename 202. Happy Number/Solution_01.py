class Solution:
    def isHappy(self, n: int) -> bool:
        cpt = 0
        seen = set()
        while not n in seen and n != 1:
            seen.add(n)
            n_str = str(n)
            n = 0
            for char in n_str:
                number = int(char)
                n += (number**2)
            cpt += 1
        return n == 1