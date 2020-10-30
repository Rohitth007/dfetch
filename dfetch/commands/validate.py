"""
Note that you can validate your manifest using :ref:`validate`.

This will parse your :ref:`Manifest` and check if all fields can be parsed.
"""

import argparse
import logging
import os

from colorama import Fore

import dfetch.commands.command
from dfetch.manifest.manifest import find_manifest
from dfetch.manifest.validate import validate

SCRIPT_PATH = os.path.dirname(__file__)
logger = logging.getLogger(__name__)


class Validate(dfetch.commands.command.Command):
    """Validate a manifest

    The Manifest is validated against a schema"""

    @staticmethod
    def create_menu(subparsers: "argparse._SubParsersAction") -> None:
        """ Add the parser menu for this action """
        dfetch.commands.command.Command.parser(subparsers, Validate)

    def __call__(self, args: argparse.Namespace) -> None:
        del args  # unused

        manifest_path = find_manifest()
        validate(manifest_path)
        manifest_path = os.path.relpath(manifest_path, os.getcwd())
        logger.info(f"{manifest_path}: {Fore.GREEN}valid")