# Edmund Dyer-Essig — portfolio

An eight-page static portfolio for GitHub Pages. No build step or third-party runtime dependencies. The homepage uses a small optional JavaScript scroll introduction; navigation and content work without JavaScript.

## Preview and check
Open index.html in a browser or run `python3 -m http.server 8000` from this directory.

Run `python3 tests/check_site.py`, `node --check home.js`, and `node tests/check_home.cjs` to check internal links/anchors, navigation, metadata, sitemap, and animation behavior. Animation tests use browser-API stubs; they do not replace real desktop/mobile browser testing.

## Pages
- index.html — introduction, role-relevant project links, selected work, public evidence, contact
- projects.html — project index
- ai-security.html, radar.html, sustainability.html — contribution summaries
- experience.html — education, experience, leadership, skills
- writing.html — published essay and credited research contribution
- about.html — background and interests

## Editing and publishing
Edit the HTML directly. Navigation/footer are repeated across all eight pages; update them consistently. styles.css controls the design; home.js controls the homepage animation. Review changes on a branch before merging into the GitHub Pages publishing branch. This change does not modify Pages settings.

## Content sources and limits
Existing roles, dates, skills, and contributions come from the original supplied portfolio. New public references:
- https://blogs.cisco.com/ai/security-framework-v2 — September 2026; credits Edmund for research and development assistance, not authorship.
- https://stanfordmag.org/contents/stem-education — personal essay by Edmund, Spring 2026.

Copy is a starting draft for Edmund to revise. Robotics is presented as an interest. No NAT title or work details have been inferred from email. No private course, calendar, or inbox content is published.

Before publishing, review current titles and dates; add an approved résumé PDF and relevant original project images when available. The site deliberately contains no placeholder résumé download or invented results. No portrait/photo was included in the original upload.

## Motion and accessibility
The introduction briefly stays in place while native scrolling moves the text and qualifications panel. The skip-to-work link bypasses the opening. Reduced-motion preferences, short screens, and missing JavaScript fall back to normal scrolling. Content never depends on animation to become visible.

## Validation limitations
Browser installation was blocked by the editing environment. Desktop/mobile visual checks, keyboard walkthrough, and performance measurements remain outstanding before publication. The automated checks do not claim to validate external links or real browser layout.
