# Pull Requests and Code Review Reflection

## 1. Why is Squash and Merge preferable for small feature branches?
Squash and Merge combines the implementation and review-fix commits into one focused commit on main, making the history easier to read and the feature easier to revert. The pull request still preserves the discussion and development context.

## 2. How do Add single comment and Start a review differ?
Add single comment publishes feedback immediately, while Start a review collects pending comments and submits them together with a review decision. Batching keeps related feedback together and reduces repeated notifications and interruptions.

## 3. How do branch protection rules prevent accidental production breakage?
When enforced without bypasses, branch protection can block direct changes to main and require a pull request with an approving review before merging. Required status checks can also prevent merging failing code, reducing the risk of production breakage without guaranteeing that every bug is caught.

## 4. Why merge origin/main locally rather than force-pushing?
After fetching, merging origin/main into the feature branch preserves both lines of development and lets the author resolve conflicts and test the combined code before updating the PR. Force-pushing rewrites remote history and can overwrite collaborators' work without reconciling the conflicting changes.

## Practice mode and assistance
This exercise uses the assignment's solo fallback, with Codex assistance authorized by the repository owner. PR #1 contains a batched COMMENT self-review, a separate docstring revision, and a resolved thread; no peer approval is claimed. See WORK_LOG.md for the actual commands, publication method, and any remaining setup.
