
# Security Assessment Report
## CodSoft Cyber Security Internship — Task 3

**Project:** Secure Code Assessment  
**Language:** Python 3  
**Assessment type:** Static code review and local functional testing  
**Scope:** `example_vulnerable.py` and `secure_version.py`  
**Environment:** Local educational environment using fictional profile data  
**Status:** Educational assessment; not a production security audit

---

## 1. Executive Summary

This assessment reviews a simple Python profile validator to identify
common secure-coding weaknesses. The original implementation has
insufficient input validation, accepts unreasonable age values, and
exposes internal exception messages to users.

A corrected implementation was developed with validation functions,
controlled error handling, and clearer separation between validation
and profile creation.

The purpose of this project is to demonstrate how a code review can
identify weaknesses and how developers can reduce associated risks.

## 2. Scope and Methodology

The review covered:

- Input validation and boundary checks
- Handling of unexpected user input
- Error-message disclosure
- Handling and display of user-provided values
- Comparison of vulnerable and corrected implementations

Methods used:

1. Read both source files.
2. Identify unsafe assumptions and missing checks.
3. Run the programs locally with fictional test data.
4. Compare expected and actual validation behavior.
5. Document findings and remediation recommendations.

This is a small educational exercise, not a complete penetration test,
formal verification, or certification of application security.

## 3. Findings Summary

| ID | Finding | Severity |
|---|---|---|
| F-01 | Missing validation for name and email | Medium |
| F-02 | Age range is not checked | Low |
| F-03 | Internal exception details are displayed | Low |
| F-04 | User input is displayed without context-specific encoding | Informational |

Severity reflects the potential risk in this demonstration. Actual
severity depends on the surrounding application, data flows, and
deployment environment.

## 4. Detailed Findings

### F-01: Missing Input Validation

**Severity:** Medium

**Location:** `example_vulnerable.py`, `create_profile()`

**Observation:**

The original program accepts name and email values without checking
whether they are empty, too long, or formatted as expected.

**Potential impact:**

Invalid or unexpected data may be stored or passed to later components.
If the profile data is reused in other contexts, downstream components
may behave incorrectly or require additional defensive handling.

**Recommendation:**

- Reject empty values.
- Apply reasonable maximum lengths.
- Validate fields according to their intended formats.
- Validate data at the point where it enters the application.

**Remediation:** Implemented in `secure_version.py` through
`validate_name()` and `validate_email()`.

### F-02: Missing Age Range Validation

**Severity:** Low

**Location:** `example_vulnerable.py`, `create_profile()`

**Observation:**

The original program converts the age to an integer but does not
verify that it falls within a sensible range.

**Potential impact:**

Negative or implausibly large values can be accepted. This can lead
to incorrect records and inconsistent application behavior.

**Recommendation:**

Check that age is a whole number and falls within the application's
defined permitted range.

**Remediation:** Implemented in `validate_age()`, which accepts ages
from 1 through 120.

### F-03: Internal Exception Disclosure

**Severity:** Low

**Location:** `example_vulnerable.py`, `main()`

**Observation:**

The original program displays the text of any caught exception
directly to the user.

**Potential impact:**

Unexpected exceptions can reveal implementation details that users
do not need to see. In larger applications, detailed errors may expose
paths, internal names, or operational information.

**Recommendation:**

Show safe, understandable messages for expected input errors. Handle
unexpected errors without exposing internal exception details to users.
Production systems should log diagnostic details securely on the
server when appropriate.

**Remediation:** Implemented using `ValidationError` and a generic
unexpected-error message in `secure_version.py`.

### F-04: User Input Display and Output Context

**Severity:** Informational

**Location:** `example_vulnerable.py`, profile output

**Observation:**

The original program displays the profile object containing
user-supplied values directly.

**Potential impact:**

Displaying input in a local terminal is not the same as inserting
input into a web page. However, if the same values are later placed
into HTML, SQL, shell commands, or another interpreted context,
context-specific protections become necessary.

**Recommendation:**

Use the appropriate encoding or parameterization for the destination.
For HTML, use context-appropriate output encoding or a safe templating
mechanism. For database operations, use parameterized queries.
Do not treat input validation as a replacement for output encoding.

**Remediation:** The secure version validates values and displays
individual fields. Any future integration must still apply protections
appropriate to its output context.

## 5. Security Improvements

The corrected implementation introduces:

- Required-field validation
- Maximum field lengths
- Basic email-format checking
- Age range validation
- Explicit validation exceptions
- Safe messages for unexpected errors
- Separate validation functions for easier testing

The email check is intentionally basic. It does not prove that an
address exists or that the user owns it.

## 6. Functional Test Plan

| Test case | Example input | Expected result |
|---|---|---|
| Valid profile | Name: Alex; email: alex@example.com; age: 25 | Accepted |
| Empty name | Empty name | Rejected |
| Invalid email | `not-an-email` | Rejected |
| Non-numeric age | `abc` | Rejected |
| Negative age | `-5` | Rejected |
| Excessive age | `150` | Rejected |
| Decimal age | `20.5` | Rejected |
| Overlong name | More than 80 characters | Rejected |

Use fictional data only. The example email domain is for demonstration.

## 7. Limitations

- This project is a small command-line demonstration.
- The email validator is not a complete implementation of all
  valid email-address rules.
- No database, authentication system, or network service is included.
- No automated static-analysis tool has been used as part of this report.
- The review does not establish that the code is free from all defects.
- Production applications need additional controls based on their
  architecture, data sensitivity, and deployment model.

## 8. Conclusion

The review demonstrates the value of validating input, constraining
values to expected ranges, and controlling error disclosure.

The corrected version is a safer baseline for this educational example.
It should not be interpreted as a guarantee of production security.

## 9. Files Included

- `example_vulnerable.py` — intentionally insecure training example
- `secure_version.py` — corrected implementation
- `SECURITY_ASSESSMENT.md` — findings and remediation report
- `README.md` — setup, execution, and project overview

---

**Prepared for:** CodSoft Cyber Security Internship — Task 3  
**Project focus:** Secure Code Assessment
