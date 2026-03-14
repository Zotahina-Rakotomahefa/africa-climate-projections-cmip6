# CMIP6 Climate Projection Analysis for Africa

---

##  Overview

This project provides a complete workflow for analyzing **historical and future climate projections over Africa using CMIP6 climate models**.

The pipeline processes NetCDF climate data, computes climatologies, generates future projections, evaluates model uncertainty, and produces scientific visualizations suitable for climate research and decision support.

The analysis focuses on two key climate variables:

 - Surface temperature

 - Precipitation

Future climate projections are evaluated using the **SSP245** and **SSP585** scenarios.

The project demonstrates a modular and reproducible climate analysis workflow using Python and open-source geospatial tools.

---

## Objectives

The main objectives of this project are:

 - Compute historical climatology (1985–2014) from CMIP6 models

 - Analyze future climate projections (2040–2069)

 - Calculate temperature and precipitation anomalies

 - Produce seasonal climate maps (DJF, JJA)

 - Evaluate inter-model uncertainty

 - Generate scientific figures for climate analysis

---

## Project structure
```
cmip6-madagascar-projection/
├── data/
     ├── boundaries/                      
     ├── processed/
     ├── raw/                          
     └── regridded/                           
├── notebooks/
    ├── 01_preprocessing.ipynb  
    ├── 02_historical_analysis.ipynb
    ├── 03_future_analysis.ipynb
    └── 04_uncertainty_analysis.ipynb
├── outputs/
    ├── figures/
    └── uncertain/     
├── src/ 
    ├── __init__.py                 
    ├── climatology.py                     
    ├── config.py               
    ├── data_loader.py          
    ├── ensemble.py    
    ├── masking.py             
    ├── preprocessing.py                    
    ├── regridding.py
    ├── uncertainty.py     
    └── visualization.py               
├── requirements.txt
└── README.md
```

---

## Technologies Used

The project relies on the following Python ecosystem:

 - Python

 - Xarray

 - NumPy

 - Matplotlib

 - Cartopy

 - GeoPandas

 - NetCDF4

These tools enable efficient processing of large climate datasets.

---

## Data Sources

Climate projections are derived from the **CMIP6 (Coupled Model Intercomparison Project Phase 6)** archive.

Variables analyzed include:

 - Surface Temperature (ts)

 - Precipitation (pr)

Future projections use the following **Shared Socioeconomic Pathways (SSP)**:

 -SSP245 : Intermediate emissions scenario

 -SSP585 : High emissions scenario

---

##  Climate Analysis Workflow

The project is organized into several analysis stages.

### Historical Climate Analysis

 - Period: 1985–2014

 - Multi-model climatology

 - Mean temperature and precipitation maps

### Future Climate Projections

 - Period: 2040–2069

 - Scenarios: SSP245 / SSP585

 - Computation of climate anomalies

Outputs include:

 - temperature anomaly maps

 - precipitation anomaly maps

 - seasonal projections (DJF, JJA)

### Uncertainty Analysis

Model uncertainty is evaluated using:

 - ensemble spread

 - model variability

 - individual model projections

Figures produced:

 - temperature uncertainty envelope

 - precipitation uncertainty envelope

 - individual model projection curves

---

##  Key Output

The workflow generates several scientific outputs including:

 - climatology maps

 - future anomaly maps

 - seasonal climate projections

 - uncertainty plots

Figures are saved in:

outputs/

---

##  Applications

This workflow can be used for:

 - climate research

 - environmental impact studies

 - climate risk analysis

 - climate services development

 - academic research

 - climate consulting projects

---

## Future Improvements

Possible extensions include:

 - extreme climate indices

 - trend analysis

 - drought indicators

 - climate hotspot detection

 - regional downscaling

---

## Author

Developed as part of a climate data science and geospatial analysis project focusing on climate change impacts over Africa.

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this software for academic, research, or commercial purposes, provided that proper attribution is given to the original author.

See the `LICENSE` file for full details
