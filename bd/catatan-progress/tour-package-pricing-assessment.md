# Tour Package Pricing Assessment

**Date:** 2026-06-08
**Scope:** Published Trivpass tour packages from the current local database snapshot.
**Pricing Strategy:** Meals excluded for regular private tours, with Blue Lagoon lunch, Batur breakfast/hot drink, and Ubud/Gianyar food-tour tastings kept as product-specific exceptions.
**Driver Cost Assumption:** Rp 700,000 base driver cost for non-Nusa Penida private-driver routes.

> Sumber: tim internal Trivpass. Disimpan di sini sebagai **input** untuk margin-overlay sheet (BD). Catatan BD: assessment ini membandingkan ke **harga RETAIL kompetitor**, belum ke **COGS Trivpass** — margin belum tervalidasi. Lihat rundown & analisis margin.

---

## Summary

Most Trivpass regular private sightseeing packages are priced above visible Bali provider benchmarks. The highest-risk packages are East Bali, Gate of Heaven, North Bali Lovina, Batur Jeep, and Nusa Penida snorkeling. The recommended direction is to lower visible per-person prices while keeping or adjusting minimum guests later to protect the Rp 700,000 driver base and direct supplier costs.

This file is an assessment only. It does not change seed data or database rows.

## Recommended Pricing Table

