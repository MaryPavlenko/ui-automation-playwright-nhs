# Checklist: NHS England Digital — Developer and integration hub

Scope: /developer, /developer/api-catalogue, individual API pages.
Read-only verification against production.

Legend:
- Auto — covered by an automated test, ID references docs/test-cases.md
- Manual — verified manually, not automated
- Not covered — deliberately out of scope, reason given


---

### Cookie consent

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | Consent dialog appears on first visit | High | Auto — NHS-CKI-01 |
| 2 | Dialog contains "Allow all cookies" button | High | Auto — NHS-CKI-01 |
| 3 | Dialog contains "Use necessary cookies only" button | High | Auto — NHS-CKI-01 |
| 4 | "Show details" link expands cookie categories | Medium | Manual |
| 5 | Consent choice persists after reload | High | Auto — NHS-CKI-02 |
| 6 | Dialog does not block page content after dismissal | High | Auto — NHS-CKI-02 |
| 7 | "Change cookie settings" in footer reopens the dialog | Low | Manual |

---

### Global navigation

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | Header contains all six primary sections | High | Auto — NHS-NAV-01 |
| 2 | Each primary link points to the correct URL | High | Auto — NHS-NAV-01 |
| 3 | Developer link opens the hub page | Medium | Auto — NHS-NAV-02 |
| 4 | NHS England logo links to the site root | Medium | Manual |
| 5 | Search icon opens the search interface | Medium | Manual |
| 6 | "Skip to main content" link is present | High | Auto — NHS-A11Y-01 |
| 7 | "Skip to main content" moves focus to main content | High | Auto — NHS-A11Y-01 |
| 8 | Mobile menu opens and closes at narrow viewport | Medium | Auto — NHS-NAV-05 |

---

### Breadcrumbs

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | Hub page shows two breadcrumb levels | Medium | Auto — NHS-NAV-03 |
| 2 | Catalogue page shows three breadcrumb levels | Medium | Auto — NHS-NAV-04 |
| 3 | API page shows four breadcrumb levels | Medium | Auto — NHS-NAV-06 |
| 4 | Current page in breadcrumbs is not a link | Medium | Auto — NHS-NAV-04 |
| 5 | Breadcrumb links navigate to the correct pages | Medium | Auto — NHS-NAV-04 |

---

### Developer hub page

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | Page title is correct | High | Auto — NHS-HUB-01 |
| 2 | Page has exactly one level 1 heading | High | Auto — NHS-HUB-01 |
| 3 | Three primary entry points are present | High | Auto — NHS-HUB-02 |
| 4 | "Get started" link points to /developer/getting-started | High | Auto — NHS-HUB-02 |
| 5 | "Browse catalogue" link opens the catalogue | High | Auto — NHS-HUB-03 |
| 6 | "View documentation" link points to the guides section | High | Auto — NHS-HUB-02 |
| 7 | Four support cards are present with correct targets | Low | Auto — NHS-HUB-04 |
| 8 | Sign in and Create account buttons are present | Low | Manual |
| 9 | Sign in and Create account flows | — | Not covered — real OAuth, out of scope |
| 10 | Images have alt text | Medium | Auto — NHS-A11Y-02 |

---

### API catalogue — general

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | Catalogue page loads with correct heading | High | Auto — NHS-CAT-01 |
| 2 | Total result count is displayed | High | Auto — NHS-CAT-02 |
| 3 | Result cards show a title as a link | High | Auto — NHS-CAT-03 |
| 4 | Result cards show a status badge | High | Auto — NHS-CAT-03 |
| 5 | Result cards show taxonomy tags | Medium | Auto — NHS-CAT-03 |
| 6 | Entries are grouped alphabetically | Medium | Manual |
| 7 | "Back to top" link returns to the page header | Low | Manual |
| 8 | Catalogue search returns relevant results | High | Auto — NHS-CAT-04 |
| 9 | Catalogue search with no matches shows an empty state | High | Auto — NHS-CAT-05 |
| 10 | Catalogue search handles special characters | Medium | Auto — NHS-CAT-06 |

---

