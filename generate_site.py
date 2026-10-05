"""
generate_site.py

Auto-generates guide HTML pages for Favour Guides from a list of
Python dictionaries. To add a new guide, just add a new dictionary
to the `pages` list below, then run:

    python3 generate_site.py

This will create/update the matching .html file.
"""

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

CARD_TEMPLATE = """<div class="guide-card">
<h3>{card_title}</h3>
<p>
                {card_text}
            </p>
</div>"""


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
    {
        "filename": "mental-wellbeing.html",
        "title": "Mental Wellbeing",
        "hero_text": "Understanding stress, sleep, and how to take care of your mind.",
        "cards": [
            ("Managing Stress", "Stress is a normal response to challenges, but too much of it can affect your health. Deep breathing, short breaks, and talking to someone you trust can help."),
            ("Good Sleep Habits", "Keep a consistent sleep schedule, avoid screens right before bed, and aim for 7-9 hours a night for most teens and adults."),
            ("Taking Care of Your Mind", "It's okay to not be okay sometimes. Talking to a trusted friend, family member, or counselor is a healthy and important step."),
        ],
    },
    {
        "filename": "mathematics.html",
        "title": "Mathematics",
        "hero_text": "Step-by-step explanations of core math topics for junior secondary to high school students.",
        "cards": [
            ("Algebra Basics", "Algebra uses letters to represent unknown numbers. An equation like x + 5 = 12 means you need to find the value of x that makes it true. Here, x = 7."),
            ("Geometry Basics", "Geometry is the study of shapes, sizes, and angles. Know key formulas like area of a rectangle (length x width) and triangle (1/2 x base x height)."),
            ("Working with Fractions", "A fraction represents a part of a whole. To add or subtract fractions, they need the same denominator first."),
        ],
    },
    {
        "filename": "english.html",
        "title": "English Language",
        "hero_text": "A guide covering grammar, comprehension, and essay writing for junior secondary to high school students.",
        "cards": [
            ("Grammar Basics", "A sentence needs at least a subject and a verb to be complete. Watch for subject-verb agreement and consistent verb tense."),
            ("Reading Comprehension", "Read the passage fully first, then the questions, then find the exact part of the passage that answers each one."),
            ("Essay Writing", "A good essay has an introduction stating your main point, body paragraphs with supporting details, and a conclusion summing up your argument."),
        ],
    },
    {
        "filename": "science.html",
        "title": "Science",
        "hero_text": "Core concepts in biology, chemistry, and physics for junior secondary to high school students.",
        "cards": [
            ("Biology Basics", "Living things are made of cells. Photosynthesis is how plants make food using sunlight, water, and carbon dioxide."),
            ("Chemistry Basics", "Everything is made of atoms, which combine to form molecules. The periodic table organizes all known elements."),
            ("Physics Basics", "Newton's Laws of Motion describe how objects move and respond to forces. Energy changes form but is never created or destroyed."),
        ],
    },
    {
        "filename": "computer-basics.html",
        "title": "Computer Basics",
        "hero_text": "Understanding how computers work, from hardware to software.",
        "cards": [
            ("Hardware vs Software", "Hardware is the physical parts you can touch. Software is the programs and instructions that run on that hardware."),
            ("Key Components", "The CPU is the brain that carries out instructions. RAM is short-term memory. Storage holds your files even when powered off."),
            ("Operating Systems", "The operating system (Windows, macOS, Linux) manages everything and lets you run programs and connect to the internet."),
        ],
    },
    {
        "filename": "internet-safety.html",
        "title": "Internet Safety",
        "hero_text": "How to stay safe online and protect your personal information.",
        "cards": [
            ("Protecting Your Information", "Avoid sharing personal details like your address or passwords with people you don't know online."),
            ("Strong Passwords", "Use different passwords for different accounts, mixing letters, numbers, and symbols. Avoid obvious things like your name."),
            ("Spotting Scams", "Be wary of messages asking you to click suspicious links or send money urgently. If it feels off, it probably is."),
        ],
    },
    {
        "filename": "useful-apps.html",
        "title": "Useful Apps & Tools",
        "hero_text": "Simple tools that can make learning and daily life easier.",
        "cards": [
            ("Note-Taking Apps", "Apps like Google Keep or Notion let you quickly jot down ideas and organize notes by subject."),
            ("Productivity Tools", "Google Calendar helps track deadlines, while Google Docs lets you write and share documents easily."),
            ("Learning Resources", "Free platforms like Khan Academy and YouTube offer lessons on almost any subject."),
        ],
    },
    {
        "filename": "time-management.html",
        "title": "Time Management",
        "hero_text": "How to plan your study time and avoid last-minute cramming.",
        "cards": [
            ("Making a Study Schedule", "Break study time into 30-45 minute blocks per subject, with short breaks in between."),
            ("Prioritizing Tasks", "Start with subjects due soonest or that you find hardest, while your mind is fresh."),
            ("Avoiding Procrastination", "Break big tasks into smaller steps. Starting with just 5-10 minutes often makes it easier to keep going."),
        ],
    },
    {
        "filename": "memory-techniques.html",
        "title": "Memory Techniques",
        "hero_text": "Simple tricks to help you remember what you learn for longer.",
        "cards": [
            ("Spaced Repetition", "Review information again after a day, then a few days, then a week, to move it into long-term memory."),
            ("Using Mnemonics", "Mnemonics are memory tricks like acronyms or rhymes that help you recall information."),
            ("Teaching What You Learn", "Explaining a topic to someone else forces you to understand it clearly enough to teach it."),
        ],
    },
    {
        "filename": "staying-focused.html",
        "title": "Staying Focused",
        "hero_text": "Ways to avoid distractions and concentrate while studying.",
        "cards": [
            ("Removing Distractions", "Put your phone in another room or block distracting notifications while you study."),
            ("The Pomodoro Technique", "Study in focused 25-minute sessions, followed by a 5-minute break. Take a longer break after four sessions."),
            ("Setting Clear Goals", "Decide exactly what you want to accomplish before you start, like 'finish 10 math problems.'"),
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