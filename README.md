# surfs_up
## Overview
The purpose of this module was to see the weather patterns, specifically the temperatures for the months of December and June. The analys swa done to see if the tempetures for those months would make the business sustainable year round. 

## Results

The following code was used to calculate the descriptive statitsics for the months of June for temperature. 

          june_temps = session.query(Measurement.date, Measurement.tobs).\ filter(extract('month', Measurement.date) == '6').all()
          june_temps_df = pd.DataFrame(results, columns = ['date', 'June temps'])
          june_temps_df.set_index(june_temps_df['date'], inplace = True)
          june_temps_df.sort_index()
          june_temps_df.describe()


A refactored code was also used to get the percipitation by replacing the 'Measurment.tobs' to 'Measurement.prcp', and the month were changed from june to December by changing the the '6' to '12'. The following results were gathered from the data. 

June temps
* mean	74.944118
* min	64.000000
* max	85.000000

December temps. 
* mean	71.041529
* min	56.000000
* max	83.000000

June percipitation
* mean	0.136360
* min	0.000000
* max	4.430000

December percipitation
* mean	0.216819
* min	0.000000
* max	6.420000

Results show that the weather in the months of June and December are consistent and vary little when compared to one another. The temperature for June and December decrease with the months as predicted. However, the weather in the winter has a higher average percipitation than july, but the difference is miniscule. 