# HAN

Replication of some of the experiments reported in:

[Yang, Zichao, et al. "Hierarchical attention networks for document classification." Proceedings of the 2016 conference of the North American chapter of the association for computational linguistics: human language technologies. 2016.](https://www.cs.cmu.edu/~./hovy/papers/16HLT-hierarchical-attention-networks.pdf)

The main goal of these experiments is to compare the performances of a Hierarchical Attention Network with a Non-Hierarchical Attention and a classic BoW approach.

## Datasets

I wasn't able to find the exactly datasets of the paper, so I have created three datasets from three cited sources: Yelp, Yahoo and Amazon. The datasets are perfectly balanced in all the classes.

|  **Dataset**  | **Classes** | **Documents** |
|---------------|-------------|---------------|
|     Yelp      |      5      |   1,569,000   |
| Yahoo Answer  |      10     |   1,450,000   |
| Amazon review |      5      |   3,650,000   |

As reported in the paper, 80% of the data is used for training, 10% for validation and the remaining 10% for test. All the dataset used in this experiments, together with the embeddings, are available [here](https://drive.google.com/open?id=1U2f7PfDYUrvfkIkNQPYR2OufAkuldNu6).

### Dataset statistics

In this section some statistics about the number of sentences and words in each document are reported. In the `plots` directory there are the distribution plots of these data. This kind of information are useful with the padding of the features. These data are obtained on the training and the validation set.

#### Yelp

* Number of sentences per document:

[//]: ![](plots/yelp_sent_per_doc.png)

| **Percentile** | 50% | 80% | 90% | 95% | 100% |
|----------------|-----|-----|-----|-----|------|
| **Value**      | 7   | 12  | 17  | 22  | 151  |


* Number of words per sentence:

[//]: ![](plots/yelp_words_per_sent.png)

| **Percentile** | 50% | 80% | 90% | 95% | 100% |
|----------------|-----|-----|-----|-----|------|
| **Value**      | 14  | 23  | 30  | 36  | 846  |

* Number of words per document:

[//]: ![](plots/yelp_words_per_doc.png)

| **Percentile** | 50% | 80% | 90% | 95% | 100% |
|----------------|-----|-----|-----|-----|------|
| **Value**      | 102 | 208 | 294 | 389 | 1234 |

#### Yahoo

* Number of sentences per document:

[//]: ![](plots/yahoo_sent_per_doc.png)

| **Percentile** | 50% | 80% | 90% | 95% | 100% |
|----------------|-----|-----|-----|-----|------|
| **Value**      | 4   | 8   | 11  | 16  | 514  |

* Number of words per sentence:

[//]: ![](plots/yahoo_words_per_sent.png)

| **Percentile** | 50% | 80% | 90% | 95% | 100%  |
|----------------|-----|-----|-----|-----|-------|
| **Value**      | 15  | 28  | 37  | 48  | 3977  |

* Number of words per document:

[//]: ![](plots/yahoo_words_per_doc.png)

| **Percentile** | 50% | 80% | 90% | 95% | 100% |
|----------------|-----|-----|-----|-----|------|
| **Value**      | 71  | 157 | 234 | 320 | 4001 |

#### Amazon

* Number of sentences per document:

[//]: ![](plots/amazon_sent_per_doc.png)

| **Percentile** | 50% | 80% | 90% | 95% | 100% |
|----------------|-----|-----|-----|-----|------|
| **Value**      | 4   | 10  | 16  | 23  | 660  |

* Number of words per sentence:

[//]: ![](plots/amazon_words_per_sent.png)

| **Percentile** | 50% | 80% | 90% | 95% | 100%  |
|----------------|-----|-----|-----|-----|-------|
| **Value**      | 17  | 28  | 35  | 43  | 1981  |

* Number of words per document:

[//]: ![](plots/amazon_words_per_doc.png)

| **Percentile** | 50% | 80% | 90% | 95% | 100% |
|----------------|-----|-----|-----|-----|------|
| **Value**      | 62  | 201 | 346 | 506 | 7485 |

## Results

Document classification, in percentage

|               | **Yelp** | **Yahoo** | **Amazon** |
|---------------|----------|-----------|------------|
| **BoW**       |   61.3   |   66.9    |    52.2    |
| **BoW-TFIDF** |   61.3   |   66.9    |    52.2    |
| **HAN**       |   ....   |   ....    |    ....    |

## Notes

The Yahoo Answer categories are mapped as the following:

|        **Domain**      | **Label** |
|------------------------|-----------|
| Business & Finance     | 0         |
| Computers & Internet   | 1         |
| Education & Reference  | 2         |
| Entertainment & Music  | 3         |
| Family & Relationships | 4         |
| Health                 | 5         |
| Politics & Government  | 6         |
| Science & Mathematics  | 7         |
| Society & Culture      | 8         |
| Sports                 | 9         |
