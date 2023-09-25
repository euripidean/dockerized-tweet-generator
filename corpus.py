import re


class Corpus:
    def __init__(self):
        self.corpus = self.clean_text()

    def read_file(self):
        with open("./data/corpus.txt") as f:
            corpus = f.read()
        return corpus

    def clean_text(self):
        """Remove punctuation and newlines, lowercase text."""
        corpus = self.read_file()
        corpus = corpus.replace("\n", " ")
        # Remove punctuation
        corpus = re.sub(r"[^a-zA-Z0-9\s']", "", corpus)
        # Remove single quotes that aren't part of words
        corpus = re.sub(r"\s'", " ", corpus)
        # Remove numbers
        corpus = re.sub(r"\d", "", corpus)
        # Remove extra spaces
        corpus = re.sub(r"\s+", " ", corpus)

        ignore_counts = {}
        for word in corpus.split():
            if word[0].isupper():
                ignore_counts[word] = ignore_counts.get(word, 0) + 1

        # sort ignore counts by values
        ignore_counts = dict(
            sorted(ignore_counts.items(), key=lambda x: x[1], reverse=True)
        )

        ignore = set()

        # if word is in ignore list more than three times, keep it in the ignore set
        for word, count in ignore_counts.items():
            if count > 3:
                ignore.add(word)

        # If word not in ignore set, put it to lowercase
        words = []
        for word in corpus.split():
            if word not in ignore:
                words.append(word.lower())

        # Words back into a single string
        corpus = " ".join(words)

        return corpus


if __name__ == "__main__":
    print(Corpus.clean_text())
