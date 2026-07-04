# 05 · Products

> What Trivpass actually sells. There are four product types in v1, and each one has a distinct buyer journey, inventory model, and brand role.

---

## At a glance

| Product type | Inventory | Typical price (per traveler) | Brand role |
|---|---|---|---|
| **Tour Packages** | Always-on | IDR 1.2M – 1.5M | Easy entry point, predictable revenue |
| **Cultural Events** *(aspirational in v1)* | Calendar-bound, capped | IDR 700K – 1.5M | Brand differentiator, hardest to clone |
| **Activities & Attractions** | Always-on | IDR 200K – 850K (varies widely by type) | Captures hotel-concierge alternatives; broadest catalog |
| **Custom Trips** (meta-product) | Generated on demand | Same as components | Removes the "I don't know what to book" friction |

All four are booked through the same checkout, with the same all-in pricing discipline, and the same Trivpass driver roster.

---

## 1. Tour Packages

### What it is

Pre-built day trips with a fixed itinerary, fixed stops, fixed price. Examples:

- **Ubud Sunrise Trio** — Tegalalang rice terraces at sunrise + Tirta Empul holy spring + Tegenungan waterfall.
- **Mt. Batur Sunrise Hike** — 3:30am pickup, ~2hr climb, sunrise summit, breakfast cooked on volcanic steam, descent + hot springs.
- **East Bali Cultural Day** — Tirta Gangga water palace + Lempuyang gates + Sidemen Valley rice fields.
- **South Bali Sunset Loop** — Uluwatu temple + Kecak fire dance + Jimbaran beach dinner.

### How travelers buy it

- Browse `/tour-packages`, filter by region/duration/vibe.
- Configure: date, guest count, vehicle class, pickup type (hotel or meet-at-venue).
- See live all-in price update as they configure.
- Book in one transparent checkout.

### What's included in the price

- Verified Trivpass driver + vehicle for the full day.
- All activity / attraction tickets for the stops on the itinerary.
- Fuel, parking, tolls, traveler insurance (vehicle is Trivpass-insured).
- Bottled water in the car.
- Sarong rental at temple stops.
- (For Mt. Batur) breakfast on the volcano.

### What's *not* included

- Lunches at restaurant stops (we say so explicitly).
- Tips (we don't pre-charge tips; we don't suggest them).
- Hotel pickup outside the standard pickup zones — surfaces as a "Request quote" CTA.

### Brand role

Tour packages are the most-booked product. They are the "first Trivpass purchase" for ~70% of new customers. They prove the brand promise (driver shows up, price is what it said, day works) so the traveler comes back for cultural events and attractions on the same trip.

### Copy notes

- The title is always **noun-led**, not adjective-led. *"Ubud Sunrise Trio"* — not *"Magical Ubud Sunrise Tour"*.
- The description leads with what you actually do, in order. *"06:00 pickup at your hotel — 07:30 at Tegalalang for sunrise photography — 09:30 breakfast at a family warung — 11:00 Tirta Empul …"*
- Pricing is always rendered "from IDR X · per traveler" — never "starting at $X".

---

## 2. Cultural Events

### What it is

Curated access to real Bali ceremonies, attended as invited guests of the host village. The canonical examples — the ones already on the seeded calendar and the additional ones in scope for v1:

- **Galungan Village Procession** *(Ubud area · every 210 days)* — the morning procession during the ten-day stretch when Balinese ancestors return to earth. Travelers walk the village paths at sunrise as the offerings are carried.
- **Melasti — Sea Purification Procession** *(Sanur · 4 days before Nyepi)* — pre-Nyepi cleansing rite where villages parade their sacred objects to the sea for ritual cleansing.
- **Mekotek — Wood-Pyramid Ritual** *(Munggu village, Mengwi · every Kuningan, 210-day cycle)* — men interlock 2-meter wooden poles into a swaying pyramid that another man climbs to ward off evil. Recognised cultural heritage; unique to Munggu village.
- **Ogoh-Ogoh Parade** *(island-wide · evening before Nyepi)* — giant demon effigies, built by each *banjar* over weeks, paraded through the streets and then ceremonially burned. The most visually distinctive night of the Balinese year.
- **Omed-Omedan** *(Sesetan, Denpasar · day after Nyepi)* — the village's annual "kissing ritual" between unmarried youth, a centuries-old tradition unique to Sesetan.
- **Pesta Kesenian Bali (PKB)** *(Denpasar · annually, mid-June to mid-July)* — month-long government-organized arts festival running since 1979. Dance, music, craft, food across multiple venues.
- **Odalan Besakih** *(Pura Besakih · temple-anniversary cycle)* — the temple anniversary at Bali's mother temple on the slopes of Mount Agung. Travelers attend as respectful prayer-visitors during the open-temple periods.