| Priority | Slug | Current Price | Current Min | Provider Benchmark | Recommended Price | Recommended Min | Pricing Assessment |
|---|---|---:|---:|---|---:|---:|---|
| 1 | `east-bali-gate-of-heaven-water-palaces` | Rp 1,350,000 | 2 | BaliVentur around Rp 700k; D Adventures Rp 750k; KutaTransport inclusive Rp 875k | **Rp 875,000** | **2** | Very high. Keep as premium only if route handling/queue support is stronger than competitors. |
| 1 | `gate-of-heaven-waterfall-photo-day` | Rp 1,300,000 | 2 | Similar Lempuyang/Gate routes around Rp 700k-875k | **Rp 875,000** | **2** | Very high. Waterfall variant can sit slightly above basic Gate route, but not Rp 1.3m. |
| 1 | `east-bali-tenganan-virgin-beach-tour` | Rp 1,200,000 | 2 | Tenganan/Virgin Beach routes around Rp 690k-700k | **Rp 850,000** | **2** | High. Current price is hard to justify with meals excluded. |
| 1 | `north-bali-lovina-dolphin-hot-spring-tour` | Rp 1,350,000 | 2 | Lovina private packages around Rp 800k; dolphin boat-only much lower | **Rp 975,000** | **2** | High. Long early route and boat/hot spring costs justify more than simple driver tour, but current price is steep. |
| 1 | `mount-batur-sunrise-jeep` | Rp 1,150,000 | 2 | Day Bali Rp 725k-785k; Bali Best Day Tour Rp 750k for 1-2 pax | **Rp 850,000** | **2** | High. Breakfast/hot drink stays included, but visible price should be closer to market. |
| 1 | `nusa-penida-snorkeling-west-land` | Rp 1,450,000 | 2 | Bali Friend Rp 1.35m includes lunch and private snorkeling boat; other shared options lower | **Rp 1,250,000** | **2** | High. Needs separate Penida cost model because boat/island costs are different. |
| 2 | `ubud-highlights-private-day-tour` | Rp 950,000 | 2 | Day Bali Rp 700k incl lunch/fees; BaliVentur Rp 550k excl lunch incl fees | **Rp 750,000** | **2** | High. Our route includes entrance fees but excludes lunch, so Rp 950k is too high. |
| 2 | `ubud-waterfall-rice-terrace-temple-day` | Rp 900,000 | 2 | Ubud/waterfall routes around Rp 550k-700k | **Rp 725,000** | **2** | High. Good route, but meal-excluded pricing should be lower. |
| 2 | `ubud-art-villages-jungle-swing-day` | Rp 850,000 | 2 | Ubud private route around Rp 550k-700k; swing/dress/photo extras commonly excluded | **Rp 700,000** | **2** | Slightly high. Keep swing extras clearly excluded. |
| 2 | `east-bali-besakih-sidemen-tour` | Rp 1,150,000 | 2 | Best Bali Adventures Rp 1.175m incl lunch; Sidemen/East Bali routes often lower | **Rp 900,000** | **2** | Slightly high. Besakih and longer route justify more than Ubud, but lunch exclusion should lower price. |
| 2 | `north-bali-bedugul-waterfall-tour` | Rp 1,150,000 | 2 | Bedugul/North routes often around Rp 790k+ or driver-based | **Rp 900,000** | **2** | Slightly high. Long route and entrance fees justify a premium, but current price is too close to meal-included tours. |
| 2 | `mt-batur-sunrise-hike` | Rp 950,000 | 2 | Batur trekking from around Rp 650k-675k | **Rp 775,000** | **2** | High. Breakfast stays included, but market starts lower. |
| 2 | `batur-sunrise-hot-spring` | Rp 1,250,000 | 2 | Trekking + hot spring benchmarks around Rp 1m | **Rp 1,050,000** | **2** | Slightly high. Hot spring inclusion supports a premium, but Rp 1.25m is aggressive. |
| 2 | `blue-lagoon-snorkeling-waterfall-day` | Rp 950,000 | 2 | Blue Lagoon all-inclusive Rp 600k-650k; waterfall add-on listings can be lower | **Rp 800,000** | **2** | High-ish. Lunch/towel/shower stay included, but waterfall add-on should not push it near Rp 1m. |
| 3 | `blue-lagoon-tanjung-jepun-snorkeling` | Rp 750,000 | 2 | Blue Lagoon all-inclusive Rp 600k-650k | **Rp 675,000** | **2** | Slightly high. This is a supplier-standard food-included exception, so lower gently. |
| 3 | `uluwatu-kecak-jimbaran-dinner` | Rp 950,000 | 2 | Uluwatu/Kecak routes around Rp 650k-750k; dinner now excluded | **Rp 750,000** | **2** | High after dinner removal. Price should reflect longer route, not included meal. |
| 3 | `holy-spring-purification-ritual` | Rp 750,000 | 2 | Perama Rp 550k; melukat-only around Rp 300k | **Rp 650,000** | **2** | Fair only if positioned as guided/private ritual with offerings and etiquette help. |
| 3 | `west-nusa-penida-day-tour` | Rp 1,150,000 | 2 | Day Bali Rp 995k includes lunch; Penida guide says private/day costs vary widely | **Rp 1,050,000** | **2** | Slightly high because lunch is excluded, but Penida costs need separate modeling. |
| 3 | `nusa-penida-east-west-highlights` | Rp 1,250,000 | 2 | Penida all-in/group day tours around Rp 600k-950k; private vehicle costs separate | **Rp 1,150,000** | **2** | Slightly high. East + West is longer, but still meal-excluded. |
| 4 | `uluwatu-sunset-temple-kecak-fire-dance` | Rp 650,000 | 2 | Uluwatu/Kecak routes commonly around Rp 650k-750k+ | **Rp 650,000** | **2** | Fair. Keep price for now. |
| 4 | `full-day-custom-tour` | Rp 475,000 | 2 | 2026 full-day driver market Rp 600k-1m/car | **Rp 475,000** | **2** | Fair. Total minimum revenue Rp 950k covers the Rp 700k driver base. |
| 4 | `half-day-custom-tour` | Rp 325,000 | 3 | 2026 half-day driver market Rp 400k-600k/car | **Rp 325,000** | **3** | Operationally safe, but min 3 makes it less friendly. Discuss min/price later. |
| 4 | `ubud-gianyar-night-market-food-tour` | Rp 650,000 | 2 | Guided food tours Rp 500k-750k; private food tours around Rp 600k-750k | **Rp 650,000** | **2** | Fair. Food tastings are the product. |

## Suggested Change Order

1. **East Bali and Gate of Heaven:** biggest visible mismatch against market.
2. **Batur Jeep and Batur Hike:** strong competitor pressure and easy traveler comparison.
3. **Ubud packages:** still high after meals-excluded positioning.
4. **North Bali:** long route, but current price is too close to meal-included competitors.
5. **Nusa Penida:** assess separately with ferry, harbor, island vehicle, snorkeling boat, and pickup-zone costs.
6. **Custom, Uluwatu sunset-only, food tour:** keep mostly unchanged for now.

## Notes By Package Family

