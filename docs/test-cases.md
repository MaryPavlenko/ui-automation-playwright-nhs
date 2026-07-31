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
   - NHS-NAV-05: Mobile menu opens and closes at narrow viewport
   - NHS-NAV-06: Breadcrumbs on an API page show four levels
- NHS-HUB — Developer hub landing page
   - NHS-HUB-01: Hub page has correct title and a single level 1 heading
   - NHS-HUB-02: Three primary entry points are present with correct targets
   - NHS-HUB-03: Browse catalogue button opens the API catalogue
   - NHS-HUB-04: Four support cards link to the correct destinations
   - NHS-HUB-05: Footer contains all expected sections and links
- NHS-CAT — API catalogue, general
   - NHS-CAT-01: Catalogue page loads with correct title and heading
   - NHS-CAT-02: Total result count is displayed
   - NHS-CAT-03: Result cards show title, status and taxonomy tags
   - NHS-CAT-04: Catalogue search returns relevant results
   - NHS-CAT-05: Catalogue search with no matches shows an empty state
   - NHS-CAT-06: Catalogue search handles special characters
   - NHS-CAT-07: Alphabet letter with results filters the catalogue
   - NHS-CAT-08: Alphabet letters without results are not links
- NHS-FLT — catalogue filters
   - NHS-FLT-01: All filter groups are displayed with result counters
   - NHS-FLT-02: Applying a filter narrows the result set
   - NHS-FLT-03: Result count matches the filter counter
   - NHS-FLT-04: Two filters can be combined
   - NHS-FLT-05: Reset filters clears all applied filters
- NHS-PAG — catalogue pagination
   - NHS-PAG-01: Pagination controls are displayed and first page is default
   - NHS-PAG-02: Navigating to page 2 loads a different result set
   - NHS-PAG-03: Last page is reachable and loads results
- NHS-API — individual API pages
   - NHS-API-01: API page loads with correct heading and description
   - NHS-API-02: API page displays a status badge
   - NHS-API-03: Taxonomy tags link back to filtered catalogue views
- NHS-A11Y — accessibility
   - NHS-A11Y-01: Skip to main content link works
   - NHS-A11Y-02: Images have alt attributes
   - NHS-A11Y-03: Heading levels are not skipped
   - NHS-A11Y-04: Landmark regions are present
   - NHS-A11Y-05: No critical axe-core violations on the hub page
   - NHS-A11Y-06: No critical axe-core violations on the catalogue page

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

### NHS-NAV-05: Mobile menu opens and closes at narrow viewport

Area: Global navigation
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state. Viewport set to a mobile width
(for example 375 x 812).

Steps:
1. Open https://digital.nhs.uk/developer at a mobile viewport
2. Activate the "Menu" control
3. Activate the "Close menu" control

Expected result:
At a narrow viewport the primary navigation is collapsed behind a menu control.
Activating "Menu" reveals the navigation links. Activating "Close menu" hides them again.

Automated test: tests/test_navigation.py::test_mobile_menu_toggle

---

### NHS-NAV-06: Breadcrumbs on an API page show four levels

Area: Breadcrumbs
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open a specific API page under https://digital.nhs.uk/developer/api-catalogue/

Expected result:
Breadcrumbs show four levels: "NHS Digital" → "Developer" → "API and integration
catalogue" → API name. The first three are links, the last is the current page and is
not a link.

Automated test: tests/test_navigation.py::test_api_page_breadcrumbs

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

### NHS-HUB-05: Footer contains all expected sections and links

Area: Footer
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Inspect the footer

Expected result:
The footer contains a "Legal" section and a "Get in touch" section. The Legal section
includes an "Accessibility" link. Social media links (Twitter, LinkedIn, YouTube) are
present with correct hrefs. External links point to their expected destinations.

External links are verified by href only; navigation is not performed.

Automated test: tests/test_footer.py::test_footer_sections_and_links

---

### NHS-CAT-01: Catalogue page loads with correct title and heading

Area: API catalogue
Priority: High
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue

Expected result:
Page title contains "API and integration catalogue".
The page has exactly one level 1 heading with the text "API and integration catalogue".

Automated test: tests/test_catalogue.py::test_catalogue_title_and_heading

---

### NHS-CAT-02: Total result count is displayed

Area: API catalogue
Priority: High
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Locate the results summary

Expected result:
A total result count is displayed (for example "188 results"). The number is greater
than zero.

Automated test: tests/test_catalogue.py::test_total_result_count_is_shown

