# Changelog

All notable changes to Contact QR Maker, newest first. The project has no version numbers yet, so changes are
grouped by day. Each entry links to the commit that made it.

## 2026-10-18

### Added
- **Middle name** field. It goes into the vCard name field (third part), the display name, the MeCard first-name
  part and a new `middle_name` CSV column; imports also accept headers such as "Middle name" or "Druhé meno".
  ([2f50bfd](https://github.com/bernysk/qr_contact_generator/commit/2f50bfd))

### Changed
- **Leave titles out (for Android)** replaces "Show titles on Android phones". Phone tests showed Android reads the
  structured name, joins it into one line and only recognises English prefixes, so a Slovak title such as "Ing."
  lands in the first name ("Ing. Jana") wherever it is in the code. The new option, off by default, removes the
  titles from the code entirely; the page preview still shows them.
  ([2f50bfd](https://github.com/bernysk/qr_contact_generator/commit/2f50bfd))
- Name fields sit on two lines on desktop, so short titles aren't cut off.
  ([2f50bfd](https://github.com/bernysk/qr_contact_generator/commit/2f50bfd))

## 2026-10-17

### Added
- **Built-in scan check.** Every code is decoded in the page at five sizes, the way a phone camera sees it, and the
  result is shown first among the chips. The ZIP export names any codes that fail.
  ([0e556ea](https://github.com/bernysk/qr_contact_generator/commit/0e556ea))
- **Field checks.** Phone numbers get the chosen country's code (`0905 333 444` becomes `+421 905 333 444`), and
  emails, websites and numbers that look wrong are highlighted. Websites without `https://` get it in the code.
  ([0e556ea](https://github.com/bernysk/qr_contact_generator/commit/0e556ea))
- **All 245 country calling codes**, checked against Wikipedia, grouped by ITU zone, named in the page language and
  shown with flags (also on Windows, through an embedded Twemoji flag font). The address country is suggested at
  the top of the list without changing the choice.
  ([d88c776](https://github.com/bernysk/qr_contact_generator/commit/d88c776))
- **Switch to keep phone numbers as typed** instead of adding the country code.
  ([a71f279](https://github.com/bernysk/qr_contact_generator/commit/a71f279))
- **Academic titles** before and after the name, stored as the vCard honorific prefix and suffix, with
  `title_before` and `title_after` CSV columns.
  ([7d48adc](https://github.com/bernysk/qr_contact_generator/commit/7d48adc))
- **Adjustable gradients.** A direction slider for linear gradients, a center and size for radial ones, and 2–4
  colors; every color is included in the contrast and red-ink checks.
  ([4a0237a](https://github.com/bernysk/qr_contact_generator/commit/4a0237a))
- **More shapes.** Soft, classy, vertical and horizontal bars, small squares and diamonds, plus separate corner
  frame and corner center shapes. Shapes and corner combinations that failed decode tests show a warning.
  ([86fcbf0](https://github.com/bernysk/qr_contact_generator/commit/86fcbf0))
- **Color presets.** 12 combinations, each tested for contrast and decoded at 250–800 px, plus 7 presets from the
  brand palette (aubergine, red, teal, slate), shown first under "Your palette".
  ([86fcbf0](https://github.com/bernysk/qr_contact_generator/commit/86fcbf0),
  [9e77d65](https://github.com/bernysk/qr_contact_generator/commit/9e77d65))
- **Red-ink warning**, since handheld scanners read codes under red light and red ink can vanish.
  ([9e77d65](https://github.com/bernysk/qr_contact_generator/commit/9e77d65))
- **Several contacts.** CSV template, CSV import (English or Slovak headers, comma or semicolon), a contact list
  edited in the form, CSV export, and a ZIP with a PNG, SVG and `.vcf` for every contact.
  ([86fcbf0](https://github.com/bernysk/qr_contact_generator/commit/86fcbf0))
- **Source and build script** in the repo (`src/contact-qr.html`, `build.py`), a GitHub Action that checks
  `index.html` is up to date, and Development notes in the README. The source was added to every earlier commit.
  ([9f6aa1a](https://github.com/bernysk/qr_contact_generator/commit/9f6aa1a))

### Changed
- **vCard text without escapes.** Google's "Add to contacts" on a Pixel showed escape characters literally
  (`Nováková\, PhD.`). Commas now stay plain, a semicolon becomes a comma (except between company and department),
  a line break becomes ", " and a backslash "/".
  ([1981210](https://github.com/bernysk/qr_contact_generator/commit/1981210),
  [c3bf18e](https://github.com/bernysk/qr_contact_generator/commit/c3bf18e))
- **Display name and titles on Android.** First the display name was reduced to first and last name, because Google
  split "prof. MUDr. Jana Nováková, PhD., MBA" into first name "MUDr. Jana" and surname "PhD"; then a "Show titles
  on Android phones" setting brought the titles back as an option. Both were superseded on 2026-10-18.
  ([c3bf18e](https://github.com/bernysk/qr_contact_generator/commit/c3bf18e),
  [fb6c741](https://github.com/bernysk/qr_contact_generator/commit/fb6c741))

### Fixed
- A line break in an imported CSV cell could add a hidden line, such as an extra phone number, to that contact's
  code and `.vcf` file. Imported fields other than the note are now single-line, and line breaks and control
  characters never reach the code.
  ([14ef57d](https://github.com/bernysk/qr_contact_generator/commit/14ef57d))
- One bad value in the saved data stopped the page from starting. Saved values are now checked, and a save that
  can't be applied is discarded. ([14ef57d](https://github.com/bernysk/qr_contact_generator/commit/14ef57d))
- MeCard escaped the comma between surname and first name.
  ([14ef57d](https://github.com/bernysk/qr_contact_generator/commit/14ef57d))
- CSV import: an empty column no longer wipes a value an earlier column set, and Outlook's or Google's "Title"
  column is read as the title before the name when a separate "Job Title" column exists.
  ([14ef57d](https://github.com/bernysk/qr_contact_generator/commit/14ef57d))
- The ZIP export, PNG export and file reads show a message when they fail instead of failing silently.
  ([14ef57d](https://github.com/bernysk/qr_contact_generator/commit/14ef57d))

## 2026-10-16

### Added
- **Contact QR Maker**: a single page that turns contact details into a vCard or MeCard QR code entirely in the
  browser, with the QR library bundled so it works offline.
  ([473a68f](https://github.com/bernysk/qr_contact_generator/commit/473a68f))
- Link to the live site in the README. ([555d596](https://github.com/bernysk/qr_contact_generator/commit/555d596))
- **Logo in the middle** (PNG, JPG or SVG). Adding one switches error correction to H, and a chip warns when the
  logo covers too much of the code. ([43cbe71](https://github.com/bernysk/qr_contact_generator/commit/43cbe71))
- **Rounded and dot styles** with rounded corner squares; rounded became the default.
  ([b582d28](https://github.com/bernysk/qr_contact_generator/commit/b582d28))
- **Remember my details in this browser**: an opt-in save of every field, style and the logo.
  ([6118eda](https://github.com/bernysk/qr_contact_generator/commit/6118eda))
- **Downloads** of PNG, SVG and a `.vcf` contact file; a **print-size hint** that warns when the code is too dense
  for a business card; **gradients** and a separate corner color; and an **English and Slovak interface**.
  ([fed295e](https://github.com/bernysk/qr_contact_generator/commit/fed295e))

### Changed
- The code wraps around the logo's own shape instead of a square, and a logo's empty margins are trimmed so wide
  logos come out at a proper size.
  ([6a6e8a0](https://github.com/bernysk/qr_contact_generator/commit/6a6e8a0),
  [c77d5f3](https://github.com/bernysk/qr_contact_generator/commit/c77d5f3))

### Fixed
- Straight quotes in the logo hint broke the page's script.
  ([c77d5f3](https://github.com/bernysk/qr_contact_generator/commit/c77d5f3))
