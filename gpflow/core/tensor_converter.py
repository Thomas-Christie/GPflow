# Copyright 2017 Artem Artemev @awav
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from gpflow.misc import get_attribute
from gpflow.core.base import GPflowError
from gpflow.core.base import Parentable


class TensorConverter:  # pylint: disable=R0903
    __tensor_mode__ = '_tensor_mode'

    @classmethod
    def tensor_mode(cls, obj):
        if not isinstance(obj, Parentable):
            raise ValueError('Object must be .')
        while True:
            if get_attribute(obj, cls.__tensor_mode__, allow_none=True) is not None:
                return True
            parent = get_attribute(obj, '_parent')
            if parent is None:
                break
            if parent is obj:
                raise GPflowError('Inconsistency in parentable object found.')
            obj = parent
        return False
