# Reusable project gallery

This is the practical layer of the archive: small implementations, notebooks, datasets, and utilities that another learner can inspect, run, adapt, or use as a starting point. They are course-derived educational artifacts, not production packages or official solutions.

## At a glance

| Project | What can be reused | Main entry point | Data and evidence |
| --- | --- | --- | --- |
| [Matrix completion and recommendation](../6.86x_machinelearning/projects/project4_netflix/) | EM and K-means mixture-model components, BIC model selection, and missing-matrix filling | [`main.py`](../6.86x_machinelearning/projects/project4_netflix/main.py) | Toy and complete/incomplete matrices are included; `python main.py` passes in this checkout |
| [Sentiment classification](../6.86x_machinelearning/projects/sentiment_analysis/) | Bag-of-words extraction, perceptron variants, Pegasos, accuracy evaluation, and hyperparameter helpers | [`project1.py`](../6.86x_machinelearning/projects/sentiment_analysis/project1.py) | Train/validation/test TSVs are included; `python test.py` passes in this checkout |
| [MNIST model baselines](../6.86x_machinelearning/projects/mnist/) | PCA, softmax regression, feature transforms, PyTorch training utilities, FC and CNN models | [`softmax.py`](../6.86x_machinelearning/projects/mnist/part1/softmax.py) | MNIST data and model artifacts are included; training is intentionally not benchmarked here |
| [High-dimensional analysis](../6.419x_dataanalysis/projects/) | A notebook pattern for transform → PCA → visualization → clustering → feature selection | [`Analysis1.ipynb`](../6.419x_dataanalysis/projects/Analysis1.ipynb) | Course data paths vary by assignment; treat notebooks as adaptable case studies |
| [CAVIAR network analysis](../6.419x_dataanalysis/projects/Analysis3_1.ipynb) | Temporal network exploration across eleven intervention phases | [`Analysis3_1.ipynb`](../6.419x_dataanalysis/projects/Analysis3_1.ipynb) | Phase CSVs are bundled in [`CAVIAR/`](../6.419x_dataanalysis/projects/CAVIAR/) |

## 1. Matrix completion and recommendation

The [`project4_netflix`](../6.86x_machinelearning/projects/project4_netflix/) folder is the strongest algorithm-focused example. It separates the Gaussian-mixture model, EM updates, K-means baseline, plotting, BIC selection, and matrix filling into small Python modules.

Reusable pieces:

- [`common.py`](../6.86x_machinelearning/projects/project4_netflix/common.py) — model container, initialization, plotting, RMSE, and BIC.
- [`em.py`](../6.86x_machinelearning/projects/project4_netflix/em.py) — EM updates and `fill_matrix`.
- [`kmeans.py`](../6.86x_machinelearning/projects/project4_netflix/kmeans.py) — hard-assignment baseline.

Run the included toy-data model-selection example from its directory:

```bash
cd 6.86x_machinelearning/projects/project4_netflix
python main.py
```

The current smoke run selects `K = 3` on the bundled toy data. Missing entries are represented by zero and the implementation uses a spherical Gaussian mixture, so adapt those assumptions before applying it to a real recommender system.

## 2. Sentiment classification

The [`sentiment_analysis`](../6.86x_machinelearning/projects/sentiment_analysis/) folder exposes a compact classical-ML pipeline without an external service. [`project1.py`](../6.86x_machinelearning/projects/sentiment_analysis/project1.py) contains hinge loss, perceptron variants, Pegasos, classification, bag-of-words, and feature-vector construction; [`utils.py`](../6.86x_machinelearning/projects/sentiment_analysis/utils.py) contains data loading and tuning helpers.

Run the local correctness harness:

```bash
cd 6.86x_machinelearning/projects/sentiment_analysis
python test.py
```

The runner accepts `SENTIMENT_DATA_DIR` when the TSV files live elsewhere. The included harness validates core functions; it is not a replacement for evaluating a new dataset.

## 3. MNIST model baselines

The [`mnist`](../6.86x_machinelearning/projects/mnist/) folder shows a useful progression from classical models to neural networks:

- [`part1/softmax.py`](../6.86x_machinelearning/projects/mnist/part1/softmax.py) — multiclass softmax regression and gradient descent.
- [`part1/features.py`](../6.86x_machinelearning/projects/mnist/part1/features.py) — cubic features and PCA projection helpers.
- [`part2-mnist/train_utils.py`](../6.86x_machinelearning/projects/mnist/part2-mnist/train_utils.py) — batching, training epochs, and accuracy.
- [`part2-mnist/nnet_fc.py`](../6.86x_machinelearning/projects/mnist/part2-mnist/nnet_fc.py) and [`nnet_cnn.py`](../6.86x_machinelearning/projects/mnist/part2-mnist/nnet_cnn.py) — fully connected and convolutional models.

The data layout is local and the scripts are intentionally easy to read. Treat saved model files and accuracy values as artifacts of a past run, not universal benchmarks.

## 4. High-dimensional and network notebooks

The 6.419x notebooks are reusable analytical patterns rather than installable libraries:

- [`Analysis1.ipynb`](../6.419x_dataanalysis/projects/Analysis1.ipynb) — transform data, compare PCA/MDS/t-SNE, and cluster.
- [`Analysis2_1.ipynb`](../6.419x_dataanalysis/projects/Analysis2_1.ipynb) and [`Analysis2_2.ipynb`](../6.419x_dataanalysis/projects/Analysis2_2.ipynb) — visualize large unlabeled data, cluster, and select features.
- [`Analysis3_1.ipynb`](../6.419x_dataanalysis/projects/Analysis3_1.ipynb) — investigate a time-varying criminal network with the bundled CAVIAR phases.

Some notebooks depend on course datasets that are not bundled. Read the [6.419x project runbook](../6.419x_dataanalysis/projects/README.md) before running them and record the dataset version, Python packages, and random seed.

## Reuse checklist

1. Read the local project README and inspect the data assumptions.
2. Install the shared baseline from the repository root: `python -m pip install -r requirements.txt`.
3. Run the smallest test or toy-data example before changing the algorithm.
4. Replace course data only after checking its license and documenting the new schema.
5. Report the Python version, package versions, dataset/cohort, and seed with any result.

For ownership, redistribution, and third-party material boundaries, see [content provenance](PROVENANCE.md).
