
import xarray as xr
import numpy as np

def create_target_grid(resolution=1.0):
    lat = np.arange(-40, 40 + resolution, resolution)
    lon = np.arange(-20, 55 + resolution, resolution)
    return lat, lon


def regrid_dataset(ds, target_lat, target_lon, method="linear"):
    """
    method: 'linear' or 'nearest'
    """
    return ds.interp(
        lat=target_lat,
        lon=target_lon,
        method=method
    )
