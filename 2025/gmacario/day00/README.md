# Boilerplate for AoC-2025 daily solver

Perform the following steps:

1. Copy `day00` to the desired day `daynn`
2. Rename `solve_day00.py` to `solve_daynn.py`
3. Rename `sample_day00.txt` to `sample_daynn.txt`
4. Copy the text of Day _nn_ challenge into `README.md`. Make sure to correct Markdown formatting
5. Copy the sample input for Day _nn_ challenge into `sample_daynn.txt`
6. Fetch the actual input into `input_daynn.txt`
7. Read and understand `README.md`
8. Adjust `solve_daynn.py` accordingly
9. Test the solution to Part 1 of the challenge:

   ```bash
   uv run daynn/solve_daynn.py
   ```

10. Ensure that the solution to `sample_daynn.txt` matches the one in the `README.md`
11. Repeat steps 7-10 until the solution to Part 1 passes with the sample data
12. Uncomment line 10 of `solve_daynn.py`, then run the solver against `input_daynn.txt`

    ```bash
    uv run daynn/solve_daynn.py
    ```

13. Paste the value in line `INFO:  Daynn solve_part1 result: xxx` into the text field of AoC-2025 Day _nn_ challenge
14. If everything works, do a `git commit` with the working changes, then proceed to solving Part 2
15. Comment line 10 of `solve_daynn.py`
16. Update `README.md` with the text for Part 2 of the challenge
17. Repeat steps 7-12 until Part 2 is solved
18. If everything works, do a `git commit` with the working changes
19. Update the code until all Super-Linter checks are green
20. Create a Pull Request against <https://github.com/B-AROL-O/advent-of-code>

<!-- EOF -->
