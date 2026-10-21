"""
NUMBER STREAM
Pattern: Linear scan / consecutive run length

Given a non-empty string containing only digits from 2 to 9, return the
string "true" if some digit d repeats consecutively at least d times.
Otherwise return the string "false". Count consecutive occurrences,
not the total number of occurrences scattered through the string.

Examples:
    number_stream("6539923335") -> "true"  (three consecutive 3s)
    number_stream("232323")     -> "false"
    number_stream("2222")       -> "true"  (at least two 2s)

Contract: return lowercase strings, as in Coderbyte, not Python booleans.
Digits 0 and 1 and empty strings are outside the input domain.

Think about: remember the previous digit and the current run length.
When the digit changes, the new run starts at one, not zero.

Source: recueil_questions.md, Coderbyte Number Stream.
"""

from testkit import check, report


def number_stream(digits):
    prev = None
    current_cpt = 0
    for digit in digits:
        current_digit = int(digit)
        if prev == current_digit:
            current_cpt += 1
            if current_cpt >= current_digit:
                return "true"
        else:
            current_cpt = 1
        prev = current_digit
    return "false"     
        



if __name__ == "__main__":
    check("run in middle", number_stream("6539923335"), "true")
    check("no qualifying run", number_stream("5556293383563665"), "false")
    check("single digit", number_stream("2"), "false")
    check("exact length", number_stream("22"), "true")
    check("longer than needed", number_stream("2222"), "true")
    check("scattered repeats", number_stream("232323"), "false")
    check("run after change", number_stream("322"), "true")
    check("run at end", number_stream("2333"), "true")
    check("eight nines are not enough", number_stream("99999999"), "false")
    check("nine nines", number_stream("999999999"), "true")
    report()
