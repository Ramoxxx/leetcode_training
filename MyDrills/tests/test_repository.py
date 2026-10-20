"""Trainer regression suite. No dependency beyond the standard library."""

import ast
from bisect import bisect_left
from contextlib import redirect_stdout
import io
from itertools import combinations, groupby, product
import math
from pathlib import Path
import random
import runpy
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import run_all
from teacher import solutions as ref
from teacher.verify import ROOT, exercise_paths, verify_exercise


def words(alphabet, max_length):
    for length in range(max_length + 1):
        for chars in product(alphabet, repeat=length):
            yield "".join(chars)


def arrays(alphabet, max_length):
    for length in range(max_length + 1):
        for values in product(alphabet, repeat=length):
            yield list(values)


class ExerciseAudit(unittest.TestCase):
    def test_every_exercise_with_references(self):
        paths = exercise_paths()
        self.assertGreaterEqual(len(paths), 55)
        for path in paths:
            with self.subTest(exercise=path.relative_to(ROOT)):
                self.assertGreater(verify_exercise(path), 0)

    def test_docstring_examples(self):
        """Check executable one-line examples too, independently of main tests."""
        checked = 0
        for path in exercise_paths():
            doc = ast.get_docstring(ast.parse(path.read_text(encoding="utf-8")))
            self.assertTrue(doc, path)
            for line in doc.splitlines():
                if " -> " not in line:
                    continue
                call, expected = (part.strip() for part in line.split("->", 1))
                try:
                    call_tree = ast.parse(call, mode="eval").body
                    # The first expression may be followed by explanatory prose.
                    expected_tree = ast.parse(expected, mode="eval").body
                except SyntaxError:
                    continue
                if not isinstance(call_tree, ast.Call) or not isinstance(call_tree.func, ast.Name):
                    continue
                try:
                    arguments = [ast.literal_eval(arg) for arg in call_tree.args]
                    value = ast.literal_eval(expected_tree)
                except (ValueError, TypeError):
                    continue
                with self.subTest(exercise=path.name, example=line):
                    self.assertEqual(getattr(ref, call_tree.func.id)(*arguments), value)
                checked += 1
        self.assertGreater(checked, 70)

    def test_tests_reject_common_wrong_solutions(self):
        cases = [
            ("drill/number_stream.py", "number_stream",
             lambda s: "true" if any(s.count(c) >= int(c) for c in s) else "false"),
            ("drill/largest_four.py", "largest_four",
             lambda nums: sum(sorted(set(nums))[-4:])),
            ("drill/triangle_number_check.py", "is_triangle_number",
             lambda n: isinstance(n, (int, float)) and n >= 0
             and math.sqrt(8 * n + 1).is_integer()),
            ("drill/product_of_array_except_self.py", "product_except_self",
             lambda nums: [0] * len(nums) if 0 in nums else
             [math.prod(nums[:i] + nums[i+1:]) for i in range(len(nums))]),
            ("drill/max_sum_distinct_subarray_k.py", "max_distinct_sum",
             lambda nums, k: max(sum(nums[i:i+k]) for i in range(len(nums)-k+1))),
            ("simulation/challenge_07.py", "pair_for_total",
             lambda nums, total: next(([i, j] for i in range(len(nums))
                                      for j in range(i, len(nums))
                                      if nums[i] + nums[j] == total), [])),
            ("simulation/challenge_13.py", "sink_zeros",
             lambda nums: [x for x in nums if x] + [0] * nums.count(0)),
            ("simulation/challenge_22.py", "same_shape",
             lambda a, b: len(a) == len(b)
             and len(set(zip(a, b))) == len(set(a))),
            ("simulation/challenge_25.py", "scramble_spots",
             lambda text, key: [i for i in range(len(text)-len(key)+1)
                                if set(text[i:i+len(key)]) == set(key)]),
            ("warmup/check_if_pangram.py", "is_pangram", lambda s: len(s) >= 26),
        ]
        for filename, name, broken in cases:
            with self.subTest(exercise=filename), patch.object(ref, name, broken):
                with self.assertRaises(AssertionError):
                    verify_exercise(ROOT / filename)

        def linear_first(n, checker):
            return next(v for v in range(1, n + 1) if checker(v))

        with patch.object(ref, "first_broken", linear_first):
            with self.assertRaisesRegex(AssertionError, "too many checker calls"):
                verify_exercise(ROOT / "simulation/challenge_33.py")


