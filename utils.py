from typing import List, Iterable
import random

import pandas as pd
import mimesis
from tqdm import tqdm
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.model_selection import train_test_split

from config import DATASET_DIR


def tokenize(doc: str) -> List[str]:
    """
    Tokenize a document (a regular Python string) into tokens.
    The string is converted to lowercase before tokenization.

    >>> tokenize("Hello There! General Kenobi!")
    ['hello', 'there', '!', 'general', 'kenobi', '!']
    """
    return word_tokenize(doc.lower())


def sent_word_tokenize(doc: str) -> List[List[str]]:
    """
    Tokenize a document (a regular Python string) into sentences and words.
    The string is converted to lowercase before tokenization.

    >>> sent_word_tokenize("Hello There! General Kenobi!")
    [['hello', 'there', '!'], ['general', 'kenobi', '!']]
    """
    doc = doc.lower()
    return [word_tokenize(sentence) for sentence in sent_tokenize(doc)]


def word_to_index(word, vocab, oov_token="UNK"):
    "Convert a word into an index according to the input vocabulary"
    try:
        return vocab[word].index
    except KeyError:
        return vocab[oov_token].index


def count_tokens(documents: Iterable[str], verbose=False):
    """Return three lists:

    - for each document, the number of sentences
    - for each sentence, the number of tokens
    - for each document, the number of tokens

    >>> count_tokens(["First document. First document again", "Second doc."])
    ([2, 1], [3, 3, 3], [6, 3])
    """
    sent_per_doc = []
    tokens_per_sent = []
    tokens_per_doc = []
    for doc in tqdm(documents, total=len(documents), disable=(not verbose)):
        tokenized_doc = sent_word_tokenize(doc)
        sent_per_doc.append(len(tokenized_doc))
        tokens = 0
        for sent in tokenized_doc:
            tokens_per_sent.append(len(sent))
            tokens += len(sent)
        tokens_per_doc.append(tokens)
    return sent_per_doc, tokens_per_sent, tokens_per_doc


def _generate_doc(label, provider, keywords):
    "Generate a random document containing a sentence with a keyword"
    num_sentences = int(random.lognormvariate(2, 0.3))
    sentences = [provider.sentence() for _ in range(num_sentences)]
    idx = random.randint(0, len(sentences) - 1)
    tokens = word_tokenize(sentences[idx])
    # insert a keyword in a random position within the sentence
    # (excluding the last position because it contains the dot)
    tokens.insert(
        random.randint(0, len(tokens) - 1), random.choice(keywords[label])
    )
    sentences[idx] = " ".join(tokens)
    return " ".join(sentences)


def create_synthetic_data(num_samples):
    keywords = {
        0: ["bad", "worst", "dirty", "irritating", "disgusting"],
        1: ["vague", "vain", "untouchable", "selfish", "rude"],
        2: ["perverse", "possessive", "arrogant", "cruel", "calm"],
        3: ["clever", "comfortable", "creative", "clean", "gentle"],
        4: ["nice", "fantastic", "good", "modern", "quite"],
    }
    p = mimesis.Text()
    data = [
        (label, _generate_doc(label, p, keywords))
        for label in keywords
        for _ in tqdm(range(num_samples // len(keywords)))
    ]
    df = pd.DataFrame.from_records(data, columns=["label", "text"]).sample(
        frac=1
    )
    df.to_csv(f"{DATASET_DIR}/synthetic.csv", index=False)
    train_df, testval_df = train_test_split(
        df, test_size=0.2, stratify=df.label
    )
    val_df, test_df = train_test_split(
        testval_df, test_size=0.5, stratify=testval_df.label
    )
    train_df.to_csv(f"{DATASET_DIR}/synthetic_train.csv", index=False)
    train_df.append(val_df).to_csv(
        f"{DATASET_DIR}/synthetic_trainval.csv", index=False
    )
    val_df.to_csv(f"{DATASET_DIR}/synthetic_val.csv", index=False)
    test_df.to_csv(f"{DATASET_DIR}/synthetic_test.csv", index=False)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
