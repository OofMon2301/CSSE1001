SCRABBLE_VALUES = (
    ("a", 1),
    ("b", 3),
    ("c", 3),
    ("d", 2),
    ("e", 1),
    ("f", 4),
    ("g", 2),
    ("h", 4),
    ("i", 1),
    ("j", 8),
    ("k", 5),
    ("l", 1),
    ("m", 3),
    ("n", 1),
    ("o", 1),
    ("p", 3),
    ("q", 10),
    ("r", 1),
    ("s", 1),
    ("t", 1),
    ("u", 1),
    ("v", 4),
    ("w", 4),
    ("x", 8),
    ("y", 4),
    ("z", 10),
)


# Write your Scrabble code below
def read_scores():
    """Takes tuple into argument and create dictionary."""
    scores = {}
    for letter, value in SCRABBLE_VALUES:
        scores[letter] = value
    return scores


def get_score(scores, word):
    """Returns the score of the word."""
    score = 0
    for char in word:
        score += scores[char]
    return score


wordguess = input("Enter a word you want to check: ")
print(get_score(read_scores(), wordguess))
