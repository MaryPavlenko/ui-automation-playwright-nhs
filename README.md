# UI Automation [NHS Developer Hub]
[![UI Tests](https://github.com/MaryPavlenko/ui-automation-playwright-nhs/actions/workflows/playwright.yml/badge.svg)](https://github.com/MaryPavlenko/ui-automation-playwright-nhs/actions/workflows/playwright.yml)
[![Playwright](https://img.shields.io/badge/Playwright-Python-2EAD33)]() [![pytest](https://img.shields.io/badge/framework-pytest-blue)]() [![POM](https://img.shields.io/badge/pattern-Page%20Object%20Model-lightgrey)]() [![Cross-browser](https://img.shields.io/badge/cross--browser-Chromium%20%7C%20Firefox%20%7C%20WebKit-orange)]()

## Overview

End-to-end UI automation of the NHS England Digital [Developer and integration hub](https://digital.nhs.uk/developer) using Playwright (Python), pytest and the Page Object Model.

The goal of this project is to show a structured QA approach to UI automation: from test planning and test design techniques to a Page Object architecture, cross-browser execution, accessibility checks, and CI on GitHub Actions.

**Object under test:** https://digital.nhs.uk/developer

The testing artifacts connect into one structured workflow:
```text
User journey → Test Plan → Test Design Techniques → Test Cases → Checklist → Page Objects → Automated Tests → CI
```

This project deliberately covers one user journey in depth (a developer finding and evaluating an NHS API in the catalogue) rather than the whole site shallowly.

## My Role

I defined the test scope and user journey, wrote the test plan and test cases, mapped test design techniques to each case, built the Page Object framework, automated the tests in Playwright with pytest, and configured cross-browser execution and CI.

## What's Inside

- **[docs/test-plan.md](docs/test-plan.md)** — scope, user journey, sampling strategy, respectful testing constraints, risks.
- **[docs/test-cases.md](docs/test-cases.md)** — test cases with IDs, steps, techniques, and links to automated tests.
- **[docs/test-design-techniques.md](docs/test-design-techniques.md)** — test design techniques mapped to specific test cases.
- **[docs/checklist.md](docs/checklist.md)** — coverage checklist across all functional areas.
- **[pages/](pages/)** — Page Object Model: base page and page-specific classes.
- **[tests/](tests/)** — automated Playwright tests, organized by area and marked with pytest markers.
- **[conftest.py](conftest.py)** — pytest fixtures, including cookie consent handling via storage state.
- **[.github/workflows/](.github/workflows)** — GitHub Actions: smoke suite on push, full cross-browser suite on schedule.

## Respectful testing

The object under test is a third-party production website. Testing is deliberately constrained to avoid unnecessary load: read-only interactions only, no form submissions or authentication, limited parallelism, sampled coverage instead of exhaustive traversal, and a full suite scheduled daily rather than on every commit. Details are in the [test plan](docs/test-plan.md).

## How to Run

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install pytest-playwright
playwright install

# 3. Generate the cookie consent state (once)
python setup_auth.py

# 4. Run the tests
pytest                        # default browser (chromium)
pytest -m smoke               # smoke suite only
pytest --browser chromium --browser firefox --browser webkit   # all browsers
```

## Tools

Python, Playwright (Python), pytest, Page Object Model, GitHub Actions.

Techniques: equivalence partitioning, boundary value analysis, state transition, error guessing, data consistency checks, checklist-based verification, accessibility testing (axe-core), cross-browser testing.

This is an independent QA portfolio project. It is not commissioned by, affiliated with, or endorsed by NHS England. All testing is performed against publicly available pages in read-only mode.

## Author

Created by [Mary Pavlenko](https://www.linkedin.com/in/mary-pavlenko/) as part of a QA Engineering portfolio.