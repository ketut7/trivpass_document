from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
KONTEN = ROOT / "konten"
OUT = ROOT / "assets"

OFF_WHITE = (250, 247, 242)
CARD = (245, 241, 233)
INK = (27, 29, 27)
JUNGLE = (31, 77, 58)
TERRACOTTA = (194, 96, 62)
MUTED = (122, 122, 112)
LINE = (226, 221, 212)

GEORGIA = "/System/Library/Fonts/Supplemental/Georgia.ttf"
GEORGIA_BOLD = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def tracking(draw, xy, text, fnt, fill, tracking=0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking


def text_right(draw, right, y, text, fnt, fill):
    draw.text((right - draw.textlength(text, font=fnt), y), text, font=fnt, fill=fill)


def redraw_cover():
    img = Image.open(KONTEN / "1.png").convert("RGB")
    draw = ImageDraw.Draw(img)

    # Rebuild the existing pass card so updated pricing does not leave text ghosts.
    mask = Image.new("L", img.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    card_box = (30, 970, 1055, 1238)
    mask_draw.rounded_rectangle(card_box, radius=12, fill=255)
    # Ticket notches at the perforation.
    mask_draw.ellipse((848, 948, 890, 990), fill=0)
    mask_draw.ellipse((848, 1218, 890, 1260), fill=0)
    card_layer = Image.new("RGB", img.size, CARD)
    img.paste(card_layer, (0, 0), mask)
    draw = ImageDraw.Draw(img)

    # Reuse exact logo and QR from the user's design.
    source = Image.open(KONTEN / "1.png").convert("RGB")
    logo = source.crop((74, 998, 241, 1031))
    qr = source.crop((918, 1098, 1005, 1186))
    img.paste(logo, (74, 998))
    img.paste(qr, (918, 1098))

    # Perforation and card text.
    dash_y = 990
    while dash_y < 1220:
        draw.line((868, dash_y, 868, dash_y + 10), fill=(202, 199, 191), width=2)
        dash_y += 18

    eyebrow = font(ARIAL_BOLD, 22)
    title = font(GEORGIA, 50)
    price = font(ARIAL, 40)
    meta = font(ARIAL, 24)
    stub = font(ARIAL_BOLD, 13)

    tracking(draw, (75, 1048), "ATTRACTION · WATER PARKS", eyebrow, TERRACOTTA, tracking=4)
    draw.text((75, 1083), "Waterbom Bali", font=title, fill=JUNGLE)
    tracking(draw, (75, 1150), "From IDR 563,000 / Adult", price, TERRACOTTA, tracking=5)
    draw.text((75, 1198), "Selected-date price · Non-Indonesian ID", font=meta, fill=MUTED)
    tracking(draw, (913, 1050), "ADMIT ONE", stub, JUNGLE, tracking=2)

    OUT.mkdir(parents=True, exist_ok=True)
    img.save(OUT / "waterbom-slide-01-cover-discount.png", quality=95)


def redraw_tier(source, output, eyebrow, rows, note, photo_crop_box):
    img = Image.open(source).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Preserve the photo area; rebuild the lower panel to avoid text ghosts.
    photo = img.crop(photo_crop_box)
    canvas = Image.new("RGB", (1080, 1350), OFF_WHITE)
    canvas.paste(photo.resize((1080, 770), Image.Resampling.LANCZOS), (0, 0))
    draw = ImageDraw.Draw(canvas)

    eyebrow_font = font(ARIAL_BOLD, 22)
    title_font = font(GEORGIA, 68)
    label_font = font(ARIAL, 34)
    price_font = font(ARIAL_BOLD, 34)
    note_font = font(ARIAL, 22)

    tracking(draw, (90, 840), eyebrow, eyebrow_font, TERRACOTTA, tracking=3)
    draw.text((90, 894), "Single Day Pass", font=title_font, fill=JUNGLE)

    y_line = 1004
    for label, price in rows:
        draw.line((90, y_line, 990, y_line), fill=LINE, width=2)
        draw.text((109, y_line + 28), label, font=label_font, fill=INK)
        text_right(draw, 950, y_line + 28, price, price_font, TERRACOTTA)
        y_line += 84
    draw.line((90, y_line, 990, y_line), fill=LINE, width=2)

    draw.text((109, 1288), note, font=note_font, fill=MUTED)

    # Reuse the logo from the user's original design so this matches the set.
    logo = Image.open(KONTEN / "2.png").convert("RGB").crop((819, 1283, 991, 1325))
    canvas.paste(logo, (819, 1283))

    OUT.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT / output, quality=95)


def main():
    redraw_cover()
    redraw_tier(
        KONTEN / "2.png",
        "waterbom-slide-02-international-discount.png",
        "TICKET · NON-INDONESIAN ID HOLDER",
        [
            ("Adult", "From IDR 563,000"),
            ("Child (2–11)", "From IDR 457,000"),
            ("Family (2A + 2C)", "From IDR 2,062,000"),
        ],
        "Current selected-date price · Park entry included",
        (0, 0, 1080, 770),
    )
    redraw_tier(
        KONTEN / "3.png",
        "waterbom-slide-03-indonesian-id-discount.png",
        "TICKET · INDONESIAN ID HOLDER",
        [
            ("Adult", "From IDR 343,000"),
            ("Child (2–11)", "From IDR 302,000"),
            ("Family (2A + 2C)", "From IDR 1,300,000"),
        ],
        "Show your KTP at booking · Selected-date price",
        (0, 0, 1080, 770),
    )


if __name__ == "__main__":
    main()
