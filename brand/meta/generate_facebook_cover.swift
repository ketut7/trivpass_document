import AppKit

let width = 1640
let height = 624
let scale = 1.0
let outPath = "brand/meta/trivpass-facebook-cover.png"
let iconPath = "brand/logo/icon-square.png"

let canvas = NSRect(x: 0, y: 0, width: width, height: height)
let image = NSImage(size: canvas.size)

func color(_ hex: String, alpha: CGFloat = 1.0) -> NSColor {
    var clean = hex
    if clean.hasPrefix("#") { clean.removeFirst() }
    let value = Int(clean, radix: 16) ?? 0
    return NSColor(
        calibratedRed: CGFloat((value >> 16) & 0xff) / 255.0,
        green: CGFloat((value >> 8) & 0xff) / 255.0,
        blue: CGFloat(value & 0xff) / 255.0,
        alpha: alpha
    )
}

func paragraph(_ alignment: NSTextAlignment = .left, lineHeight: CGFloat? = nil) -> NSMutableParagraphStyle {
    let style = NSMutableParagraphStyle()
    style.alignment = alignment
    if let lineHeight {
        style.minimumLineHeight = lineHeight
        style.maximumLineHeight = lineHeight
    }
    return style
}

func drawText(_ text: String, rect: NSRect, font: NSFont, color: NSColor, alignment: NSTextAlignment = .left, lineHeight: CGFloat? = nil, kern: CGFloat = 0) {
    let attrs: [NSAttributedString.Key: Any] = [
        .font: font,
        .foregroundColor: color,
        .paragraphStyle: paragraph(alignment, lineHeight: lineHeight),
        .kern: kern
    ]
    NSString(string: text).draw(in: rect, withAttributes: attrs)
}

image.lockFocus()

let bg = color("#faf7f2")
bg.setFill()
canvas.fill()

// Subtle paper texture.
var rng: UInt64 = 42
func nextRand() -> CGFloat {
    rng = 2862933555777941757 &* rng &+ 3037000493
    return CGFloat((rng >> 33) % 10_000) / 10_000.0
}

for _ in 0..<4200 {
    let x = nextRand() * CGFloat(width)
    let y = nextRand() * CGFloat(height)
    let a = 0.018 + nextRand() * 0.026
    color("#1a1d1b", alpha: a).setFill()
    NSBezierPath(ovalIn: NSRect(x: x, y: y, width: 1.2, height: 1.2)).fill()
}

// Warm surface band.
let bandPath = NSBezierPath()
bandPath.move(to: NSPoint(x: 0, y: 0))
bandPath.line(to: NSPoint(x: CGFloat(width), y: 0))
bandPath.line(to: NSPoint(x: CGFloat(width), y: 190))
bandPath.curve(
    to: NSPoint(x: 0, y: 136),
    controlPoint1: NSPoint(x: 1160, y: 210),
    controlPoint2: NSPoint(x: 490, y: 92)
)
bandPath.close()
color("#f3efe8").setFill()
bandPath.fill()

// Terracotta signal rule.
let rule = NSBezierPath(roundedRect: NSRect(x: 176, y: 472, width: 112, height: 8), xRadius: 4, yRadius: 4)
color("#c2603e").setFill()
rule.fill()

// Right-side oversized mark as a quiet brand shape.
if let icon = NSImage(contentsOfFile: iconPath) {
    icon.draw(
        in: NSRect(x: 1060, y: 70, width: 470, height: 470),
        from: .zero,
        operation: .sourceOver,
        fraction: 0.13
    )
}

// Logo block.
let logoBlock = NSBezierPath(roundedRect: NSRect(x: 176, y: 342, width: 378, height: 82), xRadius: 18, yRadius: 18)
color("#ffffff", alpha: 0.46).setFill()
logoBlock.fill()
color("#e6e1d4", alpha: 0.72).setStroke()
logoBlock.lineWidth = 1
logoBlock.stroke()

if let icon = NSImage(contentsOfFile: iconPath) {
    icon.draw(in: NSRect(x: 202, y: 359, width: 48, height: 48), from: .zero, operation: .sourceOver, fraction: 1)
}

let wordFont = NSFont(name: "Georgia-Bold", size: 54) ?? NSFont.boldSystemFont(ofSize: 54)
drawText("trivpass", rect: NSRect(x: 266, y: 348, width: 246, height: 70), font: wordFont, color: color("#1f4d3a"), kern: -2.2)
color("#c2603e").setFill()
NSBezierPath(ovalIn: NSRect(x: 512, y: 367, width: 10, height: 10)).fill()

// Headline and supporting copy.
let headlineFont = NSFont(name: "Georgia-Bold", size: 70) ?? NSFont.boldSystemFont(ofSize: 70)
drawText(
    "Real drivers.\nReal prices.\nNo surprises.",
    rect: NSRect(x: 176, y: 126, width: 760, height: 210),
    font: headlineFont,
    color: color("#1f4d3a"),
    lineHeight: 68,
    kern: -1.0
)

let bodyFont = NSFont(name: "AvenirNext-Medium", size: 25) ?? NSFont.systemFont(ofSize: 25, weight: .medium)
drawText(
    "Bali travel agency based in Seminyak.\nVerified drivers, day trips, activities,\nand all-in pricing.",
    rect: NSRect(x: 812, y: 142, width: 620, height: 116),
    font: bodyFont,
    color: color("#3a3f3c"),
    lineHeight: 32
)

// Receipt-style proof points.
let monoFont = NSFont.monospacedSystemFont(ofSize: 21, weight: .semibold)
let rows = [
    "DRIVER ROSTER..........VETTED",
    "PRICE..................ALL-IN",
    "OPS....................24/7"
]
for (index, row) in rows.enumerated() {
    drawText(
        row,
        rect: NSRect(x: 812, y: 318 + index * 38, width: 520, height: 30),
        font: monoFont,
        color: color(index == 1 ? "#c2603e" : "#1f4d3a"),
        kern: 0.2
    )
}

// Small footer line.
let footerFont = NSFont(name: "AvenirNext-DemiBold", size: 18) ?? NSFont.systemFont(ofSize: 18, weight: .semibold)
drawText(
    "The real Bali, uncomplicated.",
    rect: NSRect(x: 176, y: 62, width: 520, height: 28),
    font: footerFont,
    color: color("#6a706c")
)

image.unlockFocus()

guard let tiff = image.tiffRepresentation,
      let bitmap = NSBitmapImageRep(data: tiff),
      let png = bitmap.representation(using: .png, properties: [:]) else {
    fatalError("Could not render PNG")
}

try png.write(to: URL(fileURLWithPath: outPath))
print(outPath)
