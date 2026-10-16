"""Build index.html (the GitHub Pages site) from src/contact-qr.html.

src/contact-qr.html is the single source. It is written for the claude.ai artifact viewer, which wraps
the page in <html>/<head>/<body>, blocks downloads, and loads libraries from a CDN. This script turns
it into a standalone page that works offline:

- adds the document skeleton (doctype, charset, viewport, description)
- removes the artifact-only meta tag and the Google Fonts link (no external requests)
- points the QR libraries at the copies bundled in this repo
- switches downloads on (ALLOW_DOWNLOAD = true)

Run with:  python build.py
Check only (used by CI): python build.py --check
"""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src" / "contact-qr.html"
OUT = ROOT / "index.html"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Make a QR code for your contact details (vCard or MeCard). Runs entirely in your browser.">
"""

# CDN script URL in the source -> file bundled in this repo.
LIBS = {
    "https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js": "qrcode.min.js",
    "https://cdn.jsdelivr.net/npm/jsqr@1.4.0/dist/jsQR.js": "jsQR.js",
}

# Base styles the artifact viewer normally provides.
RESET = "img { max-width: 100%; }\n[hidden] { display: none !important; }\nhtml, body { margin: 0; }\n"


def build(src: str) -> str:
    out = []
    for line in src.split("\n"):
        if "claude:viewport-fit-sides" in line or "fonts.googleapis" in line:
            continue
        for url, local in LIBS.items():
            line = line.replace(url, local)
        line = line.replace("const ALLOW_DOWNLOAD = false;", "const ALLOW_DOWNLOAD = true;")
        out.append(line)
        if line == "* { box-sizing: border-box; }":
            out.append(RESET.rstrip("\n"))
        if line == "</style>":
            out.append("</head>\n<body>")
    body = "\n".join(out).rstrip("\n")
    # Early versions of the page had no downloads, so the switch is only required when the source has one.
    must_have = ["</head>"] + (["const ALLOW_DOWNLOAD = true;"] if "ALLOW_DOWNLOAD" in src else [])
    for must in must_have:
        if must not in body:
            sys.exit(f"build.py: expected '{must}' in the output; did the source change shape?")
    return HEAD + body + "\n</body>\n</html>\n"


def main() -> None:
    result = build(SRC.read_text(encoding="utf-8"))
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current.replace("\r\n", "\n") != result:
            sys.exit("index.html is out of date. Run: python build.py")
        print("index.html is up to date.")
        return
    OUT.write_text(result, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT.name} from {SRC.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
