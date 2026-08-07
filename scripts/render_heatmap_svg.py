import json
from pathlib import Path

# Load contribution data
with open("data/contributions.json") as f:
    days = json.load(f)

# GitHub-like colors
PALETTE = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353"
]

CELL = 12
GAP = 3

WIDTH = 53 * (CELL + GAP) + 40
HEIGHT = 7 * (CELL + GAP) + 60

svg = f'''
<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}">

<rect width="100%" height="100%" fill="#0d1117"/>

<text
x="20"
y="20"
fill="white"
font-size="16"
font-family="monospace">

GitHub Contribution Heatmap

</text>
'''

for i, day in enumerate(days):

    week = i // 7
    weekday = i % 7

    x = 20 + week * (CELL + GAP)
    y = 30 + weekday * (CELL + GAP)

    level = min(day["level"], 4)

    color = PALETTE[level]

    delay = i * 0.002

    svg += f'''
<rect
x="{x}"
y="{y}"
width="{CELL}"
height="{CELL}"
rx="2"
fill="{color}"
opacity="0">

<animate
attributeName="opacity"
from="0"
to="1"
begin="{delay}s"
dur="0.2s"
fill="freeze"/>

</rect>
'''

svg += "</svg>"

Path("assets/contrib-heatmap.svg").write_text(svg)

print("✅ assets/contrib-heatmap.svg generated")