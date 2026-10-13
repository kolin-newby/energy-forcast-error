# Energy Forecast Error and Weather Extremes
This project is a small learning project I am attempting to refresh my data-science skills and express my passion for environmental and clean energy topics. It looks at the connection between the error in energy load forecast data on a daily basis and weather events like heat waves, cold snaps, and extreme storms.

I am utilizing EIA for power demand and forecast data and intend to use NOAA GHCNh weather station data for stations in the counties associated with the balancing authorities from the EIA data.

## Status
I have successfully setup the project to pull daily EIA data from their API. The data is cleaned and organized in a notebook and further utilized to create plots using `matplotlib`. These plots are currently for the month of January 2019. See a few examples of these figures below or look at the current state of the figures for all regions in `/reports/figures/`

<div style={{display: flex; flex-wrap: wrap; width: 100%}}>
  <img width="49%" alt="CAL" src="https://github.com/user-attachments/assets/645c3de5-bef6-4ca4-b8ad-5235dba88534" />
  <img width="49%" alt="MIDW" src="https://github.com/user-attachments/assets/78bebf4d-6381-4c24-8d80-1c4b5e3a4d3a" />
  <img width="49%" alt="TEX" src="https://github.com/user-attachments/assets/c41369ae-bd73-4f32-a76d-20e2a2397d2b" />
  <img width="49%" alt="SE" src="https://github.com/user-attachments/assets/e959f2f9-4757-44e2-a6b3-5e836d91c7f1" />

</div>

## Next Steps
I will refine the data pipeline a bit more to assure the collection of data is smooth and then move on to collection weather data from a new source, likely NOAA GHCNh (as discussed above). That data will need to go through a similar cleaning and organization process before I can combine the two data sources together.
