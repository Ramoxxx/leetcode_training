"""
CHALLENGE 28

A report numbers its rows from 1 to n, but with two display rules:
    - rows divisible by 3 show "Fizz" instead of the number
    - rows divisible by 5 show "Buzz" instead of the number
    - rows divisible by both 3 and 5 show "FizzBuzz"
    - all other rows show the number as a string

Given n, return the list of row labels from 1 to n.

Examples:
    row_labels(3) -> ["1", "2", "Fizz"]
    row_labels(5) -> ["1", "2", "Fizz", "4", "Buzz"]

Contract:
n is a non-negative integer. For n = 0, return [].
Return a list of strings, with the exact capitalization shown.

"""

from testkit import check, report


def row_labels(n):
    result = []
    for num in range(1,n+1):
        if num % 15 == 0:
            result.append("FizzBuzz")
        elif num % 5 == 0:
            result.append("Buzz")
        elif num % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(num))
    return result



if __name__ == "__main__":
    check("up to three", row_labels(3), ["1", "2", "Fizz"])
    check("up to five", row_labels(5), ["1", "2", "Fizz", "4", "Buzz"])
    check("includes fizzbuzz", row_labels(15),
          ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
           "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])
    check("zero rows", row_labels(0), [])
    check("single row", row_labels(1), ["1"])
    check('second fizzbuzz', row_labels(30)[-1], 'FizzBuzz')
    report()
