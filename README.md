# Contact QR Maker

Make a QR code for your contact details. Scan it with a phone camera to save the contact.

**Try it: https://bernysk.github.io/qr_contact_generator/**

- **vCard 3.0** (all fields, works on iPhone and Android) or **MeCard** (smaller code)
- Name with academic titles before and after (stored in the vCard honorific prefix and suffix, shown as
  "Ing. Jana Nováková, PhD."), company, job title, phones, email, website, address, note; full UTF-8 (č, š, ž …)
- Styles: square, rounded, soft, classy, vertical or horizontal bars, small squares, dots or diamonds; corner frame
  (square, rounded, circle, leaf) and corner center (square, rounded, circle, leaf, diamond) set separately.
  Shapes and corner combinations that failed decode tests show a warning
- Colors: 19 tested color presets (7 from the brand palette), or your own solid color or gradient: linear at any
  angle or radial from any point and size, with 2 to 4 colors, plus an optional separate color for the corner squares. Warns when red ink could vanish under the red light
  of handheld scanners
- Several contacts: download a CSV template, fill it in Excel or Google Sheets, import it, edit contacts in a list,
  export the list as CSV, and download every code at once as a ZIP (PNG and/or SVG, plus .vcf files)
- Optional logo in the middle (PNG, JPG or SVG), with adjustable size; error correction switches to H.
  With a transparent PNG or SVG the code wraps around the logo's shape, or pick a square background.
  Empty margins in the logo file are trimmed automatically, and wide or tall logos get a matching box
- Scan check: every code is decoded in the page at five sizes, the way a phone camera sees it, and the result is
  shown next to the code; the ZIP export lists any codes that fail
- Field checks: phone numbers get the chosen country's code (e.g. `0905 333 444` becomes `+421 905 333 444`).
  All 245 calling codes from Wikipedia's list, grouped by ITU zone, with flags; the address country is
  suggested at the top of the list but never changes the choice by itself. The conversion can be switched off
  to keep numbers exactly as typed,
  and emails, websites and numbers that look wrong are highlighted
- Print-size hint: shows the smallest width the code can be printed at, and warns when it is too dense for a business card
- Download PNG, SVG or a `.vcf` contact file; or copy the image, SVG or contact text
- English and Slovak interface (follows your browser language, switch in the top corner)

## Privacy

Everything runs in your browser. There is no server, no tracking and no external requests:
the QR libraries are bundled in this repo (`qrcode.min.js`, `jsQR.js`). Nothing you type is sent anywhere.

If you tick **Remember my details in this browser**, your fields, style choices and logo are saved in
your browser's local storage on that device only, and filled in next time. Untick it to delete them.

## Run locally

Download or clone the repo and open `index.html` in any browser. No install, no build step,
and it works offline.

```bash
git clone https://github.com/bernysk/qr_contact_generator.git
```

## Development

`index.html` is generated, so don't edit it directly. The source is `src/contact-qr.html`:

1. Edit `src/contact-qr.html`.
2. Run `python build.py` to regenerate `index.html` (Python 3, no packages needed).
3. Commit both files. A GitHub Action runs `python build.py --check` and fails if they don't match.

The source is written for the claude.ai artifact viewer: it loads the QR libraries from a CDN and has downloads
switched off, because the viewer blocks them. `build.py` turns it into the standalone, offline page: it adds the
HTML skeleton, uses the bundled libraries, drops the web font, and switches downloads on.

## Credits

QR encoding by [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator)
by Kazuhiko Arase, MIT license. QR reading for the scan check by [jsQR](https://github.com/cozmo/jsQR), Apache-2.0 license.
Flag emoji on Windows by [Twemoji Country Flags](https://github.com/talkjs/country-flag-emoji-polyfill) (MIT),
with flag art from [Twemoji](https://github.com/twitter/twemoji), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
embedded unchanged in the page.
