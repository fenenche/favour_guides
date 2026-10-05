"""
generate_site.py

Auto-generates guide HTML pages for Favour Guides from a list of
Python dictionaries. To add a new guide, just add a new dictionary
to the `pages` list below, then run:

    python3 generate_site.py

This will create/update the matching .html file.
"""

# The shared header and footer used on every guide page.
# {title} and {hero_text} get filled in per page.
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - Favour Guides</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<header>
<nav>
<a href="index.html">Favour Guides</a>

<div>
<a href="index.html">Home</a>
<a href="school-studies.html">School Studies</a>
<a href="health.html">Health</a>
<a href="technology.html">Technology</a>
<a href="study-tips.html">Study Tips</a>
</div>
</nav>
</header>

<main>
<section class="hero">
<h1>{title}</h1>
<p>
            {hero_text}
</p>
</section>

<section id="guides">
<div class="guide-container">
{cards}
</div>
</section>
</main>

</body>
</html>
"""

# Template for a single card inside a guide page.
CARD_TEMPLATE = """<div class="guide-card">
<h3>{card_title}</h3>
<p>
                {card_text}
            </p>
</div>"""


# --- PAGE DATA ---
# Each entry here becomes one HTML file.
# "filename" is what the .html file will be called.
# "cards" is a list of (card_title, card_text) tuples.

pages = [
    {
        "filename": "nutrition.html",
        "title": "Nutrition Basics",
        "hero_text": "Simple, practical guidance on eating well and building healthy habits.",
        "cards": [
            ("Balanced Meals", "A balanced meal generally includes a mix of carbohydrates, protein, and vegetables. Try to fill half your plate with vegetables or fruit when you can."),
            ("Staying Hydrated", "Drinking enough water each day helps your body function properly, supports concentration, and prevents fatigue."),
            ("Healthy Snacking", "Instead of sugary or heavily processed snacks, try fruit, nuts, or yogurt to keep your energy steady."),
        ],
    },
    {
        "filename": "exercise.html",
        "title": "Exercise & Fitness",
        "hero_text": "Easy, practical ways to stay active, even with a busy schedule.",
        "cards": [
            ("Why Exercise Matters", "Regular physical activity strengthens your heart, improves mood, and boosts energy levels."),
            ("Simple Ways to Stay Active", "Take the stairs, walk or cycle for short trips, or do a 15-minute home workout."),
            ("Building a Routine", "Start with 2-3 days a week of light activity and build up gradually. Consistency matters more than intensity."),
        ],
    },
]


def generate_page(page):
    cards_html = "\n\n".join(
        CARD_TEMPLATE.format(card_title=title, card_text=text)
        for title, text in page["cards"]
    )

    html = PAGE_TEMPLATE.format(
        title=page["title"],
        hero_text=page["hero_text"],
        cards=cards_html,
    )

    with open(page["filename"], "w") as f:
        f.write(html)

    print(f"Generated {page['filename']}")


if __name__ == "__main__":
    for page in pages:
        generate_page(page)

    print(f"\nDone! Generated {len(pages)} page(s).")