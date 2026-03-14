
import xarray as xr
import numpy as np

def convert_temperature(ds, var="tas"):
    if ds[var].attrs.get("units") in ["K", "kelvin"]:
        ds[var] = ds[var] - 273.15
        ds[var].attrs["units"] = "°C"
    return ds

def convert_precipitation(ds, var="pr"):
    # kg m-2 s-1 → mm/month
    seconds_per_day = 86400
    ds[var] = ds[var] * seconds_per_day
    ds[var] = ds[var] * ds.time.dt.days_in_month
    ds[var].attrs["units"] = "mm/month"
    return ds

def standardize_coordinates(ds):
    if "latitude" in ds.coords:
        ds = ds.rename({"latitude": "lat"})
    if "longitude" in ds.coords:
        ds = ds.rename({"longitude": "lon"})
    return ds

def harmonize_calendar(ds):
    ds = xr.decode_cf(ds)
    return ds
