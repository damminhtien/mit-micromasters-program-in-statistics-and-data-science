# 6.86x projects

This directory contains small Python projects, notebooks, datasets, and model artifacts from the Machine Learning course. For the public-facing catalog, see the repository's [reusable project gallery](../../docs/PROJECTS.md).

## Before running a project

From the repository root, install the shared baseline with `python -m pip install -r requirements.txt`. Then change into the project directory before running scripts so that relative dataset paths resolve correctly.

| Project | Focus | Local status |
| --- | --- | --- |
| [`project0/`](project0/) | Environment and starter checks | Small Python scripts |
| [`mnist/`](mnist/) | Linear models and neural networks | Includes local sample data and model files |
| [`project4_netflix/`](project4_netflix/) | Matrix completion and recommendation | Includes toy/test data; [`main.py`](project4_netflix/main.py) is the smallest smoke example |
| [`sentiment_analysis/`](sentiment_analysis/) | Text classification | Includes datasets, notebook, and [`test.py`](sentiment_analysis/test.py) |
| [`reinforcement_learning/`](reinforcement_learning/) | Reinforcement-learning notebook | Notebook example |

These are educational artifacts, not production benchmarks. Report the interpreter version, dependency versions, dataset variant, and random seed when comparing results.