---

### NHS-CAT-03: Result cards show title, status and taxonomy tags

Area: API catalogue
Priority: High
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Inspect the first result card

Expected result:
Each result card contains a title rendered as a link to an individual API page,
at least one status badge (for example "In production"), and one or more taxonomy tags.

Automated test: tests/test_catalogue.py::test_result_card_structure

---

### NHS-CAT-04: Catalogue search returns relevant results

Area: API catalogue
Priority: High
Technique: Equivalence partitioning
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Enter a known term into the catalogue search (for example "booking")
3. Submit the search

Expected result:
The result set updates to show entries related to the search term. At least one result
is returned, and visible results contain the search term in their title or description.

Automated test: tests/test_catalogue.py::test_search_returns_relevant_results

---

### NHS-CAT-05: Catalogue search with no matches shows an empty state

Area: API catalogue
Priority: High
Technique: Equivalence partitioning
Type: Negative

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Enter a term with no expected matches (for example "zzzznomatch")
3. Submit the search

Expected result:
The page displays a zero or empty result state without errors. The application does not
crash and the page structure remains intact.

Automated test: tests/test_catalogue.py::test_search_no_results_state

---

### NHS-CAT-06: Catalogue search handles special characters

Area: API catalogue
Priority: Medium
Technique: Error guessing
Type: Negative

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Enter special characters into the search (for example "!!!@@@###")
3. Submit the search

Expected result:
The page handles the input gracefully. A valid results page or empty state is shown,
with no unhandled error and no broken layout.

Automated test: tests/test_catalogue.py::test_search_special_characters

---

### NHS-CAT-07: Alphabet letter with results filters the catalogue

Area: Alphabetical navigation
Priority: High
Technique: Equivalence partitioning
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Click the letter "A" in the quick navigation

Expected result:
The catalogue view updates to entries associated with the letter "A". Results are shown,
and the URL reflects the selected letter.

Automated test: tests/test_catalogue.py::test_alphabet_letter_with_results

---

### NHS-CAT-08: Alphabet letters without results are not links

Area: Alphabetical navigation
Priority: High
Technique: Equivalence partitioning
Type: Negative

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Inspect the quick navigation letters J, K, X, Y, Z

Expected result:
Letters that have no associated entries are rendered as plain text, not as clickable
links.

Automated test: tests/test_catalogue.py::test_empty_alphabet_letters_not_clickable
### NHS-FLT-01: All filter groups are displayed with result counters

Area: Catalogue filters
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Inspect the filters panel

Expected result:
The filter groups are displayed (for example Business function, Care setting,
Integration type, Technology, Status, Owner). Each filter value shows a numeric result
counter in the form "Name (count)".

Automated test: tests/test_filters.py::test_filter_groups_and_counters_present

---

### NHS-FLT-02: Applying a filter narrows the result set

Area: Catalogue filters
Priority: High
Technique: Equivalence partitioning
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Note the total result count
3. Apply the Status filter "In production"

Expected result:
The result set updates and shows fewer or equal results than the unfiltered total.
The URL reflects the applied filter.

Automated test: tests/test_filters.py::test_applying_filter_narrows_results

---

### NHS-FLT-03: Result count matches the filter counter

Area: Catalogue filters
Priority: High
Technique: Data consistency
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Read the counter shown next to the Technology filter "FHIR" (for example "FHIR (80)")
3. Apply that filter
4. Read the total result count on the filtered page

Expected result:
The total result count on the filtered page matches the number shown in the filter
counter.

Note: the comparison is made between the counter and the actual filtered result total
on the same run, not against a hard-coded number, because catalogue contents change
over time.

Automated test: tests/test_filters.py::test_counter_matches_filtered_result_count

---

### NHS-FLT-04: Two filters can be combined

Area: Catalogue filters
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Apply the Status filter "In production"
3. Apply the Technology filter "FHIR"

Expected result:
Both filters are applied simultaneously. The result set reflects entries matching both
criteria, and the result count is less than or equal to the count for either filter
applied alone.

Automated test: tests/test_filters.py::test_two_filters_combined

---

### NHS-FLT-05: Reset filters clears all applied filters

Area: Catalogue filters
Priority: High
Technique: State transition
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Apply one or more filters
3. Click "Reset filters"

Expected result:
All filters are cleared. The result set returns to the full unfiltered total, and the
URL no longer contains filter parameters.

Automated test: tests/test_filters.py::test_reset_filters_clears_all

---

### NHS-PAG-01: Pagination controls are displayed and first page is default

