# Test Cases: NHS England Digital — Developer and integration hub

ID prefixes for Test Cases:
- NHS-CKI — cookie consent
   - NHS-CKI-01: Cookie consent dialog is displayed on first visit
   - NHS-CKI-02: Consent choice persists after page reload
- NHS-NAV — global navigation and breadcrumbs
   - NHS-NAV-01: Primary navigation contains all six sections with correct targets
   - NHS-NAV-02: Developer link in primary navigation opens the hub page
   - NHS-NAV-03: Breadcrumbs on the hub page show two levels
   - NHS-NAV-04: Breadcrumbs on the catalogue page show three levels
- NHS-HUB — Developer hub landing page
   - NHS-HUB-01: Hub page has correct title and a single level 1 heading
   - NHS-HUB-02: Three primary entry points are present with correct targets
   - NHS-HUB-03: Browse catalogue button opens the API catalogue
   - NHS-HUB-04: Four support cards link to the correct destinations
- NHS-CAT — API catalogue, general
- NHS-FLT — catalogue filters
- NHS-PAG — catalogue pagination
- NHS-API — individual API pages
- NHS-A11Y — accessibility

---

### NHS-CKI-01: Cookie consent dialog is displayed on first visit

Area: Cookie consent
Priority: High
Technique: State transition
Type: Positive

Preconditions: Fresh browser context with no stored cookies.

Steps:
1. Open https://digital.nhs.uk/developer

Expected result:
The cookie consent dialog "Your privacy and cookies" is displayed. It contains the
buttons "Allow all cookies" and "Use necessary cookies only", and a "Show details" link.

Automated test: tests/test_cookie_banner.py::test_banner_is_displayed_on_first_visit

---

### NHS-CKI-02: Consent choice persists after page reload

Area: Cookie consent
Priority: High
Technique: State transition
Type: Positive

Preconditions: Fresh browser context with no stored cookies.

Steps:
1. Open https://digital.nhs.uk/developer
2. Click "Use necessary cookies only"
3. Reload the page

Expected result:
The dialog is dismissed after the click and is not displayed again after reload.
Page content is interactive.

Automated test: tests/test_cookie_banner.py::test_consent_choice_persists_after_reload

---

### NHS-NAV-01: Primary navigation contains all six sections with correct targets

Area: Global navigation
Priority: High
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Inspect the primary navigation in the page header

Expected result:
The navigation contains six links with the following accessible names and targets:
Services → /services
Data → /data
Cyber → /cyber
Developer → /developer
News → /news
About → /about-nhs-digital

Automated test: tests/test_navigation.py::test_primary_navigation_links

---

### NHS-NAV-02: Developer link in primary navigation opens the hub page

Area: Global navigation
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Click the "Developer" link in the primary navigation

Expected result:
The Developer hub page loads. The page heading is "Developer and integration hub".

Automated test: tests/test_navigation.py::test_developer_nav_link_opens_hub

---

### NHS-NAV-03: Breadcrumbs on the hub page show two levels

Area: Breadcrumbs
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer

Expected result:
Breadcrumbs show two levels: "NHS Digital" as a link to the site root, followed by
"Developer" as the current page.

Automated test: tests/test_navigation.py::test_hub_breadcrumbs

---

### NHS-NAV-04: Breadcrumbs on the catalogue page show three levels

Area: Breadcrumbs
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue

Expected result:
Breadcrumbs show three levels: "NHS Digital" → "Developer" → "API and integration
catalogue". The first two are links, the last is the current page and is not a link.

Automated test: tests/test_navigation.py::test_catalogue_breadcrumbs

---

### NHS-HUB-01: Hub page has correct title and a single level 1 heading

Area: Developer hub
Priority: High
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer

Expected result:
Page title contains "Developer and integration hub".
The page has exactly one level 1 heading, with the text "Developer and integration hub".

Automated test: tests/test_hub.py::test_hub_title_and_heading

---

### NHS-HUB-02: Three primary entry points are present with correct targets

Area: Developer hub
Priority: High
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Inspect the three primary content sections

Expected result:
Three entry points are present with working links:
"Getting started with our APIs" → /developer/getting-started
"API and integration catalogue" → /developer/api-catalogue
"Documentation, guides and tutorials" → /developer/guides-and-documentation

Automated test: tests/test_hub.py::test_primary_entry_points

---

### NHS-HUB-03: Browse catalogue button opens the API catalogue

Area: Developer hub
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Click "Browse catalogue"

Expected result:
The API and integration catalogue page loads at /developer/api-catalogue.
The page heading is "API and integration catalogue".

Automated test: tests/test_hub.py::test_browse_catalogue_navigation

---

### NHS-HUB-04: Four support cards link to the correct destinations

Area: Developer hub
Priority: Low
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Inspect the four support cards

Expected result:
Four support links are present with correct targets:
"Developer community" → https://developer.community.nhs.uk/ (external)
"Help and support building software" → /developer/help-and-support
"Our architecture" → /developer/architecture
"Onboarding to APIs and services" → /developer/assurance/process-for-apis-and-services

External links are verified by href only; navigation is not performed.

Automated test: tests/test_hub.py::test_support_links

---

