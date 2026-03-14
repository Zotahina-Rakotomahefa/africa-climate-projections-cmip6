
import xarray as xr
import numpy as np

def stack_models(model_arrays):
    """
    Combines several models into one dimension 'model'
    """
    return xr.concat(model_arrays, dim="model")

def model_spread(model_stack):
    """
    Calculates average, minimum, and maximum of the models
    """
    mean = model_stack.mean("model")
    minimum = model_stack.min("model")
    maximum = model_stack.max("model")

    return mean, minimum, maximum

def intermodel_std(model_stack):
    """
    Standard deviation between models
    """
    return model_stack.std("model")

def coefficient_of_variation(mean, std):
    """
    Relative variability
    """
    return std / mean

def agreement_map(anomaly_datasets, var):

    stacked = xr.concat([ds[var] for ds in anomaly_datasets], dim="model")

    sign = np.sign(stacked)

    agreement = (sign > 0).sum("model")

    return agreement
