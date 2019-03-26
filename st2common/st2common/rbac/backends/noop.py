# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from st2common.rbac.backends.base import BaseRBACBackend
from st2common.rbac.backends.base import BaseRBACPermissionResolver
from st2common.rbac.backends.base import BaseRBACRemoteGroupToRoleSyncer

__all__ = [
    'NoOpRBACBackend',
    'NoOpRBACPermissionResolver',
    'NoOpRBACRemoteGroupToRoleSyncer'
]


class NoOpRBACBackend(BaseRBACBackend):
    """
    NoOp RBAC backend.
    """
    def get_resolver_for_resource_type(resource_type):
        return NoOpRBACPermissionResolver()

    def get_resolver_for_permission_type(permission_type):
        return NoOpRBACPermissionResolver()

    def get_remote_group_to_role_syncer(self):
        pass


class NoOpRBACPermissionResolver(BaseRBACPermissionResolver):
    """
    No-op RBAC permission resolver for installations without RBAC.
    """

    def user_has_permission(self, user_db, permission_type):
        return True

    def user_has_resource_api_permission(self, user_db, resource_api, permission_type):
        return True

    def user_has_resource_db_permission(self, user_db, resource_db, permission_type):
        return True


class NoOpRBACRemoteGroupToRoleSyncer(BaseRBACRemoteGroupToRoleSyncer):
    def sync(self, user_db, groups):
        return []
