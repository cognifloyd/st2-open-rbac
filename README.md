**StackStorm** is a platform for integration and automation across services and tools, taking actions in response to events. Learn more at [www.stackstorm.com](http://www.stackstorm.com/product).

# open_rbac for StackStorm

Open Source RBAC

To use, install in the /opt/stackstorm/st2 virtualenv.
No warranties or guarantees (as indicated in the Apache License). This is AS-IS and quality/fitness for any purpose is unknown.

## TODO

- [ ] Get the tests to run.

ST2 uses nosetest to run them but I'm more familiar with pytest.
Also, running tests with 3.1.0 is broken because some intermediate deps changed. One of the incompatibilities was fixed in master by upgrading cryptography to 2.8, but the other has not been fixed.
PRs welcome to get a good way to test this.


## Copyright, License, and Contributors Agreement

Copyright 2014-2018 StackStorm, Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License. You may obtain a copy of the License in the [LICENSE](LICENSE) file, or at:

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

By contributing you agree that these contributions are your own (or approved by your employer) and you grant a full, complete, irrevocable copyright license to all users and developers of the project, present and future, pursuant to the license of the project.
