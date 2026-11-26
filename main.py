import os
import sys

"""
Writes a single funny one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Also mirrors to /output/entry.txt when the target directory differs.
"""

LINE = "The shower spider pays rent in mosquito control and demands hot water weekends."


def main() -> None:
    content = LINE + "\n"
    if not (1 <= len(content) <= 200 and content.strip() and content.count('\n') == 1):
        raise ValueError("content validation failed")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(f"{out_path} {len(content)}")


if __name__ == "__main__":
    main()
# Entry validated: output is 1-200 chars, one line, deterministic.
