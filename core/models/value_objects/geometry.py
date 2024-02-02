from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from enum import IntEnum

from shapely.errors import ShapelyError
from shapely.geometry.base import BaseGeometry, BaseMultipartGeometry
from shapely.geometry import shape as as_shape

__all__ = (
    "SRID_EPSG",
    "Geometry",
)


class SRID_EPSG(IntEnum):
    _3857 = 3857
    _4326 = 4326

    @classmethod
    def as_expression(cls, enum: SRID_EPSG) -> str:
        return f"EPSG:{enum.value}"


@dataclass
class Geometry:
    """
    Value of geometry is parsed from valid GeoJSON

    For full format reference:
    https://www.rfc-editor.org/rfc/rfc7946#appendix-A

    For transformation check see:
    https://epsg.io/
    """
    value: Union[BaseGeometry, BaseMultipartGeometry]
    srid: SRID_EPSG = SRID_EPSG._4326  # WGS-84 - default for GeoJSON

    @classmethod
    def create(
        cls,
        geojson: dict,
        geojson_srid: SRID_EPSG
    ) -> Geometry:

        if not isinstance(geojson, dict):
            raise  # Geometry invalid argument

        try:
            shape = as_shape(context=geojson)
        except (TypeError, ValueError) as error:
            raise  # Geometry not parsable
        except ShapelyError as error:
            raise  # Geometry not parsable from e

        geometry = cls(value=shape, srid=geojson_srid)

        return geometry