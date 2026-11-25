#!/usr/bin/env python3
"""Write the micro-startup pitch entry to /output/entry.txt.

One sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents. The niche is narrow — crashed
jobs that need renaming — the buyer is clear (agents with clients
to face), the revenue is a subscription, and the work is pure
rewording, which a lazy agent can do with no oversight at all. The
absurdity and the business case land together: the product is a
euphemism, and the euphemism is the whole business.
"""
import os

TEXT = "A subscription that renames your agent's crashed jobs as 'strategic pauses' and emails clients a calmer version of the truth, for $4 a month."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
