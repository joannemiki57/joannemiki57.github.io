# joannemiki57.github.io

Personal academic site for Junghyun (Joanne) Yun. Layout follows the al-folio Jekyll theme, recolored in UW–Madison red (#C5050C). Plain static HTML, no Jekyll or Ruby needed.

## Edit

All text lives in `_build/build.py` (the CONTENT section at the top). Change it, then regenerate:

```
python3 _build/build.py
```

Images are in `assets/img/`, the CV and poster PDFs in `assets/pdf/`.

## Preview locally

```
python3 -m http.server 4321 --directory .
```

Then open http://localhost:4321.

## Deploy

Served by GitHub Pages from `main` (root).