### Status in v1

**Aspirational.** The cultural-event product line depends on written agreements with host *banjars* and *Pemangku* priests — covering visitor conduct, group-size limits, sacred-date cancellation rights, and the per-traveler community contribution. **Until those agreements are signed, this product line is "curated catalog being built", not "live booking".**

Do not write copy that implies the calendar is fully live. The website treats this product line as in-progress.

### Inventory model

- **Calendar-bound** — tied to the Bali Hindu calendar. Most events fall on specific lunar days; some are village-specific *odalan* (every 210 days).
- **Capacity-capped** — typically 12 visitors, sometimes 8. Set by the host *banjar*, not by us.
- **Seats decrement at cart-add time**, not at checkout — to prevent over-booking from concurrent visitors.
- **Cart abandonment reclaims seats after 24h** so we don't lock seats on incomplete bookings.

### What's included in the price

- Sarong + sash + cultural-respect briefing.
- Driver + vehicle to and from the village.
- Pemangku/guide language interpretation during the ceremony.
- IDR 100,000 per traveler community contribution to the host *banjar* — **shown explicitly on every cultural-event card**.
- Bottled water, light refreshment after the ceremony.

### Brand role

The single most distinctive product. The reason a returning Bali traveler chooses Trivpass over a hotel concierge. The hardest to clone — even with all the engineering budget in the world, a competitor cannot fast-forward the trust relationship with the host *banjar*.

### Copy notes

- Always disclose the community contribution upfront. **"IDR 100,000 of your booking goes directly to the local community hosting this ceremony"** — non-negotiable, on every card.
- Disclose the capacity number. **"Limited to 12 visitors per session."**
- Disclose the cancellation right. **"If the *banjar* cancels for a sacred reason, you receive a full refund."**
- Use Balinese terms (*odalan, purnama, banjar, Pemangku*) glossed on first use. Italicize on first appearance, plain text thereafter.
- Never claim "*banjar*-approved", "village-endorsed", or "Pemangku-certified". We are guests, not certified partners.

---

## 3. Activities & Attractions

> *Internally the data model uses `experience_type` of either `'activity'` or `'attraction'`. The customer-facing umbrella term is **Activities & Attractions** (plural).*

### What it is

A broad catalog of individual experiences — attractions and activities — bookable as standalone with optional driver. The traveler picks the experience, the ticket tier, the date, and whether they want a Trivpass driver for the day.

The category spans two shapes:

- **Attractions** — single sites with timed entry. Temples (Tirta Empul, Uluwatu, Tanah Lot, Ulun Danu), scenic spots (Tegalalang rice terraces, Lempuyang gates), cultural shows (Kecak fire dance), photo destinations.
- **Activities** — bookable experiences with a duration and operator. Water parks (Waterbom Bali), wildlife parks (Bali Zoo, Bali Safari), watersports (Tanjung Benoa parasailing, jet-ski, banana boat), ATV rides, white-water rafting, hot-springs day passes, day clubs.

Categories in the catalog include: Culture & Heritage · Wildlife & Animals · Water Parks · Hot Springs & Wellness · Water Activities · Theme Parks & Play · Nature & Scenic · Adventure & Photo Spots · Day Clubs & Lifestyle · Family.

### How it differs from a tour package

- **One experience, not a route.** Activities & attractions are single destinations or single activities; tour packages bundle 3–5 stops across a day.
- **Driver is optional.** Many travelers book just the ticket and arrange their own transport (Grab, hotel shuttle, taxi). The Trivpass driver add-on is a separate line item.
- **Ticket tiers** — vary by experience. Common tiers: Day Entry / Day + Add-on (e.g., guided tour, cooking demo, sunset access) / Day + Sunset (timed for golden hour). Activities use operator-specific tier names (e.g. for watersports: single-ride / combo of 3 / full-day pass).

### Brand role

The product type with the broadest catalog and the broadest price range. The category that competes most directly with hotel concierges and OTA single-experience listings (Klook, GetYourGuide, Viator). The traveler-friendly entry point for someone who's only adding one Trivpass experience to an otherwise self-directed trip.

### Copy notes

