# 6.419x projects

The notebooks in this directory are worked examples from the Data Analysis course. They are valuable as case studies, but they are not official solutions and are not all guaranteed to run without the original course data.

## Setup

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Open a notebook from its project directory when it uses relative paths. Keep downloaded or private course data outside Git unless redistribution is permitted.

## Project data

- `HW1/` includes the local data used by the first homework notebooks.
- `CAVIAR/` contains the small network-analysis data archive.
- `Analysis5.ipynb` requires the OceanFlow dataset from the course. Set `OCEANFLOW_DATA` to the directory containing `1u.csv`, `1v.csv`, through `100u.csv`, `100v.csv` before running it. The dataset is not bundled here.

## Reproducibility checklist

Record the Python version, package versions, data source/cohort, and random seed when publishing a result. A notebook output saved on one machine is evidence of a past run, not a guarantee that a fresh run will reproduce it.
