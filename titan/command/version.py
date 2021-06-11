#   Copyright 2021 by Godwin peter <me@godwin.dev>, Tolaram Group.
#   All rights reserved.
#   This file is part of the the Titan micro task scheduler project,
#   and is released under the "MIT License Agreement". Please see the LICENSE
#   file that should have been included as part of this package.

import click
# from titan.handler.cli import instance as cli


@click.command()
@click.option('--version', '-v', help='Show application version.')
def version(version):
    click.echo(f'version check..')

# Command
# Option
