# -*- coding: utf-8 -*-

import logging
from pathlib import Path
import time
import urllib.request

import datasets.registry as registry


class Dataset:
    def __init__(self, url: str) -> None:
        self.url = url
        self.filename = self.url.split("/")[-1]

    def download(self, path: Path = Path.cwd(), isverbose: bool = True) -> None:
        if isverbose:
            self.__log_to_stdout()

        logging.info(f"Querying {self.url}")
        status, file_size = self.get_status()

        logging.info(f"HTTP Status: {status}")
        logging.info(f"File Size: {file_size:.2f} MB")

        logging.info(f"Downloading {self.filename} ({file_size:.2f} MB)")
        start = time.time()
        urllib.request.urlretrieve(self.url, path / self.url.split("/")[-1])
        elapsed = time.time() - start
        logging.info(f"Downloaded {self.filename} in {elapsed:.2f} seconds")

    def get_status(self) -> tuple[str, float]:
        req = urllib.request.Request(self.url, method="HEAD")
        f = urllib.request.urlopen(req)
        file_size = int(f.headers["Content-Length"]) / 1e6
        return f.status, file_size

    def __log_to_stdout(self) -> None:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)


def download_data(
    dataset_name: str, path: Path = Path.cwd(), isverbose: bool = True
) -> None:
    dataset = get_dataset(dataset_name)
    dataset.download(path, isverbose)


def get_dataset(dataset_name: str) -> Dataset:
    url = registry.REGISTRY[dataset_name]
    return Dataset(url)
