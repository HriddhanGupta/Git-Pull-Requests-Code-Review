# Practice Work Log

## Scope and starting point
The provided repository was empty. A basic addition/subtraction calculator was initialized as the baseline; this is not claimed to be an imported previous assignment. Work was performed with Codex assistance in a Linux terminal and through the owner's connected GitHub account.

## GitHub actions actually performed
1. Initialized calculator.py on main (948d396).
2. Created add-multiply-divide and committed the new operations (4813e30).
3. Opened PR #1 with summary, testing instructions, and solo reviewer assignment.
4. Submitted a single COMMENT review containing an inline docstring request through GitHub's review API. This is the batched-review equivalent of the UI's Start a review / Finish your review, not a standalone issue comment.
5. Added docstrings in a separate commit (f56e65e), tested, and resolved the review thread.
6. Squash-merged PR #1 (0662c10).
7. Opened PR #2 from feature-header with the V2 header (673fd9b).
8. Opened and merged supporting PR #3 from alternate-header with SUPER CALCULATOR, creating a competing main change (b7cd8ce).
9. GitHub reported PR #2 as mergeable=false, mergeable_state=dirty. Local Git also produced a real conflict.
10. Resolved the header to SUPER CALCULATOR V2 locally and published the resolved merge tree with both original parents to the same feature-header branch.

## Terminal commands and observed output (abridged)
Repository path is abbreviated below. Feature creation, PR creation, review submission, and merges used the GitHub connector rather than fictitious terminal commands.

```console
$ git clone https://github.com/HriddhanGupta/Git-Pull-Requests-Code-Review.git repo
Cloning into 'repo'...

$ git fetch origin
$ git switch --track origin/add-multiply-divide
branch 'add-multiply-divide' set up to track 'origin/add-multiply-divide'.

$ python3 calculator.py
=== CALCULATOR ===
8 + 2 = 10
8 - 2 = 6
8 * 2 = 16
8 / 2 = 4.0

$ python3 - <<'PY'
from calculator import add, subtract, multiply, divide
assert add(8,2)==10
assert subtract(8,2)==6
assert multiply(6,4)==24
assert multiply(-3,2)==-6
assert multiply(0,5)==0
assert divide(12,3)==4
assert divide(5,2)==2.5
try:
    divide(10,0)
except ValueError as e:
    assert str(e)=='Cannot divide by zero'
else:
    raise AssertionError('Missing ValueError')
print('All 8 calculator checks passed.')
PY
All 8 calculator checks passed.

$ git fetch origin
$ git switch --track origin/feature-header
$ git merge origin/main
Auto-merging calculator.py
CONFLICT (content): Merge conflict in calculator.py
Automatic merge failed; fix conflicts and then commit the result.
```

The conflicting block was replaced with:

```python
    print("=== SUPER CALCULATOR V2 ===")
```

```console
$ python3 calculator.py
=== SUPER CALCULATOR V2 ===
8 + 2 = 10
8 - 2 = 6
8 * 2 = 16
8 / 2 = 4.0

$ python3 -m py_compile calculator.py
$ git diff --check
$ git add calculator.py
$ git -c user.name='Hriddhan Gupta' -c user.email='136644263+HriddhanGupta@users.noreply.github.com' commit -m 'Resolve conflict with main'
[feature-header cbae802] Resolve conflict with main

$ git push origin feature-header
fatal: could not read Username for 'https://github.com': No such device or address

$ git rev-parse HEAD^{tree}
8c2383f8ad9484ab0b69f28f66b735d47dfd4b03

$ git show -s --format='%P' HEAD
673fd9bf372b534c65b3c91f9c835fcaa7b6fb97 b7cd8ce37dc344c1e03cc47db6543a35b19cd617
```

The terminal could fetch this public repository but had no push credentials. The authenticated GitHub connector therefore created merge commit 0ca2dfc with the identical tree SHA and the same two ordered parents, then advanced feature-header without force. This preserves the real locally resolved merge; it does not claim that the failed terminal push succeeded.

## Reproduce validation
```bash
python3 calculator.py
python3 -m unittest -v
python3 -m py_compile calculator.py test_calculator.py
git diff --check
```

## Remaining administrative setup at time of writing
The connector does not expose branch-protection updates or remote-branch deletion, and the browser is signed out. The owner must configure main to require PRs and one approval (using the documented solo exception when necessary), and delete the merged feature branches. Branch protection is not claimed to have been configured. PR and code work can be inspected independently through the linked history.
