
import numpy as np
import xarray as xr
from shapely.geometry import Point
from shapely.ops import unary_union


def apply_africa_mask(ds, africa_shape):

    africa_polygon = unary_union(africa_shape.geometry)

    lat = ds.lat.values
    lon = ds.lon.values

    lon2d, lat2d = np.meshgrid(lon, lat)

    mask = np.zeros(lon2d.shape, dtype=bool)

    for i in range(lon2d.shape[0]):
        for j in range(lon2d.shape[1]):

            point = Point(lon2d[i, j], lat2d[i, j])

            mask[i, j] = africa_polygon.contains(point)

    mask = xr.DataArray(
        mask,
        coords={"lat": lat, "lon": lon},
        dims=("lat", "lon")
    )

    return ds.where(mask)
