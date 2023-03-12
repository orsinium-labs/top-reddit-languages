#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

import praw
from config import REDDIT

UA = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36'  # noqa
client = praw.Reddit(user_agent=UA, **REDDIT)
ROOT = Path(__file__).parent
sub_names = (ROOT / 'subreddits.txt').read_text().strip().splitlines()
result = []
for sub_name in sub_names:
    print(sub_name)
    sub = client.subreddit(sub_name)
    result.append(dict(
        name=sub_name,
        subscribers=sub.subscribers,
        title=sub.title,
        icon=sub.community_icon,
    ))

with (ROOT / 'data.json').open('w') as stream:
    json.dump(result, stream, indent=2)
