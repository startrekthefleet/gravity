#!/usr/bin/env python3

import argparse
import sys
from distutils.dir_util import copy_tree
from shutil import rmtree

grav_project_template_dir = "/opt/grav-1.7.42.3"

# Setup parser
parser = argparse.ArgumentParser(description="Project scaffolding tool for Grav (CMS)")

# Setup subparser for subcommands
subparsers = parser.add_subparsers(dest="command")

# Create parser with args for configuring email, API key, and/or mission id
init_command = subparsers.add_parser(
    "init", help="Initialize current working directory as Grav project"
)


if __name__ == "__main__":
    # Print help text if no arguments passed
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Parse arguments
    args = parser.parse_args()

    # Handle "init" command
    if args.command == "init":
        # copy content for Grav project scaffolding to current working directory
        copy_tree(grav_project_template_dir, ".")
        # remove bin/ directory
        rmtree("./bin")
