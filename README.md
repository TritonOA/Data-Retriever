# Data Retriever

This package provides tools to retrieve publicly available data from ocean acoustics experiments.

## Available Data

Data sets available for download are listed in the table below.
For information about the datasets, please consult the relevant reference websites.
We do not maintain these data sets and are unable to answer questions about them.

| Experiment | Event | Array | Download Size | Name (`dataset_name`) |
| --- | --- | --- | --- | --- |
| [SWellEx-96](http://swellex96.ucsd.edu) | S5 | VLA | 346.5 MB | `SWellEx96EventS5VLA` |
| [SWellEx-96](http://swellex96.ucsd.edu) | S5 | TLA | 385.6 MB | `SWellEx96EventS5TLA` |
| [SWellEx-96](http://swellex96.ucsd.edu) | S5 | HLA North | 378.1 MB | `SWellEx96EventS5HLANorth` |
| [SWellEx-96](http://swellex96.ucsd.edu) | S5 | HLA South | 392.7 MB | `SWellEx96EventS5HLASouth` |
| [SWellEx-96](http://swellex96.ucsd.edu) | S59 | VLA | 297 MB | `SWellEx96EventS59VLA` |
| [SWellEx-96](http://swellex96.ucsd.edu) | S59 | TLA | 335 MB | `SWellEx96EventS59TLA` |
| [SWellEx-96](http://swellex96.ucsd.edu) | S59 | HLA North | 481 | `SWellEx96EventS59HLANorth` |
| [SWellEx-96](http://swellex96.ucsd.edu) | S59 | HLA South | 499 MB | `SWellEx96EventS59HLASouth` |

## Installation

The package can be cloned directly from GitHub, or installed as a dependency via `pip`:
```bash
pip install git+https://github.com/TritonOA/Data-Retriever.git
```

The package has no dependencies outside the Python standard libraries.

## Usage

From the table above, select which dataset you wish to download. Provide the `dataset_name` argument and specify the `PATH_TO_SAVED_DATA` where you want it downloaded. If the `path` keyword argument is `None`, the data will be downloaded to your current working directory.

```python
from datasets import datasets

dataset = datasets.Dataset(dataset_name="SWellEx96EventS5VLA")
dataset.download(path=PATH_TO_SAVED_DATA)
```
