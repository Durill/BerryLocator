from typing import Union

from shapely.geometry.base import BaseGeometry, BaseMultipartGeometry


class Geometry:
    value: Union[BaseGeometry, BaseMultipartGeometry]
