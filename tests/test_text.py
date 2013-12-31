from pathlib import Path
import unittest

from text_counter_lab.core import analyze
from text_counter_lab.fixture_check import check


class TextTests(unittest.TestCase):
    def test_words_casefold_and_punctuation(self):
        result = analyze("Hello hello HELLO!\nworld\n")
        self.assertEqual((result["lines"], result["words"], result["unique_words"]), (2, 4, 3))
        self.assertEqual(result["top_words"][0], {"word": "hello", "count": 2})

    def test_unicode_and_empty_text(self):
        self.assertEqual(analyze("café café")["characters"], 9)
        self.assertEqual(analyze("")["lines"], 0)
        self.assertEqual(analyze("\n")["lines"], 1)
        self.assertEqual(analyze("   ")["words"], 0)

    def test_top_word_ties_are_deterministic(self):
        self.assertEqual(analyze("z a")["top_words"], [{"word": "a", "count": 1}, {"word": "z", "count": 1}])

    def test_all_generated_fixtures(self):
        self.assertGreaterEqual(check(Path(__file__).resolve().parents[1] / "fixtures" / "cases.jsonl", analyze), 350)


if __name__ == "__main__":
    unittest.main()
