#pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest
from unittest.mock import patch, mock_open

from dfetch.manifest import Manifest

VERSION_ONLY = u'''
manifest:
   version: 0
'''

def given_manifest_from_text(text):
    with patch('dfetch.manifest.open', mock_open(read_data=text)):
        return Manifest.from_file('manifest.yaml')

class TestParsing(unittest.TestCase):

    def test_can_read_version(self):
        manifest = given_manifest_from_text(VERSION_ONLY)
        self.assertEqual(manifest.version, 0)