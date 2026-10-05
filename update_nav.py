"""
update_nav.py

Finds every .html file in this folder and adds a "Business & Finance"
link to the navigation bar, right after "Study Tips" -- so you don't
have to manually edit the nav in every single file.

Run with:
    python3 update_nav.py
"""

import glob

OLD_NAV_END = '<a href="study-tips.html">Study Tips</a>\n</div>'
NEW_NAV_END = '<a href="study-tips.html">Study Tips</a>\n<a href="business-finance.html">Business & Finance</a>\n</div>'

updated_count = 0
skipped_count = 0

for filename in glob.glob("*.html"):
    with open(filename, "r") as f:
        content = f.read()

    if OLD_NAV_END in content:
        new_content = content.replace(OLD_NAV_END, NEW_NAV_END)
        with open(filename, "w") as f:
            f.write(new_content)
        print(f"Updated nav in {filename}")
        updated_count += 1
    elif "business-finance.html" in content:
        print(f"Skipped {filename} (already has the new link)")
        skipped_count += 1
    else:
        print(f"Skipped {filename} (nav pattern not found)")
        skipped_count += 1

print(f"\nDone! Updated {updated_count} file(s), skipped {skipped_count}.")