class IndependentOracles(unittest.TestCase):
    def test_numeric_arrays_exhaustively(self):
        for nums in arrays((-2, -1, 0, 1, 2), 5):
            self.assertEqual(ref.largest_four(nums), sum(sorted(nums, reverse=True)[:4]))
            self.assertEqual(ref.contains_duplicate(nums),
                             any(nums[i] == nums[j] for i, j in combinations(range(len(nums)), 2)))
            self.assertEqual(ref.distinct_count(sorted(nums)), len(set(nums)))
            original = nums[:]
            moved = ref.sink_zeros(original)
            self.assertIs(moved, original)
            self.assertEqual(moved, [x for x in nums if x != 0] + [0] * nums.count(0))
            odds = sorted(x for x in nums if x % 2)
            expected = nums[:]
            for i, x in enumerate(nums):
                if x % 2:
                    expected[i] = odds.pop(0)
            self.assertEqual(ref.sort_odd(nums), expected)
            if len(nums) >= 2:
                expected = [math.prod(nums[:i] + nums[i+1:]) for i in range(len(nums))]
                self.assertEqual(ref.product_except_self(nums), expected)

    def test_windows_exhaustively(self):
        for nums in arrays((1, 2, 3), 6):
            for k in range(1, len(nums) + 1):
                windows = [nums[i:i+k] for i in range(len(nums)-k+1)]
                expected = max((sum(w) for w in windows if len(set(w)) == k), default=0)
                self.assertEqual(ref.max_distinct_sum(nums, k), expected)
                self.assertAlmostEqual(ref.best_average(nums, k),
                                       max(sum(w) / k for w in windows))
        for nums in arrays((-3, -1, 2), 4):
            for k in range(1, len(nums) + 1):
                self.assertAlmostEqual(ref.best_average(nums, k),
                                       max(sum(nums[i:i+k]) / k for i in range(len(nums)-k+1)))

    def test_pairs_search_and_rotation(self):
        for nums in arrays((-1, 0, 1, 2), 4):
            for target in range(-3, 6):
                pairs = [[i, j] for i, j in combinations(range(len(nums)), 2)
                         if nums[i] + nums[j] == target]
                if len(pairs) <= 1:
                    self.assertEqual(ref.pair_for_total(nums, target), pairs[0] if pairs else [])
                sorted_nums = sorted(nums)
                pairs = [[i+1, j+1] for i, j in combinations(range(len(nums)), 2)
                         if sorted_nums[i] + sorted_nums[j] == target]
                if len(pairs) <= 1:
                    self.assertEqual(ref.coupon_pair(sorted_nums, target), pairs[0] if pairs else [])
        for size in range(8):
            nums = list(range(-size, size, 2))
            for target in range(-9, 10):
                self.assertEqual(ref.search_insert(nums, target), bisect_left(nums, target))
                for pivot in range(max(1, len(nums))):
                    rotated = nums[pivot:] + nums[:pivot]
                    expected = rotated.index(target) if target in rotated else -1
                    self.assertEqual(ref.locate(rotated, target), expected)

    def test_profits_and_water(self):
        for nums in arrays((0, 1, 3), 6):
            pairs = list(combinations(range(len(nums)), 2))
            expected = max([0] + [nums[j] - nums[i] for i, j in pairs])
            self.assertEqual(ref.best_profit(nums), expected)
            expected = max([0] + [min(nums[i], nums[j]) * (j-i) for i, j in pairs])
            self.assertEqual(ref.most_water(nums), expected)

    def test_strings_exhaustively(self):
        for text in words("abA ", 5):
            self.assertEqual(ref.unique_in_order(text), [c for c, _ in groupby(text)])
            self.assertEqual(ref.first_unique(text),
                             next((i for i, c in enumerate(text) if text.count(c) == 1), -1))
            lowered = text.lower()
            self.assertEqual(ref.duplicate_encode(text),
                             "".join("(" if lowered.count(c) == 1 else ")" for c in lowered))
            cleaned = "".join(c.lower() for c in text if c.isalnum())
            self.assertEqual(ref.is_palindrome(text), cleaned == cleaned[::-1])
            self.assertEqual(ref.almost_palindrome(text),
                             text == text[::-1] or any(
                                 (text[:i] + text[i+1:]) == (text[:i] + text[i+1:])[::-1]
                                 for i in range(len(text))))
            self.assertEqual(ref.longest_clean_run(text), max(
                (j-i for i in range(len(text)+1) for j in range(i, len(text)+1)
                 if len(set(text[i:j])) == j-i), default=0))
            squashed = text
            while True:
                i = next((i for i in range(len(squashed)-1)
                          if squashed[i] == squashed[i+1]), None)
                if i is None:
                    break
                squashed = squashed[:i] + squashed[i+2:]
            self.assertEqual(ref.squash(text), squashed)
        for text in words("abc", 5):
            for key in ("a", "aa", "ab", "aab", "abc", "aaaaaa"):
                self.assertEqual(ref.scramble_spots(text, key),
                                 [i for i in range(len(text)-len(key)+1)
                                  if sorted(text[i:i+len(key)]) == sorted(key)])
        for text in words("234", 6):
            if text:
                expected = "true" if any(c * int(c) in text for c in "234") else "false"
                self.assertEqual(ref.number_stream(text), expected)

    def test_subsequences_isomorphism_and_anagrams(self):
        tokens = list(words("ab", 4))
        for a in tokens:
            subsequences = {"".join(a[i] for i in range(len(a)) if mask & (1 << i))
                            for mask in range(1 << len(a))}
            for b in tokens:
                self.assertEqual(ref.is_subsequence(b, a), b in subsequences)
                self.assertEqual(ref.is_anagram(a, b), sorted(a) == sorted(b))
                expected = len(a) == len(b) and all(
                    (a[i] == a[j]) == (b[i] == b[j])
                    for i in range(len(a)) for j in range(len(a)))
                self.assertEqual(ref.same_shape(a, b), expected)

    def test_brackets_by_pair_reduction(self):
        for text in words("()[]{}", 5):
            reduced = text
            while any(pair in reduced for pair in ("()", "[]", "{}")):
                for pair in ("()", "[]", "{}"):
                    reduced = reduced.replace(pair, "")
            self.assertEqual(ref.is_valid(text), reduced == "")

    def test_integer_boundaries_and_checker_budget(self):
        triangles = {m * (m + 1) // 2 for m in range(150)}
        for n in range(10000):
            self.assertEqual(ref.is_triangle_number(n), n in triangles)
            self.assertEqual(ref.int_sqrt(n), math.isqrt(n))
            self.assertEqual(ref.is_power_of_two(n), n in {2**i for i in range(14)})
        for bad in (True, False, None, "3", [], {}, float("inf"), float("nan"), 1.5, -1):
            self.assertIs(ref.is_triangle_number(bad), False)
        for n in range(1, 80):
            for first in range(1, n + 1):
                calls = []

                def checker(version):
                    self.assertIs(type(version), int)
                    self.assertTrue(1 <= version <= n)
                    calls.append(version)
                    return version >= first

                self.assertEqual(ref.first_broken(n, checker), first)
                self.assertLessEqual(len(calls), n.bit_length())
        for n in range(1000):
            digits = list(map(int, str(n)))
            self.assertEqual(ref.tick(digits), list(map(int, str(n+1))))

    def test_stack_against_list_model(self):
        rng = random.Random(20261015)
        stack, model = ref.MinStack(), []
        for _ in range(1000):
            if model and rng.randrange(3) == 0:
                self.assertIsNone(stack.pop())
                model.pop()
            else:
                value = rng.randrange(-5, 6)
                self.assertIsNone(stack.push(value))
                model.append(value)
            if model:
                self.assertEqual(stack.top(), model[-1])
                self.assertEqual(stack.get_min(), min(model))

    def test_roman_numerals_all_canonical_values(self):
        table = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                 (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                 (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))
        for n in range(1, 4000):
            remaining, numeral = n, ""
            for value, symbol in table:
                count, remaining = divmod(remaining, value)
                numeral += symbol * count
            self.assertEqual(ref.roman_value(numeral), n)

    def test_remaining_patterns_against_simple_models(self):
        rng = random.Random(42)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for _ in range(500):
            # Missing value and a single unpaired value, including negatives.
            n = rng.randrange(30)
            missing = rng.randrange(n + 1)
            nums = [x for x in range(n + 1) if x != missing]
            rng.shuffle(nums)
            self.assertEqual(ref.missing_number(nums), missing)
            singleton = -50
            nums = list(range(n)) * 2 + [singleton]
            rng.shuffle(nums)
            self.assertEqual(ref.single_number(nums), singleton)

            codes = [rng.choice(("ab", "ba", "aab", "aba", "", "b", "A"))
                     for _ in range(rng.randrange(10))]
            remaining, groups = codes[:], []
            while remaining:
                first = remaining[0]
                group = [x for x in remaining if sorted(x) == sorted(first)]
                groups.append(sorted(group))
                remaining = [x for x in remaining if sorted(x) != sorted(first)]
            self.assertEqual(ref.cluster(codes), sorted(groups, key=lambda g: g[0]))
            expected = ""
            if codes:
                for i in range(1, len(codes[0]) + 1):
                    if all(c.startswith(codes[0][:i]) for c in codes):
                        expected = codes[0][:i]
            self.assertEqual(ref.common_start(codes), expected)

            views = [rng.randrange(-3, 4) for _ in range(rng.randrange(15))]
            k = rng.randrange(len(set(views)) + 1)
            self.assertEqual(ref.top_viewed(views, k),
                             sorted(set(views), key=lambda x: (-views.count(x), x))[:k])
            right = [rng.randrange(-3, 4) for _ in range(rng.randrange(15))]
            self.assertEqual(ref.in_both(views, right),
                             sorted({x for x in views if x in right}))
            majority = [99] * (len(views) + 1) + views
            rng.shuffle(majority)
            self.assertEqual(ref.winner(majority), 99)

            text = "".join(rng.choices("abAeIoUxy !", k=rng.randrange(20)))
            vowels = [c for c in text if c in "aeiouAEIOU"]
            self.assertEqual(ref.flip_vowels(text),
                             "".join(vowels.pop() if c in "aeiouAEIOU" else c for c in text))
            self.assertEqual(ref.reverse_words(text), " ".join(text.split()[::-1]))
            if text.strip():
                self.assertEqual(ref.length_of_last_word(text), len(text.strip().split(" ")[-1]))
            text = "".join(rng.choices(alphabet, k=rng.randrange(100)))
            self.assertEqual(ref.is_pangram(text), all(c in text for c in alphabet))
            left = "".join(rng.choices("abA12", k=rng.randrange(1, 20)))
            right = left[::-1]
            expected = "".join((left if i % 2 == 0 else right)[i // 2]
                               for i in range(len(left) * 2))
            self.assertEqual(ref.string_merge(left + "*" + right), expected)

            scores, ops = [], []
            for _ in range(30):
                allowed = ["number"] + (["C", "D"] if scores else [])
                if len(scores) >= 2:
                    allowed.append("+")
                op = rng.choice(allowed)
                if op == "number":
                    value = rng.randrange(-9, 10)
                    scores.append(value)
                    ops.append(str(value))
                elif op == "C":
                    ops.append(op)
                    scores = scores[:-1]
                elif op == "D":
                    ops.append(op)
                    scores += [scores[-1] * 2]
                else:
                    ops.append(op)
                    scores += [sum(scores[-2:])]
            self.assertEqual(ref.final_total(ops), sum(scores))

        for a, b, c in product(range(-1, 6), repeat=3):
            self.assertEqual(ref.is_triangle(a, b, c),
                             min(a, b, c) > 0 and a + b > c and a + c > b and b + c > a)
        for n in range(100):
            expected = []
            for i in range(1, n+1):
                if i % 15 == 0:
                    expected.append("FizzBuzz")
                elif i % 3 == 0:
                    expected.append("Fizz")
                elif i % 5 == 0:
                    expected.append("Buzz")
                else:
                    expected.append(str(i))
            self.assertEqual(ref.row_labels(n), expected)
        for n in range(1, 500):
            # A bounded sequence model: once a value repeats, reaching 1 later
            # is impossible. This also catches missing cycle detection.
            sequence = [n]
            while sequence[-1] != 1:
                current = sequence[-1]
                digits = []
                while current:
                    current, digit = divmod(current, 10)
                    digits.append(digit)
                following = sum(x*x for x in digits)
                if following in sequence:
                    break
                sequence.append(following)
            self.assertEqual(ref.is_lucky(n), sequence[-1] == 1)


class TestInfrastructure(unittest.TestCase):
    def test_types_float_tolerance_and_report_exit(self):
        helper = runpy.run_path(str(ROOT / "testkit.py"))
        equal = helper["_equal"]
        self.assertFalse(equal(True, 1))
        self.assertFalse(equal(1, True))
        self.assertFalse(equal([1], ["1"]))
        self.assertFalse(equal([True], [1]))
        self.assertFalse(equal((1,), [1]))
        self.assertFalse(equal(5, 5.0))
        self.assertTrue(equal(0.1 + 0.2, 0.3))
        self.assertFalse(equal(0.31, 0.3))
        self.assertFalse(equal(float("nan"), 0.0))
        for pairs, code in (([], 1), ([(1, 1)], 0), ([(1, 2)], 1)):
            helper = runpy.run_path(str(ROOT / "testkit.py"))
            with redirect_stdout(io.StringIO()):
                for got, expected in pairs:
                    helper["check"]("case", got, expected)
                with self.assertRaises(SystemExit) as caught:
                    helper["report"]()
            self.assertEqual(caught.exception.code, code)

    def test_folder_helpers_share_root_behavior(self):
        for folder in ("drill", "simulation", "warmup"):
            helper = runpy.run_path(str(ROOT / folder / "testkit.py"))
            with redirect_stdout(io.StringIO()):
                helper["check"]("wrong boolean type", 1, True)
                with self.assertRaises(SystemExit) as caught:
                    helper["report"]()
            self.assertEqual(caught.exception.code, 1)

    def test_runner_failure_crash_timeout_and_continuation(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory) / "warmup"
            folder.mkdir()
            files = {
                "a_pass.py": "raise SystemExit(0)",
                "b_fail.py": "raise SystemExit(1)",
                "c_crash.py": "raise RuntimeError('broken submission')",
                "d_timeout.py": "while True: pass",
                "e_continues.py": "raise SystemExit(0)",
            }
            for filename, source in files.items():
                (folder / filename).write_text(source, encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, "-c",
                 "import run_all; run_all.HERE = " + repr(directory)
                 + "; raise SystemExit(run_all.main())", "--timeout", "1"],
                cwd=ROOT, capture_output=True, text=True, timeout=15,
            )
            self.assertEqual(completed.returncode, 1)
            self.assertIn("TIMEOUT", completed.stdout)
            self.assertIn("e_continues.py", completed.stdout)
            self.assertIn("Exercises: 2 passed, 3 failed.", completed.stdout)
            self.assertIn("RuntimeError", completed.stderr)

    def test_runner_success_empty_and_invalid_timeout(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory) / "warmup"
            folder.mkdir()
            with patch.object(run_all, "HERE", directory), patch.object(
                sys, "argv", ["run_all.py"]
            ), redirect_stdout(io.StringIO()):
                self.assertEqual(run_all.main(), 1)
                (folder / "ok.py").write_text("raise SystemExit(0)")
                self.assertEqual(run_all.main(), 0)
        for timeout in ("0", "-1", "nan", "inf"):
            with patch.object(sys, "argv", ["run_all.py", "--timeout", timeout]), patch(
                "sys.stderr", new_callable=io.StringIO
            ):
                with self.assertRaises(SystemExit) as caught:
                    run_all.main()
                self.assertEqual(caught.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
