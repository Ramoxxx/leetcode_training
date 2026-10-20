# Algo Drills

Exercises to practise problem-solving patterns before the technical test.
Each file contains **one exercise**: the statement, an empty function to
fill in, and test cases that run when you execute the file.

## How to use

1. Clone the repo and open it in your editor.
2. Pick a file, for example `warmup/contains_duplicate.py`.
3. Read the statement at the top. **Before writing any code**, do this:
   - Reword the problem in one sentence.
   - Run one example by hand on paper.
   - Name what is happening: am I comparing? scanning? remembering?
   - Only then write the code.
4. Run the file:

   ```
   python warmup/contains_duplicate.py
   ```

5. Read the output. Green `PASS` lines mean that case works. A `FAIL`
   line shows you exactly what was expected versus what you returned.
6. When everything passes, say the solution out loud: which pattern,
   which data structure, what complexity.

## Run everything at once

```
python run_all.py
```

This runs every file and prints a pass/fail summary per exercise. Handy
to see where you still have work to do.

Unsolved functions intentionally fail: this is normal on a fresh clone.
The command exits with status 1 if any exercise fails, crashes, or times
out, and 0 when all pass. Each exercise has a 10-second limit to stop
accidental infinite loops; change it with `python run_all.py --timeout 30`.
This is a local safety limit, not a performance benchmark for the exam.

## Folders

- **warmup/** — the pattern is obvious from the title. Build confidence.
- **drill/** — the core patterns for the test. Spend the most time here.
- **simulation/** — reworded problems with no pattern hint, like the real
  test. Read carefully, name the pattern yourself, then solve.

## The four-step method (read this before you start)

The hardest part is usually not the code — it is knowing where to begin.
When you feel stuck, you almost certainly skipped a step:

1. **Reword** the problem in your own words.
2. **Trace** one example by hand, no code.
3. **Name** what is happening (compare / scan / count / remember).
4. **Code** what you just described.

If the idea will not come, you jumped straight to step 4. Go back to 1.

## A note on tests

The test cases include edge cases on purpose: empty inputs, single
elements, duplicates at the end, negatives, zeros. A solution that only
passes the obvious case is fragile. Make all of them green.

Each statement specifies its input domain: an empty input is only required
when allowed there. Return the exact requested type: `True`, `1`, and
`"true"` are different answers. Floats allow rounding differences through
`math.isclose` with relative and absolute tolerances of `1e-9`.

All green tests check the listed cases; also review any complexity,
in-place mutation, or forbidden-operation requirements in the statement.

## Requirements

Python 3.8 or newer. No external libraries.
