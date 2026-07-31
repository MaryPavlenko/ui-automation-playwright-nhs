# Test Design Techniques

This document explains the test design techniques applied in this project and maps each one to the specific test cases that use it. The goal is to make the reasoning behind test selection explicit, rather than testing by intuition.

Full test cases are in docs/test-cases.md.

---

## Why test design techniques matter

The catalogue contains 188 entries, around 69 filter values, 26 alphabet letters and 10 pages of results. Testing every combination is impossible and, against a third-party production site, irresponsible. Test design techniques are a systematic way to choose a small set of inputs that finds the most defects for the least execution. They also make coverage defensible: each test exists for a stated reason, not by chance.

---

## Equivalence Partitioning (EP)

**What it is**: Inputs are divided into groups (partitions) that the system is expected to treat the same way. One representative from each partition is tested, on the assumption that if the representative passes, the rest of the partition will too.

**Why it is used here**: The alphabet navigation and the catalogue search both have inputs that fall into clear classes. Testing every letter or every search term adds execution time without adding meaningful coverage.

**Where it is applied**:
- NHS-CAT-07 and NHS-CAT-08 — alphabet letters split into two partitions: letters with results (A, B) and letters without results (J, K, X, Y, Z). One representative of each class is tested. A letter with results should be a link; a letter without results should be plain text.
- NHS-CAT-04 and NHS-CAT-05 — search terms split into a partition that returns results (a known term such as "booking") and a partition that returns nothing (a term such as "zzzznomatch").
- NHS-FLT-02 — filter values treated as a partition that narrows the result set.

Example of the reasoning: There is no need to click all 21 letters that have results. If "A" behaves correctly, "C" is expected to behave the same way, because they belong to the same equivalence class. The valuable contrast is between the two classes, not within one class.

---

## Boundary Value Analysis (BVA)

**What it is**: Defects cluster at the edges of a range rather than in the middle. BVA tests the values at and around boundaries.

**Why it is used here**: Pagination is a bounded range: page 1 to page 10. The middle pages are the least likely to reveal defects; the edges are where off-by-one errors, missing "previous" or "next" controls, and empty last pages tend to appear.

**Where it is applied**: 
- NHS-PAG-01 — first page, the lower boundary, is active by default.
- NHS-PAG-02 — transition across the first boundary, from page 1 to page 2.
- NHS-PAG-03 — last page, the upper boundary, loads and shows results.

Example of the reasoning: Intermediate pages (3 to 9) are deliberately not traversed. They belong to the interior of the range and are covered by the same rendering logic as pages 1 and 2. Testing them would add load on the site without adding defect-finding power.

---

## State Transition

**What it is**: Some behaviour depends on the current state and on transitions between states, not on a single input. State transition testing checks that the system moves correctly between states and holds each state as expected.

**Why it is used here**: Cookie consent is stateful: the banner shown to a first-time visitor must not reappear after a choice is made, and that choice must persist across page loads. Filters have a similar reset transition.

**Where it is applied**:
- NHS-CKI-01 — initial state: consent not yet given, banner is displayed.
- NHS-CKI-02 — transition: choice made, then reload; the accepted state must persist and the banner must not return.
- NHS-FLT-05 — transition: filters applied, then reset back to the initial unfiltered state.

Example of the reasoning: Checking only that the banner appears is not enough. The defect risk is in the transition: a site can show the banner correctly but fail to remember the choice, so the banner returns on every page. That is only caught by testing the transition and the persistence.

---

## Data Consistency

**What it is**: A check that two representations of the same information agree with each other. Rather than comparing against a fixed expected value, it compares two values the system itself produces.

**Why it is used here**: Each filter shows a counter, for example "FHIR (80)". That counter is a promise about how many results the filter will return. If the promise and the actual result set disagree, the user is misled. Because catalogue content changes over time, a hard-coded expected number would be fragile, so the check is made between two live values in the same run.

**Where it is applied**: NHS-FLT-03 — the counter shown next to a filter is compared with the actual number of results after that filter is applied, in the same execution.

Example of the reasoning: Hard-coding "expect 80 results" would break the day NHS adds an eighty-first FHIR API. The robust check is "the number the counter claims equals the number of results actually shown", which stays valid regardless of how the catalogue grows.

---

## Error Guessing

**What it is**: Tests are designed from experience about where systems commonly fail: unusual input, special characters, empty values, and other cases developers often forget to handle.

**Why it is used here**: Search fields are a classic source of unhandled-input defects. Special characters can break query handling or rendering if input is not sanitised.

**Where it is applied**: NHS-CAT-06 — special characters ("!!!@@@###") entered into catalogue search, checking the page handles them gracefully rather than erroring or breaking layout.

Example of the reasoning: A normal search term follows the happy path. Experience says that punctuation and symbols are where input handling tends to fail, so this input is chosen specifically to probe that weakness.

---

## Checklist-Based Verification

**What it is**: Verification against a predefined list of expected elements or conditions. Useful for structural and inventory checks where the value is completeness rather than input variation.

**Why it is used here**: Navigation links, footer links, breadcrumb levels, landmark regions and required page elements are all inventory checks: a known set of things must be present and correct.

**Where it is applied**:
- NHS-NAV-01 — six primary navigation links and their targets.
- NHS-HUB-02 and NHS-HUB-04 — primary entry points and support cards.
- NHS-HUB-05 — footer sections and links.
- NHS-A11Y-04 — required landmark regions.

Example of the reasoning: There is no input to vary here; the risk is omission. A checklist makes the expected inventory explicit so a missing or mis-targeted link is caught deterministically.

---

## Tool-Based Audit (accessibility)

**What it is**: An automated scan using a specialised tool, here axe-core, which checks a page against a ruleset derived from WCAG.

**Why it is used here**: Accessibility is a legal requirement for UK public sector sites. An automated audit gives broad, repeatable coverage of common accessibility defects.

**Where it is applied**: NHS-A11Y-05 and NHS-A11Y-06 — axe-core scans of the hub and catalogue pages, failing on critical or serious violations.

Important limitation: Automated accessibility tools detect roughly a third of accessibility issues. They cannot judge whether alt text is meaningful, whether focus order is logical, or whether content makes sense to a screen reader user. For that reason the axe-core scans are combined with explicit structural checks (NHS-A11Y-01 to NHS-A11Y-04) and with manual checks recorded in the checklist. The tool is a floor, not a ceiling.

---

## Summary mapping

| Technique | Test cases |
|---|---|
| Equivalence Partitioning | NHS-CAT-04, NHS-CAT-05, NHS-CAT-07, NHS-CAT-08, NHS-FLT-02 |
| Boundary Value Analysis | NHS-PAG-01, NHS-PAG-02, NHS-PAG-03 |
| State Transition | NHS-CKI-01, NHS-CKI-02, NHS-FLT-05 |
| Data Consistency | NHS-FLT-03 |
| Error Guessing | NHS-CAT-06 |
| Checklist-Based Verification | NHS-NAV-01, NHS-HUB-02, NHS-HUB-04, NHS-HUB-05, NHS-A11Y-04 |
| Tool-Based Audit | NHS-A11Y-05, NHS-A11Y-06 |