### Alphabetical navigation

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | Letters with results are rendered as links | High | Auto — NHS-CAT-07 |
| 2 | Letters without results are not links | High | Auto — NHS-CAT-08 |
| 3 | Clicking a letter filters results to that letter | High | Auto — NHS-CAT-07 |
| 4 | Filtered view shows only entries starting with that letter | High | Auto — NHS-CAT-07 |

---

### Filters

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | All filter groups are displayed | Medium | Auto — NHS-FLT-01 |
| 2 | Each filter value shows a result counter | High | Auto — NHS-FLT-01 |
| 3 | Applying a filter narrows the result set | High | Auto — NHS-FLT-02 |
| 4 | Result count matches the filter counter | High | Auto — NHS-FLT-03 |
| 5 | Applied filter is visually indicated | Medium | Manual |
| 6 | Two filters can be combined | Medium | Auto — NHS-FLT-04 |
| 7 | "Reset filters" clears all applied filters | High | Auto — NHS-FLT-05 |
| 8 | "show more" expands the full list of filter values | Low | Manual |
| 9 | Exhaustive testing of all ~69 filter values | — | Not covered — sampling strategy, see test plan |

---

### Pagination

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | Pagination controls are displayed | High | Auto — NHS-PAG-01 |
| 2 | First page is shown by default | High | Auto — NHS-PAG-01 |
| 3 | Navigating to page 2 loads different results | High | Auto — NHS-PAG-02 |
| 4 | Last page is reachable and loads results | High | Auto — NHS-PAG-03 |
| 5 | Page number is reflected in the URL | Medium | Auto — NHS-PAG-02 |
| 6 | Traversal of all intermediate pages | — | Not covered — sampling strategy, see test plan |

---

### Individual API pages

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | API page loads with correct heading | High | Auto — NHS-API-01 |
| 2 | Status badge is displayed | High | Auto — NHS-API-02 |
| 3 | Description is present | Medium | Auto — NHS-API-01 |
| 4 | Taxonomy tags link back to filtered catalogue views | Medium | Auto — NHS-API-03 |
| 5 | Documentation or specification links are present | Medium | Manual |
| 6 | Breadcrumbs reflect the catalogue hierarchy | Medium | Auto — NHS-NAV-06 |

---

### Footer

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | Legal section contains all expected links | Medium | Auto — NHS-HUB-05 |
| 2 | Get in touch section contains all expected links | Medium | Auto — NHS-HUB-05 |
| 3 | Accessibility statement link is present | High | Auto — NHS-HUB-05 |
| 4 | Social media links are present with correct hrefs | Low | Auto — NHS-HUB-05 |
| 5 | External links are marked as external | Low | Manual |
| 6 | Navigation to external domains | — | Not covered — third-party sites out of scope |

---

### Accessibility

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | "Skip to main content" link works | High | Auto — NHS-A11Y-01 |
| 2 | Images have alt attributes | Medium | Auto — NHS-A11Y-02 |
| 3 | Page has one level 1 heading | High | Auto — NHS-HUB-01 |
| 4 | Heading levels are not skipped | Medium | Auto — NHS-A11Y-03 |
| 5 | Landmarks are present (banner, main, contentinfo, navigation) | High | Auto — NHS-A11Y-04 |
| 6 | No critical axe-core violations on the hub page | High | Auto — NHS-A11Y-05 |
| 7 | No critical axe-core violations on the catalogue page | High | Auto — NHS-A11Y-06 |
| 8 | Interactive elements are reachable by keyboard | High | Manual |
| 9 | Focus is visible on interactive elements | Medium | Manual |
| 10 | Colour contrast meets WCAG AA | Medium | Auto — covered by axe-core |

---

### Cross-browser and responsive

| # | Check | Priority | Status |
|---|---|---|---|
| 1 | Suite passes in Chromium | High | Auto — CI matrix |
| 2 | Suite passes in Firefox | High | Auto — CI matrix |
| 3 | Suite passes in WebKit | High | Auto — CI matrix |
| 4 | Mobile menu behaviour at narrow viewport | Medium | Auto — NHS-NAV-05 |
| 5 | Catalogue filters are usable at narrow viewport | Medium | Manual |

---