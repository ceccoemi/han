import argparse

import pandas as pd
from gensim.models import Word2Vec
from tqdm import tqdm

from config import TQDM, EMBEDDING_SIZE, Yelp, Yahoo, Amazon, Synthetic
from utils import sent_word_tokenize


class SentenceIterator:
    def __init__(self, dataset):
        self.dataset = dataset

    def __iter__(self):
        for _, doc in tqdm(
            self.dataset.itertuples(index=False),
            total=len(self.dataset),
            disable=(not TQDM),
        ):
            tokenized_doc = sent_word_tokenize(doc)
            for sentence in tokenized_doc:
                yield sentence


def train_word2vec_model(dataset, dim_embedding, min_count=5):
    model = Word2Vec(min_count=min_count, size=dim_embedding)
    model.build_vocab([["PAD"] * min_count])  # add PAD word
    model.build_vocab([["UNK"] * min_count], update=True)  # add OOV word
    sentence_iter = SentenceIterator(dataset)
    model.build_vocab(sentence_iter, update=True)
    model.train(
        sentence_iter, total_examples=model.corpus_count, epochs=model.epochs,
    )
    return model


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a word2vec model")
    parser.add_argument(
        "dataset",
        choices=["yelp", "yahoo", "amazon", "synthetic"],
        help="Choose the dataset",
    )

    args = parser.parse_args()

    if args.dataset == "yelp":
        dataset_config = Yelp
    elif args.dataset == "yahoo":
        dataset_config = Yahoo
    elif args.dataset == "amazon":
        dataset_config = Amazon
    elif args.dataset == "synthetic":
        dataset_config = Synthetic
    else:
        # should not end there
        exit()

    dataset = pd.concat(
        [
            pd.read_csv(dataset_config.TRAIN_DATASET).fillna(""),
            pd.read_csv(dataset_config.VAL_DATASET).fillna(""),
        ]
    ).sample(frac=1)
    model = train_word2vec_model(dataset, EMBEDDING_SIZE)
    model.wv.save(dataset_config.EMBEDDING_FILE)
