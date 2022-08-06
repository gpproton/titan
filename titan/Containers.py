#  Copyright 2021 by Godwin peter <me@godwin.dev>, Tolaram Group.
#  All rights reserved.
#  This file is part of the the Titan micro task scheduler project,
#  and is released under the "MIT License Agreement". Please see the LICENSE
#  file that should have been included as part of this package.
from dependency_injector import containers, providers
from titan.common.defaults import constant


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    constant = providers.Factory(constant)
