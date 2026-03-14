
import xarray as xr
import geopandas as gpd

def load_dataset(path):
    return xr.open_dataset(path)

def load_africa_boundary(path):
    return gpd.read_file(path)

def subset_period(ds, period):
    return ds.sel(time=slice(period[0], period[1]))

def subset_bbox(ds, bbox):
    return ds.sel(
        lon=slice(bbox["lon_min"], bbox["lon_max"]),
        lat=slice(bbox["lat_min"], bbox["lat_max"])
    )