Area: Catalogue pagination
Priority: High
Technique: Boundary value analysis
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Inspect the pagination controls

Expected result:
Pagination controls are displayed with multiple page numbers. The first page is the
active page on initial load.

Automated test: tests/test_pagination.py::test_pagination_present_first_page_default

---

### NHS-PAG-02: Navigating to page 2 loads a different result set

Area: Catalogue pagination
Priority: High
Technique: Boundary value analysis
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Record the first result title on page 1
3. Navigate to page 2

Expected result:
The result set changes: the first result title on page 2 differs from page 1. The page
number is reflected in the URL.

Automated test: tests/test_pagination.py::test_page_two_loads_different_results

---

### NHS-PAG-03: Last page is reachable and loads results

Area: Catalogue pagination
Priority: High
Technique: Boundary value analysis
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Navigate to the last available page (for example page 10)

Expected result:
The last page loads successfully and displays at least one result. No error is shown.

Automated test: tests/test_pagination.py::test_last_page_loads_results

---

### NHS-API-01: API page loads with correct heading and description

Area: Individual API pages
Priority: High
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state. A stable API in production
status is selected.

Steps:
1. Open a selected API page under https://digital.nhs.uk/developer/api-catalogue/

Expected result:
The page has exactly one level 1 heading containing the API name. A description
paragraph is present below the heading.

Automated test: tests/test_api_page.py::test_api_page_heading_and_description

---

### NHS-API-02: API page displays a status badge

Area: Individual API pages
Priority: High
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state. A stable API in production
status is selected.

Steps:
1. Open the selected API page

Expected result:
A status badge is displayed (for example "In production"). The status is one of the
documented catalogue statuses.

Automated test: tests/test_api_page.py::test_api_page_status_badge

---

### NHS-API-03: Taxonomy tags link back to filtered catalogue views

Area: Individual API pages
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state. A stable API in production
status is selected.

Steps:
1. Open the selected API page
2. Inspect the taxonomy tags
3. Activate one taxonomy tag

Expected result:
Taxonomy tags are rendered as links. Activating a tag opens a filtered catalogue view
for that taxonomy, and the resulting page shows the filter applied.

Automated test: tests/test_api_page.py::test_taxonomy_tag_links_to_catalogue

---

### NHS-A11Y-01: Skip to main content link works

Area: Accessibility
Priority: High
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Locate the "Skip to main content" link
3. Activate it

Expected result:
A "Skip to main content" link is present. Activating it moves focus to the main content
region, so keyboard users can bypass the navigation.

Automated test: tests/test_accessibility.py::test_skip_to_main_content

---

### NHS-A11Y-02: Images have alt attributes

Area: Accessibility
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Inspect content images

Expected result:
Content images have an alt attribute. Decorative images have an empty alt attribute
rather than a missing one.

Automated test: tests/test_accessibility.py::test_images_have_alt

---

### NHS-A11Y-03: Heading levels are not skipped

Area: Accessibility
Priority: Medium
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Inspect the heading structure

Expected result:
The page has a single level 1 heading. Heading levels increase by one step at a time
and do not skip levels (for example an h2 is not followed directly by an h4).

Automated test: tests/test_accessibility.py::test_heading_levels_not_skipped

---

### NHS-A11Y-04: Landmark regions are present

Area: Accessibility
Priority: High
Technique: Checklist-based
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Inspect landmark regions

Expected result:
The page exposes the expected landmark regions: banner, main, contentinfo and at least
one navigation landmark.

Automated test: tests/test_accessibility.py::test_landmark_regions_present

---

### NHS-A11Y-05: No critical axe-core violations on the hub page

Area: Accessibility
Priority: High
Technique: Tool-based audit
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer
2. Run an axe-core scan

Expected result:
The axe-core scan reports no violations of critical or serious impact.
Lower-impact findings are recorded but do not fail the test.

Automated test: tests/test_accessibility.py::test_axe_scan_hub_page

---

### NHS-A11Y-06: No critical axe-core violations on the catalogue page

Area: Accessibility
Priority: High
Technique: Tool-based audit
Type: Positive

Preconditions: Consent state pre-set via storage_state.

Steps:
1. Open https://digital.nhs.uk/developer/api-catalogue
2. Run an axe-core scan

Expected result:
The axe-core scan reports no violations of critical or serious impact.
Lower-impact findings are recorded but do not fail the test.

Automated test: tests/test_accessibility.py::test_axe_scan_catalogue_page

---