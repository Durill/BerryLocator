from rest_framework.decorators import api_view

from core import Geometry, SRID_EPSG


@api_view(http_method_names=['POST'])
def register_trip(request):
    geometry = request.data['geometry']
    #device_id = request.data['device_id']

    print(f'\ngeometry: {Geometry.create(geojson=geometry, geojson_srid=SRID_EPSG(4326))}\n')
