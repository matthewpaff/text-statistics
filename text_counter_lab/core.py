"""Simple text statistics, with explicit whitespace-based word semantics."""
from collections import Counter


def analyze(text):
    if not isinstance(text, str):
        raise ValueError("Input must be text")
    words = text.split()
    return {"characters": len(text), "lines": len(text.splitlines()), "words": len(words),
            "unique_words": len(set(word.casefold() for word in words)),
            "longest_word": max(map(len, words), default=0),
            "top_words": [{"word": word, "count": count} for word, count in sorted(
                Counter(word.casefold() for word in words).items(), key=lambda item: (-item[1], item[0]))[:10]]}
