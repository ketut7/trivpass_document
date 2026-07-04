#!/usr/bin/env python3
"""Build SOP-Driver-Trivpass PDF from the markdown source.
Usage: python3 build-sop-pdf.py
Pipeline: markdown -> HTML (branded CSS) -> wkhtmltopdf body -> reportlab cover -> pypdf merge.
Includes a fix for a wkhtmltopdf bug that drops spaces adjacent to inline <strong>/<em>/<code>
tags (the space is moved INSIDE the tag so there is no boundary space to drop)."""
import os, pathlib, markdown
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color, white
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader, PdfWriter

HERE = pathlib.Path(__file__).parent
MD   = HERE / "SOP-Driver-Trivpass-v1.0.md"
OUT  = HERE / "SOP-Driver-Trivpass-v1.0.pdf"
LOGO = "/Users/ketutsuryada/AI/Claude/Trivpass/brand/logo/icon-square.png"

body = markdown.markdown(MD.read_text(encoding="utf-8"),
                         extensions=["tables","fenced_code","sane_lists","nl2br","attr_list"])
# wkhtmltopdf space-eating fix: pin boundary spaces with a literal non-breaking
# space (U+00A0), which wkhtmltopdf preserves where it drops a normal space.
NB = " "
for t in ("strong","em","code"):
    body = body.replace(f" <{t}>", f"{NB}<{t}>").replace(f"</{t}> ", f"</{t}>{NB}")

CSS = """@page{size:A4;margin:0;} *{box-sizing:border-box;}
body{font-family:Arial,'Liberation Sans',sans-serif;color:#2b2b28;font-size:11.5px;line-height:1.55;word-spacing:2px;}
h1{color:#1f4d3a;font-size:23px;margin:0 0 10px;border-bottom:3px solid #1f4d3a;padding-bottom:8px;}
h2{color:#1f4d3a;font-size:15.5px;margin:24px 0 8px;border-bottom:1px solid #d9cfc2;padding-bottom:4px;}
h3{color:#c2603e;font-size:13px;margin:16px 0 6px;}
p{margin:7px 0;} ul,ol{margin:7px 0;padding-left:22px;} li{margin:4px 0;padding-left:2px;}
strong{color:#1b1b18;}
blockquote{border-left:4px solid #c2603e;background:#faf7f2;margin:10px 0;padding:8px 14px;color:#4a463f;} blockquote p{margin:3px 0;}
table{border-collapse:collapse;width:100%;margin:10px 0;font-size:10.8px;}
th{background:#1f4d3a;color:#fff;text-align:left;padding:7px 9px;border:1px solid #1f4d3a;}
td{padding:6px 9px;border:1px solid #d9cfc2;vertical-align:top;} tr:nth-child(even) td{background:#faf7f2;}
code{background:#f0ece4;padding:1px 4px;border-radius:3px;font-size:10.5px;}
hr{border:none;border-top:1px solid #e3dccf;margin:18px 0;}
.foot{margin-top:22px;padding-top:9px;border-top:1px solid #d9cfc2;color:#9a9388;font-size:9px;}"""
html = f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}<div class="foot">Trivpass · SOP Driver · Versi 1.0 · dokumen internal</div></body></html>'
(HERE/"_sop.html").write_text(html, encoding="utf-8")
os.system(f'wkhtmltopdf --quiet --enable-local-file-access --encoding utf-8 '
          f'--margin-top 30 --margin-bottom 30 --margin-left 18 --margin-right 18 '
          f'"{HERE/"_sop.html"}" "{HERE/"_body.pdf"}"')

# --- cover ---
W,H=A4; G=Color(31/255,77/255,58/255); T=Color(194/255,96/255,62/255); GR=Color(107/255,100/255,89/255)
c=canvas.Canvas(str(HERE/"_cover.pdf"),pagesize=A4)
c.setFillColor(G); c.rect(0,H-16,W,16,fill=1,stroke=0); c.rect(0,0,W,34,fill=1,stroke=0)
c.drawImage(ImageReader(LOGO),(W-150)/2,H-330,width=150,height=150,mask='auto',preserveAspectRatio=True)
c.setFillColor(G); c.setFont("Helvetica-Bold",13); c.drawCentredString(W/2,H-360,"T R I V P A S S")
c.setStrokeColor(T); c.setLineWidth(2.5); c.line(W/2-40,H-378,W/2+40,H-378)
c.setFillColor(G); c.setFont("Helvetica-Bold",40); c.drawCentredString(W/2,H-430,"SOP DRIVER")
c.setFillColor(GR); c.setFont("Helvetica",13); c.drawCentredString(W/2,H-456,"Standard Operating Procedure  ·  Roster Driver")
c.setFont("Helvetica-Oblique",11); c.drawCentredString(W/2,H-476,"Kepatuhan Rute  ·  Keselamatan  ·  Layanan")
c.setStrokeColor(Color(0.85,0.82,0.76)); c.setLineWidth(0.8); c.line(W/2-150,210,W/2+150,210)
c.setFillColor(GR); c.setFont("Helvetica",11); c.drawCentredString(W/2,188,"Versi 1.0  —  Juni 2026"); c.drawCentredString(W/2,170,"Disusun oleh Trivpass")
c.setFont("Helvetica-Bold",10.5); c.setFillColor(T); c.drawCentredString(W/2,148,"DOKUMEN INTERNAL · RAHASIA")
c.setFillColor(white); c.setFont("Helvetica-Bold",10); c.drawCentredString(W/2,12.5,"Real drivers. Real prices. No surprises.")
c.showPage(); c.save()

w=PdfWriter(); w.add_page(PdfReader(str(HERE/"_cover.pdf")).pages[0])
for p in PdfReader(str(HERE/"_body.pdf")).pages: w.add_page(p)
with open(OUT,"wb") as f: w.write(f)
for x in ("_sop.html","_body.pdf","_cover.pdf"): (HERE/x).unlink(missing_ok=True)
print("Built", OUT.name, "-", len(PdfReader(str(OUT)).pages), "pages")
