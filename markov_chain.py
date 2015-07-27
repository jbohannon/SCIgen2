import random

class Model(object):
    end_marker = '_ENDMARKER_'
    def __init__(self, n=3):
        self.n = n
        self.prefix = ['_LEAD_IN%d_' % i for i in range(n-1)]
        self.words = {}

    def read_sample(self, sequence):
        sequence = self.prefix + sequence + [self.end_marker]
        n = self.n
        for ix in range(len(sequence) - n + 1):
            key = tuple(sequence[ix:ix+n-1])
            val = sequence[ix+n-1]
            if key not in self.words:
                self.words[key] = []
            self.words[key].append(val)

    def train(self, sequence_generator):
        for seq in sequence_generator:
            self.read_sample(seq)

    def generate(self):
        sequence = self.prefix[:]
        n = self.n
        while True:
            key = tuple(sequence[-(n-1):])
            word = random.choice(self.words[key])
            if word == self.end_marker:
                break
            sequence.append(word)

        return sequence[n-1:]  # Trim off the prefix
