# Test Plan: NHS England Digital — Developer & Integration Hub

### 1. Purpose
This document defines the scope, approach and constraints for automated UI regression testing of the Developer and integration hub on digital.nhs.uk. It is not commissioned by, affiliated with or endorsed by NHS England. All testing is performed against publicly available pages in read-only mode.

### 2. Object under test
NHS England Digital Developer and integration hub.
Base URL: https://digital.nhs.uk/developer.<br>
The hub is the entry point for product owners, delivery leads, architects and developers who build healthcare software and integrate with NHS APIs.

### 3. User journey under test
A developer or architect working for a healthcare organisation needs to integrate with an NHS API. The journey is:

1. Arrive at the Developer hub
2. Navigate to the API and integration catalogue
3. Narrow down 188 available integrations using filters or alphabetical navigation
4. Open the page of a specific API
5. Confirm its status, technology and available documentation

### 4. Why this journey matters
If the catalogue is not searchable or filterable, a developer cannot determine which integration fits their use case. <br>
If status information is wrong or filters return inconsistent results, a team may integrate against an API that is deprecated or retired, and lose development time.<br>
If navigation or breadcrumbs break, users lose orientation inside a large content site.<br>
Accessibility is a legal requirement for UK public sector websites under the Public Sector Bodies (Websites and Mobile Applications) Accessibility Regulations 2018.

### 5. Scope
In scope:
- /developer — hub landing page
- /developer/api-catalogue — catalogue with filters, alphabetical navigation, pagination
- /developer/api-catalogue/{api-name} — individual API pages (limited sample)
- Global header navigation and breadcrumbs within the Developer section
- Footer links present on Developer section pages
- Cookie consent banner
- Accessibility checks on hub and catalogue pages

Out of scope:
- Sign in to developer account and Create account (real OAuth flows, external identity provider)
- Any authenticated area
- External domains: developer.community.nhs.uk, england.nhs.uk, social media links
  (link presence and href are verified, navigation is not performed)
- Sections of digital.nhs.uk outside /developer
- Performance, load and security testing
- Backend API testing (the NHS APIs themselves are not called)

### 6. Sampling strategy
The catalogue contains 188 entries across 10 pages and approximately 69 filter values. Exhaustive traversal would create unnecessary load on a third-party production system and would produce slow, low-value tests. <br>
<br>
Coverage is therefore deliberately sampled:<br>
- Filters — three values from three different filter groups, chosen to cover different result set sizes:
- Status → In production
- Technology → FHIR
- Integration type → API standard

Alphabetical navigation — two letters with results (A, B) and two letters without results (J, X). This is an equivalence partitioning decision, not an arbitrary choice. <br>

Pagination — first page, transition to second page, and last page. Intermediate pages are not traversed.<br>

API pages — two entries with stable production status. Entries marked as deprecated, retired or under review for deprecation are excluded, because their content is expected to change.

### 7. Test approach
- Framework: Playwright (Python, sync API) with pytest
- Architecture: Page Object Model with separate page components for header, footer and cookie banner
- Locators: role-based and accessible-name locators are preferred over CSS classes, because they are more stable and reflect how assistive technology reads the page
- Assertions: Playwright web-first assertions with built-in auto-waiting. No fixed sleeps
- Accessibility: axe-core via the axe-playwright-python integration
- Reporting: Allure
- Browsers: Chromium, Firefox, WebKit

### 8. Handling of cookie consent
The site presents a Cookiebot consent dialog on first visit. The dialog overlays page content and blocks interaction. <br>

Approach:
- One dedicated functional test verifies the banner itself (presence, buttons, dismissal)
- All other tests run with a pre-set consent state loaded via storage_state, so that the banner does not interfere with the behaviour under test

This mirrors common production practice: the consent mechanism is tested once, not repeatedly re-triggered in every test.

### 9. Respectful testing constraints
The object under test is a third-party production website. The following constraints apply:

- Maximum 2 parallel workers
- No exhaustive traversal of catalogue pages or filter combinations
- No form submissions, no account creation, no authentication attempts
- Read-only interactions only
- No attempt is made to bypass bot-mitigation measures

### 9.1 Test execution environments

The NHS suite is executed locally, not from CI. <br>
[digital.nhs.uk](https://digital.nhs.uk/) is protected by a bot-mitigation service. Requests originating from CI data-centre IP addresses receive a security verification page instead of the site content, so the tests cannot reach the pages under test. Circumventing that protection is out of scope and would contradict the constraints in section 9. To validate the framework itself in a continuous integration environment, a separate small suite runs against automationintesting.online, a demo application published specifically for test automation practice. That suite exercises the same framework components (Page Object Model, pytest markers, Playwright assertions) and runs on GitHub Actions: a smoke check on push, and the full suite across Chromium, Firefox and WebKit on a daily schedule.

Execution summary:
| Suite | Location | Execution |
|---|---|---|
| NHS Developer hub | tests/nhs/ | Local, on demand |
| Booking demo | tests/booking_demo/ | GitHub Actions: smoke on push, full suite daily |

### 10. Test levels and types
- Functional UI regression
- Navigation and content structure verification
- Data consistency checks (filter counters against actual result counts)
- Negative testing (empty result sets, non-existent search terms)
- Accessibility testing
- Cross-browser testing
- Responsive behaviour (mobile menu)

### 11. Test design techniques applied
- Equivalence partitioning — alphabet letters with and without results; filter values with large, medium and empty result sets
- Boundary value analysis — first and last pagination page
- State transition — cookie banner: not accepted → accepted → persisted
- Error guessing — special characters and empty input in catalogue search
- Checklist-based verification — footer and navigation link inventory
Detailed mapping is documented in docs/test-design-techniques.md.

### 12. Risks and limitations
The object is a live production site not controlled by the author. Consequences:<br>

- Content changes (new APIs, updated counts) can invalidate hard-coded expected values. Mitigation: assertions target structure and relative consistency rather than exact content where possible.
- Filter counters change as the catalogue is updated. Mitigation: counter tests compare the displayed counter with the actual number of results on the same page, rather than against a fixed number.
- Individual API pages may be deprecated or removed. Mitigation: only entries with stable production status are used, and the selection is documented so it can be revised.
- Site availability and rate limiting are outside the author's control. Mitigation: limited parallelism, retries configured in CI.

### 13. Environment
- Target: production (https://digital.nhs.uk)
- No test environment is available, as this is a public third-party site
- Python 3.13, Playwright 1.61, pytest 9.1
- Local execution and GitHub Actions

### 14. Entry and exit criteria
Entry: the site is reachable, the Developer hub returns HTTP 200. <br>
Exit: all tests in the suite pass in Chromium, Firefox and WebKit, or failures are triaged and documented as either defects or expected content changes.