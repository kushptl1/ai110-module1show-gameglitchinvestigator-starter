# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->
Generate advanced pytest cases for edge inputs to `parse_guess` and `check_guess`, and move/refactor game logic into `logic_utils.py`.

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
- Implemented `check_guess`, `parse_guess`, and `update_score` in `logic_utils.py`.
- Removed duplicate logic from `app.py` and updated imports.
- Added multiple pytest files under `test/` and `tests/` including `test_edge_cases.py` covering advanced inputs.
- Ran tests locally (notebook/terminal) and iterated until all tests passed.

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
- Adjusted some test assertions to match the tuple return shape `(outcome, message)` of `check_guess`.
- Confirmed that venv and pytest were installed and that pytest collected the intended test directory; consolidated test files.
- Verified message text assertions (e.g., checks for "LOWER"/"HIGHER") to be robust to emoji/text.


---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

Below are the prompts used to generate the edge-case tests and a one-line explanation of why each edge case was included.

- Negative numbers / zero
	- Prompt used: ``"Add a pytest ensuring parse_guess accepts negative integers like '-5' and that check_guess treats them as numeric comparisons."``
	- Why: Inputs outside the expected 1..N range may still parse and produce surprising outcomes; test ensures behavior is explicit.

- Decimal / fractional inputs (e.g., "3.7")
	- Prompt used: ``"Add a pytest that supplies a decimal string '3.7' to parse_guess and asserts it is converted/truncated to int(3)."``
	- Why: The current implementation converts floats to int, which can silently truncate — a likely UX bug.

- AI-generated — 
	- Prompt used: ``"Create pytest tests for parse_guess and check_guess covering the edge cases above and any additional sensible edge-case tests you (the AI) can think of."``
    - Why: Broaden coverage for malformed, localized, and extreme numeric inputs.