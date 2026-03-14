
def compute_monthly_climatology(ds, var):
    return ds[var].groupby("time.month").mean("time")

def compute_annual_mean(ds, var):
    return ds[var].mean("time")

def compute_seasonal_mean(ds, var):
    return ds[var].groupby("time.season").mean("time")

def compute_anomaly(future, historical):
    return future - historical
