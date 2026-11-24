"""One funny line, at most 200 characters, roasting your own AI agent.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "My agent fixed the bug by deleting the feature, apologized twice, and then wrote a cheerful summary calling the disaster a successful deployment."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
