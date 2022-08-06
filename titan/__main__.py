#  Copyright 2021 by Godwin peter <me@godwin.dev>, Tolaram Group.
#  All rights reserved.
#  This file is part of the the Titan micro task scheduler project,
#  and is released under the "MIT License Agreement". Please see the LICENSE
#  file that should have been included as part of this package.
import sys
from titan import main
from titan.Containers import Container
from titan.common.defaults import constant


if __name__ == "__main__":
    container = Container()
    container.config.from_yaml(constant.project_configuration)
    container.init_resources()
    container.wire(modules=[sys.modules[__name__]])

    main()
