import random
from collections import deque
from dictogram import Dictogram
from corpus import Corpus


class Markov(Dictogram):
    """Markov chain that uses a dictionary histogram to store word counts."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Markov, self).__init__()  # Initialize this as a new dict
        self.types = 0
        self.tokens = 0
        self.word_list = Corpus().clean_text().split()
        self.markov_dict = {}
        self.markov_dict = self.markov_chain()

    def markov_chain(self):
        """Create a Markov chain from given data string."""
        queue = deque(maxlen=4)  # Use deque to store the word pair
        for word in self.word_list:
            queue.append(word)
            if len(queue) == 4:  # Once the deque has two words, create the pair
                word_quad = tuple(queue)
                next_word_dict = self.markov_dict.get(word_quad, Dictogram())
                next_word = queue[-1]  # Get the next word
                next_word_dict.add_count(next_word)
                self.markov_dict[word_quad] = next_word_dict

        return self.markov_dict

    def random_walk(self, num_words=25):
        """Randomly walk the Markov chain and return a list of words thats length equals the num_words value."""
        sentence = []
        while len(sentence) < num_words:
            word_quad = random.choice(list(self.markov_dict.keys()))
            for word in word_quad:
                sentence.append(word)
        return sentence

    def print_markov_chain(self, num_samples=15):
        """Print a sample of the Markov chain."""
        print("Markov chain samples:")
        for _ in range(num_samples):
            sentence = self.random_walk()
            print(" ".join(sentence))
        print()

    def generate(self):
        sentence = self.random_walk()
        sentence = " ".join(sentence)
        # Capitalize the first letter of the sentence
        sentence = sentence[0].upper() + sentence[1:]
        # Add a period to the end of the sentence
        if not sentence.endswith((".", "?", "!")):
            sentence += "."
        return sentence


def main():
    word_list = Corpus().clean_text().split()
    markov = Markov(word_list)
    markov.print_markov_chain()
    print("Random Sentence:", " ".join(markov.random_walk()))


if __name__ == "__main__":
    main()
