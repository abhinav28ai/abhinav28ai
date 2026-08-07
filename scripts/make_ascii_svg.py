from PIL import Image

RAMP = " .`:-=+*#%@"

img = Image.open("source-prepped.png").convert("L")

WIDTH = 90

aspect = img.height / img.width

HEIGHT = int(WIDTH * aspect * 0.55)

img = img.resize((WIDTH, HEIGHT))

pixels = list(img.getdata())

rows = []

for y in range(HEIGHT):
    row = ""
    for x in range(WIDTH):
        p = pixels[y * WIDTH + x]
        row += RAMP[p * (len(RAMP)-1) // 255]
    rows.append(row)

line_height = 12
svg_height = line_height * len(rows) + 30

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="760"
height="{svg_height}"
viewBox="0 0 760 {svg_height}">

<rect width="100%" height="100%" fill="#0d1117"/>

<style>
text {{
font-family: monospace;
font-size:11px;
fill:#39d353;
}}

.cursor {{
animation: blink 1s infinite;
}}

@keyframes blink {{
50% {{ opacity:0; }}
}}
</style>
'''

y = 20

delay = 0

for row in rows:

    svg += f'''
<text x="10" y="{y}" opacity="0">
{row}
<animate
attributeName="opacity"
begin="{delay}s"
dur="0.05s"
fill="freeze"
from="0"
to="1"/>
</text>
'''

    y += line_height

    delay += 0.03

svg += f'''
<rect
x="730"
y="{svg_height-18}"
width="8"
height="12"
fill="#39d353"
class="cursor"/>
'''

svg += "</svg>"

with open("assets/ascii.svg","w") as f:
    f.write(svg)

print("✅ assets/ascii.svg generated")