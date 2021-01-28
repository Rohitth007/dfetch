"""List metadata of all projects listed in the manifest.

For each project listed in the manifest the metadata is shown,
such as timestamp of last fetch, revision, remote url, etc.
"""

import argparse
import logging
import os

from colorama import Fore

import dfetch.commands.command
import dfetch.manifest.manifest
from dfetch.project.metadata import Metadata


logger = logging.getLogger(__name__)


class List(dfetch.commands.command.Command):
    """List metadata for each project.

    List all information provided in manifest and metadata files.
    """

    @staticmethod
    def create_menu(subparsers: "argparse._SubParsersAction") -> None:
        """Add the parser menu for this action."""
        dfetch.commands.command.Command.parser(subparsers, List)

    def __call__(self, args: argparse.Namespace) -> None:
        """Perform the list."""
        manifest, path = dfetch.manifest.manifest.get_manifest()

        with dfetch.util.util.in_directory(os.path.dirname(path)):
            for project in manifest.projects:
                metadata = Metadata.from_file(Metadata.from_project_entry(project).path)
                logger.info(f"  {Fore.GREEN}- {project.name}")
                logger.info(f"     {Fore.RED}{'remote':12s}: {project.remote}")
                logger.info(f"     {Fore.RED}{'remote url':12s}: {metadata.remote_url}")
                logger.info(f"     {Fore.RED}{'branch':12s}: {metadata.branch}")
                logger.info(f"     {Fore.RED}{'last fetch':12s}: {metadata.last_fetch}")
                logger.info(f"     {Fore.RED}{'revision':12s}: {metadata.revision}")
