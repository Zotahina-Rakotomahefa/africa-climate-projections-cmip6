
import xarray as xr

def multi_model_mean(datasets, var):
    stacked = xr.concat([ds[var] for ds in datasets], dim="model")
    return stacked.mean("model")
