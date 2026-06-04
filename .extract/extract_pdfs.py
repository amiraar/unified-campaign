import os
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"d:/dungeon and dragons")
OUT = ROOT / ".extract" / "pdf_text"

pdf_paths = sorted(ROOT.rglob("*.pdf"))

for pdf_path in pdf_paths:
    rel = pdf_path.relative_to(ROOT)
    out_path = OUT / rel
    out_path = out_path.with_suffix(".txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        reader = PdfReader(str(pdf_path))
        text_parts = []
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text_parts.append(page_text)
        text = "\n\n".join(text_parts)
    except Exception as exc:
        text = f"[EXTRACTION_ERROR] {exc}\n"

    out_path.write_text(text, encoding="utf-8")

manifest_path = OUT / "_manifest.txt"
manifest_lines = [str(p.relative_to(ROOT)) for p in pdf_paths]
manifest_path.write_text("\n".join(manifest_lines), encoding="utf-8")
