from __future__ import annotations
from datetime import date

import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# get template
ROOT = Path(__file__).parent
env = Environment(loader=FileSystemLoader(ROOT))
template = env.get_template('index.html.j2')

# render data
with (ROOT / 'data.json').open() as stream:
    subs: list = json.load(stream)
subs.sort(key=lambda sub: sub['subscribers'], reverse=True)
content = template.render(
    subs=subs,
    max_subscribers=subs[0]['subscribers'],
    today=date.today(),
)

# write result
output_path = (ROOT / 'public' / 'index.html')
output_path.parent.mkdir(exist_ok=True)
output_path.write_text(content)
