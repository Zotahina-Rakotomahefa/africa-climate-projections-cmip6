
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd
import numpy as np
import os

BOUNDARY_PATH = "/content/drive/MyDrive/cmip6-madagascar-projection/data/boundaries/ne_10m_admin_0_countries.shp"
OUTPUT_FIG_PATH = "/content/drive/MyDrive/cmip6-madagascar-projection/outputs/figures"

os.makedirs(OUTPUT_FIG_PATH, exist_ok=True)

def plot_africa_map(data, title, cmap="coolwarm", save_name=None):

    africa = gpd.read_file(BOUNDARY_PATH)

    fig = plt.figure(figsize=(10, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.set_extent([-20, 55, -40, 40], crs=ccrs.PlateCarree())

    gl = ax.gridlines(
        draw_labels=True,
        linewidth=0.5,
        color="gray",
        alpha=0.5,
        linestyle="--"
    )

    gl.top_labels = False
    gl.right_labels = False

    if "Precipitation" in title:
        cmap = "PuBuGn"
        unit = "mm / month"
    else:
        cmap = "coolwarm"
        unit = "°C"

    im = data.plot(
        ax=ax,
        transform=ccrs.PlateCarree(),
        cmap=cmap,
        add_colorbar=False
    )

    africa.boundary.plot(
        ax=ax,
        linewidth=0.6,
        edgecolor="black"
    )

    for idx, row in africa.iterrows():

        if row["NAME"] in [
            "Madagascar",
            "South Africa",
            "Kenya",
            "Ethiopia",
            "Nigeria",
            "Egypt",
            "Algeria"
        ]:

            centroid = row.geometry.centroid

            ax.text(
                centroid.x,
                centroid.y,
                row["NAME"],
                fontsize=7,
                transform=ccrs.PlateCarree(),
                ha="center"
            )

    cbar = plt.colorbar(im, ax=ax, orientation="horizontal", pad=0.06)

    cbar.set_label(unit)

    plt.title(title, fontsize=12)

    if save_name is not None:

      save_path = os.path.join(
           OUTPUT_FIG_PATH,
           f"{save_name}.png"
    )

      plt.savefig(
          save_path,
          dpi=300,
          bbox_inches="tight"
    )

      print("Figure saved :", save_path)

    plt.show()
