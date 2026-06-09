# GitHub Pages Deployment

Based on [codepo8/hosting-on-github-template](https://github.com/codepo8/hosting-on-github-template).

## Quick Setup

1. Create a GitHub repository (or use an existing one).
2. Push the contents of `Webseite/site/` to the `main` branch root.
3. In **Settings → Pages**:
   - Source: **Deploy from a branch**
   - Branch: `main`, folder: **/ (root)**
4. Wait for the Actions build to finish (green checkmark).
5. Site URL: `https://{username}.github.io/{repository}/`

## Static Files

Any `.html`, `.css`, `.js`, image, or video in the repo root is served directly. No build step required.

Add `.nojekyll` (already included) if you use folders starting with `_` or want to bypass Jekyll processing.

## Optional: PWA / Offline

See `_refs/github-page-pwa/` and the `github-page-pwa` skill. Requires:

- `manifest.webmanifest` with correct `scope` and `start_url` (include repo name path)
- `sw.js` service worker with `GHPATH = '/{repository-name}'`
- Service worker registration in `index.html`

## Optional: Markdown Pages

GitHub Pages can render Markdown with custom `_layouts/` templates. See the hosting-on-github-template repo for Jekyll layout examples.