- The umbrella term is always plural — *"Activities & Attractions"* — never singular *"Activity & Attraction"* as a section header. Singular forms are fine as ticket-card eyebrows: *"Activity"* or *"Attraction"*.
- The driver upsell is presented as **optional**, never default-on. *"Add a private Trivpass driver — pickup, wait at the venue, drop-off."*
- Skip-the-line entry is a real value — surface it when available.
- Use the right umbrella term in copy: *"official tickets for water parks, wildlife parks, watersports, ATV rides, rafting, cultural shows, temples, and Bali's popular photo spots."*

---

## 4. Custom Trip Builder

### What it is

A meta-product. The traveler describes their trip — dates, traveler count, vibes, pace, must-visit places — and our AI generates three bespoke itineraries (typically *cultural*, *nature*, and *soulful* angles by default). The traveler picks one and books directly, or saves it and waits for a human-refined version from our trip designers.

### How travelers buy it

1. Submit the brief form at `/custom-trip` (8 sections — dates, guests, vibes, pace, regions, budget, must-visit, notes).
2. AI generates 3 proposals within ~30 seconds. User is shown a loading state during generation.
3. User browses the 3 angles in `/my-trips/proposals/<brief-ref>`, can save any of them for later.
4. User clicks "Book this trip" → standard cart + checkout flow.
5. *Optionally:* user waits and the admin team posts a refined version of one of the proposals.

### Inventory model

- **Generated on demand.** No pre-built inventory. Each brief produces its own proposal set.
- **Regeneration** — users can request a new set of 3 if the first set misses. Old proposals are retained for audit.
- **Admin refinement** — the proposals can be edited by Trivpass trip designers, who add a 4th angle or rewrite the AI angles. The original AI version is retained.

### Brand role

The custom trip builder removes the **"I don't know what to book"** friction without compromising the curation pitch. The AI is good enough that 60%+ of users book the AI proposal directly (no human refinement). When users *do* wait for human refinement, the trip designer's edit is itself part of the brand — they're stamping it as worth your money.

### Important: custom trip flow ≠ admin trip refinement

A point of internal confusion: the custom trip is **not** an admin-built itinerary. The customer picks an AI proposal directly. Admin only **verifies** and **materializes the booking** at the gate. (See [project_custom_trip_flow memory] for the lifecycle: awaiting_review → in_progress → admin_verify → booked.)

### Copy notes

- The AI is named transparently. *"Our AI builds three drafts based on your brief — you pick one and we make it real."*
- The "wait for human" option is presented as additive, not corrective. *"Or wait 24 hours for our trip designers to refine the proposals."* — not *"… in case the AI got it wrong."*
- Pricing is computed live from the component costs (driver day rate × days, attractions, cultural events). Same all-in discipline as the other products.

---

## How the products fit together

Most travelers buy **2–4 items** across a single Bali trip:

- A first-day **activity or attraction** to test the brand (low-commitment, low-price).
- A **tour package** in the middle of the trip (the agency demonstrates day-management).
- A **cultural event** late in the trip (the differentiated, distinctive memory they'll tell stories about).
- *Or:* a single **custom trip** that bundles all three across a multi-day plan.

The system is designed so each product is good on its own but stronger together. The first booking is the trust-building purchase; the second and third are where the brand earns its margin.

---

## What we deliberately do *not* sell in v1

- **Hotels.** We are not Booking.com. We may surface partner-hotel recommendations in editorial content, but we do not collect commissions on hotel bookings.
- **Flights.** Out of scope. Customer's responsibility.
- **Visa processing.** Out of scope.
- **Multi-day all-inclusive packages with accommodation.** Out of scope; would require us to take on hotel inventory and partner relationships beyond v1.
- **Loyalty / referral programs.** Out of scope.
- **Gift cards.** Out of scope.

These could become products later, but they are not v1. Saying no keeps the product surface honest and the pricing model clean.

### What we do serve that sometimes gets miscategorized

A few notes on edge cases where the answer is *yes, we serve this*:

- **Group bookings (10+ travelers).** We do handle these — multi-vehicle dispatch, consolidated invoice, single point of contact. For very large groups, the booking flow is higher-touch (often via `hello@trivpass.com` or `trips@trivpass.com` rather than self-serve checkout).
- **Photo-spot travelers** (Tegalalang swing, Lempuyang gates, Handara archway, Wanagiri tree-nest). Our *Adventure & Photo Spots* category sells official tickets and an optional driver who knows the queue and the light. We don't manufacture or stage these spots — we just make the booking honest.
