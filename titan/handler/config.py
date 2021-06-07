#   Copyright 2021 by Godwin peter <me@godwin.dev>, Tolaram Group.
#   All rights reserved.
#   This file is part of the the Titan micro task scheduler project,
#   and is released under the "MIT License Agreement". Please see the LICENSE
#   file that should have been included as part of this package.


from yamlreader import yaml_load
from titan.common.utils.log import logger


def get_all(location="conf/*.yaml"):
    default_config = {}
    try:
        config_value = yaml_load(location)
        default_config.update(config_value)
    except Exception as err:
        logger.error(err)
    return default_config


def value(obj_key):
    # Get an object with key
    pass
