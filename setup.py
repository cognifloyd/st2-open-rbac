# -*- coding: utf-8 -*-
# Copyright 2019 Extreme Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path

from setuptools import setup, find_packages

from dist_utils import fetch_requirements
from dist_utils import apply_vagrant_workaround
from dist_utils import get_version_string

ST2_COMPONENT = 'open_rbac'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS_FILE = os.path.join(BASE_DIR, 'requirements.txt')
INIT_FILE = os.path.join(BASE_DIR, 'src/open_rbac/__init__.py')

install_reqs, dep_links = fetch_requirements(REQUIREMENTS_FILE)

apply_vagrant_workaround()
setup(
    name=ST2_COMPONENT,
    version=get_version_string(INIT_FILE),
    description='Open Source RBAC for StackStorm',
    author="Jacob Floyd (based on Stackstorm's work)",
    author_email='cognifloyd@gmail.com',
    license='Apache License (2.0)',
    url='https://stackstorm.com/',
    install_requires=install_reqs,
    dependency_links=dep_links,
    test_suite=ST2_COMPONENT,
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['setuptools', 'tests']),
    scripts=[
        'bin/st2-apply-rbac-definitions',
    ],
    entry_points={
        'st2common.rbac.backend': [
            # TODO: we might need to do something to silence the non-enterpirse warning
            #       triggered if cfg.CONF.rbac.enable and cfg.CONF.rbac.backend != 'enterprise'
            #       aargh. It's now raising a ValueError in st2api... Might need a monkeypatch to adjust. :(
            #       or we have to name this "enterprise" even though its not the same thing.
            #       Now it must both be the backend setting, and must be in stevedore's list of backends.
            #       Yeah, this has to be enterprise. :(
            # 'openrbac = open_rbac.backend:OpenRBACBackend'
            'enterprise = open_rbac.backend:OpenRBACBackend'
        ],
    },
)
