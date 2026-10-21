
# CodSoft Task 3 — Secure Code Assessment

A beginner-friendly Python project for the CodSoft Cyber Security
Internship. It demonstrates how to identify common secure-coding
weaknesses and improve a simple profile-validation program.

## Project Overview

This project compares two implementations:

- **`example_vulnerable.py`** — intentionally insecure example for
  educational code review.
- **`secure_version.py`** — improved version with input validation
  and safer error handling.
- **`SECURITY_ASSESSMENT.md`** — security findings, severity ratings,
  potential impacts, remediation recommendations, and test cases.

## Learning Objectives

- Understand input validation.
- Identify missing boundary checks.
- Recognize risks associated with exposing internal errors.
- Understand why output protections depend on context.
- Document security findings and recommend fixes.
- Compare insecure and improved code.

## Requirements

- Python 3.10 or newer recommended
- No third-party packages required

## Getting Started

Clone the repository or download its source files.

Open a terminal in the project folder.

### Run the vulnerable example

```bash
python example_vulnerable.py
```

This program is intentionally insecure and should only be used for
local educational review. Do not deploy it.

### Run the improved version

```bash
python secure_version.py
```

Enter fictional test data and observe how the program handles valid
and invalid values.

## Example Test Data

Valid example:

- Name: Alex
- Email: alex@example.com
- Age: 25

Invalid examples:

- Empty name
- Email without a valid basic format
- Age entered as `abc`
- Age entered as `-5`
- Age entered as `150`
- Age entered as `20.5`

Expected behavior: the secure version should reject invalid input
with a clear validation message.

## Findings

The assessment covers:

1. Missing input validation
2. Missing age-range validation
3. Internal exception disclosure
4. User-input display and output-context considerations

Read [`SECURITY_ASSESSMENT.md`](SECURITY_ASSESSMENT.md) for details.

## Project Structure

```text
CODSOFT_TASK3/
├── example_vulnerable.py
├── secure_version.py
├── SECURITY_ASSESSMENT.md
└── README.md
```

## Security Notice

The vulnerable file exists solely to demonstrate secure-code-review
concepts. Do not use it in production.

The improved version is an educational example, not a complete
production security solution. Applications handling real user data
require additional review and controls appropriate to their context.

## Author

Created as part of the CodSoft Cyber Security Internship — Task 3:
Secure Code Assessment.
