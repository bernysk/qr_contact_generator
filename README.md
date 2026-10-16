# Contact QR Maker

Make a QR code for your contact details. Scan it with a phone camera to save the contact.

**Try it: https://bernysk.github.io/qr_contact_generator/**

- **vCard 3.0** (all fields, works on iPhone and Android) or **MeCard** (smaller code)
- Name, company, job title, phones, email, website, address, note; full UTF-8 (č, š, ž …)
- Styles: square, rounded (connected) or dot modules, with square or rounded corner squares
- Optional logo in the middle (PNG, JPG or SVG), with adjustable size; error correction switches to H
- Error correction level, colors with contrast check, image size up to 2048 px
- Copy as PNG, copy as SVG, or right-click the code to save the image

## Privacy

Everything runs in your browser. There is no server, no tracking and no external requests:
the QR library is bundled in this repo (`qrcode.min.js`). Nothing you type is sent anywhere.

If you tick **Remember my details in this browser**, your fields, style choices and logo are saved in
your browser's local storage on that device only, and filled in next time. Untick it to delete them.

## Run locally

Download or clone the repo and open `index.html` in any browser. No install, no build step,
and it works offline.

```bash
git clone https://github.com/bernysk/qr_contact_generator.git
```

## Credits

QR encoding by [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator)
by Kazuhiko Arase, MIT license.