### Ubud
Trivpass Ubud products are currently Rp 850k-950k while competitor private tours show Rp 550k-700k, sometimes with lunch included. Since Trivpass excludes lunch for these, the recommended range is Rp 700k-750k depending route and ticket load.

### East Bali / Gate of Heaven
This is the clearest pricing problem. Visible providers show East Bali/Gate routes around Rp 700k-875k with similar entrance-fee coverage. Recommended Trivpass pricing should land around Rp 850k-900k, not Rp 1.2m-1.35m.

### Batur
Batur breakfast/hot drink remains a supplier-standard exception. Even so, the Jeep and hike products are higher than visible competitors. Recommended reductions are moderate rather than extreme because supplier quality and early pickup reliability matter.

### Blue Lagoon
Blue Lagoon lunch remains included because suppliers commonly bundle lunch/towel/shower/changing room. The base snorkeling package only needs a small reduction. The waterfall variant should be reduced more because the current Rp 950k looks too close to premium long-route products.

### Uluwatu
The sunset-only product is fair at Rp 650k. The Jimbaran dinner-stop variant should drop after dinner was removed from inclusions; it now sells extra route time and dinner flexibility, not included seafood.

### Nusa Penida
Penida should not use the same driver-only cost model. The recommended prices above are provisional. A later model should separate: Bali-side pickup vehicle; return fast boat; harbor/infrastructure fees; Nusa Penida island vehicle; land attraction fees; snorkeling boat type (shared vs private); pickup-zone surcharges.

### Custom Tours
Full-day custom pricing is already aligned with the Rp 700k driver base. Half-day custom is margin-safe but less customer-friendly because `min_guests = 3`; discuss whether to keep min 3 or create a higher two-person price later.

## Source Benchmarks
- Day Bali Ubud tour: Rp 700k for 2 pax, includes lunch and entrance fees. https://www.daybalitour.com/bali-tegenungan-waterfall-and-best-ubud-tour-package/
- BaliVentur Ubud tour: Rp 550k per person, lunch optional/excluded, entrance fees included. https://baliventur.com/tours/ubud-tour/
- BaliVentur Lempuyang/Gate of Heaven: visible from Rp 700k. https://baliventur.com/tours/lempuyang-temple-gates-of-heaven-tour/
- D Adventures East Bali: Rp 750k for 2 pax, includes Lempuyang shuttle/tickets, Tirta Gangga, Taman Ujung, private car, driver. https://dadventuresbali.com/packages/east-bali-tour-lempuyang-temple-tirta-gangga-taman-ujung/
- KutaTransport East Bali: regular car Rp 850k/car, inclusive tour Rp 875k/person for 2-3 pax. https://kutatransport.net/lempuyang-temple-tirta-gangga-taman-ujung-east-bali-tour/
- Day Bali Batur Jeep: Rp 725k-785k for 2 pax depending pickup area, includes breakfast and Kintamani fees. https://www.daybalitour.com/bali-batur-sunrise-jeep-tour/
- Bali Best Day Tour Batur Jeep: Rp 750k for 1-2 pax, includes transfer, jeep, entrance, breakfast/hot drink, water, insurance. https://www.balibestdaytour.com/link/mount-batur-jeep-sunrise-tour.html
- Blue Lagoon benchmark: Rp 600k-650k all-inclusive with lunch. https://www.thebalipackage.com/tours/snorkeling-blue-lagoon-bali/
- Day Bali Nusa Penida: Rp 995k for 2 pax, includes return fast boat, lunch, entrance fees. https://www.daybalitour.com/the-west-nusa-penida-island-day-tour-package/
- Bali Friend Nusa Penida snorkeling + west: Rp 1.35m for 2 pax, includes lunch and private snorkeling boat. https://www.balifriendtour.com/nusa-penida/west-penida-snorkeling
- Go2Bali private driver guide: full-day driver market around Rp 600k-1m for 10 hours; half-day Rp 400k-600k. https://go2-bali.com/blog/bali-private-driver-cost-guide/
- Perama Tirta Empul purification private tour: Rp 550k/person, min 2. https://peramatour.com/tour/detail/212/tirta-empul-purification-private-tour
- Taman Dukuh Ubud/Gianyar food tour: group Rp 500k; private 2 adults Rp 750k/person; private 3-5 Rp 600k/person. https://tamandukuh.com/bali-cultural-experiences/bali-night-market-food-tours-in-ubud/
