"""Original synthetic text examples with independently specified expected counts."""
import argparse
import json


def make_case(index):
    label = "synthetic-text-{:04d}".format(index)
    count = 1 + index % 6
    token = "word{:04d}".format(index)
    separator = "\n" if index % 2 else " "
    text = separator.join([token] * count)
    if index % 7 == 0:
        text = ""
        expected = {"characters": 0, "lines": 0, "words": 0, "unique_words": 0, "longest_word": 0, "top_words": []}
    else:
        expected = {"characters": len(token) * count + count - 1, "lines": count if separator == "\n" else 1,
                    "words": count, "unique_words": 1, "longest_word": len(token), "top_words": [{"word": token, "count": count}]}
    return {"id": label, "input": text, "expected": expected}


def main():
    parser = argparse.ArgumentParser(description="Print synthetic text cases as JSONL.")
    parser.add_argument("--count", type=int, default=20)
    args = parser.parse_args()
    if not 1 <= args.count <= 10000:
        parser.error("Count must be between 1 and 10000")
    for index in range(args.count):
        print(json.dumps(make_case(index), ensure_ascii=True, sort_keys=True))


if __name__ == "__main__":
    main()
