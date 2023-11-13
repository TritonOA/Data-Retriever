#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import unittest
from unittest.mock import patch, MagicMock, Mock

from datasets import datasets, registry


class TestDataset(unittest.TestCase):
    @patch("datasets.datasets.urllib.request.urlopen")
    def test_get_status(self, mock_urlopen):
        # Mocking the return value of urlopen
        mock_response = Mock()
        mock_response.status = 200
        mock_response.headers = {"Content-Length": "1000000"}
        mock_urlopen.return_value = mock_response

        dataset = datasets.Dataset("http://example.com")
        status, size = dataset.get_status()

        self.assertEqual(status, 200)
        self.assertEqual(size, 1)

    @patch("datasets.datasets.urllib.request.urlretrieve")
    @patch("datasets.datasets.urllib.request.urlopen")
    def test_download(self, mock_urlopen, mock_urlretrieve):
        # Mocking the return values of urlopen and urlretrieve
        mock_response = Mock()
        mock_response.status = 200
        mock_response.headers = {"Content-Length": "1000000"}
        mock_urlopen.return_value = mock_response

        dataset = datasets.Dataset("http://example.com")
        dataset.download(Path.cwd(), False)

        mock_urlretrieve.assert_called_once_with(
            dataset.url, Path.cwd() / dataset.filename
        )


class TestDownloadData(unittest.TestCase):
    @patch("datasets.datasets.get_dataset")
    def test_download_data(self, mock_get_dataset):
        # Create a mock dataset object with a mock download method
        mock_dataset = MagicMock(spec=datasets.Dataset)
        mock_get_dataset.return_value = mock_dataset

        # Call the function we are testing
        datasets.download_data("SWellEx96EventS5VLA", Path("/tmp"), False)

        # Check that get_dataset was called with the correct argument
        mock_get_dataset.assert_called_once_with("SWellEx96EventS5VLA")

        # Check that the download method was called with the correct arguments
        mock_dataset.download.assert_called_once_with(Path("/tmp"), False)


class TestGetDataset(unittest.TestCase):
    @patch("datasets.registry.REGISTRY", registry.REGISTRY)
    def test_get_dataset(self):
        dataset = datasets.get_dataset("SWellEx96EventS5VLA")
        self.assertIsInstance(dataset, datasets.Dataset)
        self.assertEqual(
            dataset.url, "http://swellex96.ucsd.edu/downloads/J1312315.vla.21els.sio.gz"
        )


if __name__ == "__main__":
    unittest.main()
