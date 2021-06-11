#   Copyright 2021 by Godwin peter <me@godwin.dev>, Tolaram Group.
#   All rights reserved.
#   This file is part of the the Titan micro task scheduler project,
#   and is released under the "MIT License Agreement". Please see the LICENSE
#   file that should have been included as part of this package.

import click
from titan.command import version

@click.group(
    help="Titan, easy-to-use python background task scheduler",
    invoke_without_command=True,
)
def instance():
    pass


def hook():

    # Bounded CLI commands
    instance.add_command(version.version)

    # Start execution
    instance()
