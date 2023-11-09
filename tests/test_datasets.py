#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, Mock
from pathlib import Path
from datasets import datasets


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


class TestSWellEx96EventS5VLA(unittest.TestCase):
    def test_init(self):
        dataset = datasets.SWellEx96EventS5VLA()
        self.assertEqual(dataset.url, datasets.DATASET_REGISTRY["SWellEx96EventS5VLA"])


class TestSWellEx96EventS5TLA(unittest.TestCase):
    def test_init(self):
        dataset = datasets.SWellEx96EventS5TLA()
        self.assertEqual(dataset.url, datasets.DATASET_REGISTRY["SWellEx96EventS5TLA"])


class TestSWellEx96EventS5HLANorth(unittest.TestCase):
    def test_init(self):
        dataset = datasets.SWellEx96EventS5HLANorth()
        self.assertEqual(
            dataset.url, datasets.DATASET_REGISTRY["SWellEx96EventS5HLANorth"]
        )


class TestSWellEx96EventS5HLASouth(unittest.TestCase):
    def test_init(self):
        dataset = datasets.SWellEx96EventS5HLASouth()
        self.assertEqual(
            dataset.url, datasets.DATASET_REGISTRY["SWellEx96EventS5HLASouth"]
        )


if __name__ == "__main__":
    unittest.main()
