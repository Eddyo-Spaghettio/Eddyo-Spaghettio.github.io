# Edmund Dyer-Essig — personal website

A responsive, seven-page static site for GitHub Pages. No build step, external fonts, or dependencies required. Homepage motion uses a small progressive-enhancement JavaScript file; content and navigation work without JavaScript.

## Preview
Open index.html directly in your browser, or run `python3 -m http.server 8000` in this directory and visit http://localhost:8000.

## Review and publish
Preview this branch locally before merging. GitHub Pages publishes from the repository's configured source branch; merging into that branch may update the live site. This redesign does not change Pages settings.

## Pages
- index.html: concise introduction and selected work
- projects.html: research and project index
- ai-security.html, radar.html, sustainability.html: individual project summaries
- experience.html: education, experience, leadership, and skills
- about.html: background, interests, and Kyoto experience

## Content and editing
Content comes from the uploaded website; project summaries intentionally do not invent results or metrics. Email comes from the résumé contact details shared in the conversation. Review titles, dates, current roles, and contact details before publishing. Shared navigation and footer are ordinary HTML on each page; update all seven pages if changing them.

The archive contained no résumé PDF. The site has an Experience page without a placeholder download link. Add an approved PDF when available. Review dates, titles, current roles, and contact details before publishing.

## Recruiter-focused design
The homepage presents education, Cisco experience, radar research, and technical skills at a glance. Project summaries use concrete contributions. Robotics remains an interest, not an invented work credential. The design uses neutral backgrounds, sans-serif typography, fine rules, and restrained green accents. The landscape illustration has been removed.

## Scroll-controlled opening
On screens with enough vertical space, the introduction stays in place for a short native scroll. The introduction moves upward, the qualifications panel settles into place, and a thin progress rule fills before the project section arrives. No scroll capture or forced timing is used. The homepage offers a direct skip-to-work link and immediate experience/contact links.

Without JavaScript, with reduced motion, or when the introduction does not fit the screen, everything uses normal document scrolling. All content stays visible. home.js is only used on the homepage.

## Validation
Checked all local links, assets, anchor targets, and JavaScript syntax. Browser-API stub tests cover animation progress, boundaries, reduced-motion changes, and short-screen fallback. Browser rendering was unavailable; review desktop/mobile appearance before publishing.
