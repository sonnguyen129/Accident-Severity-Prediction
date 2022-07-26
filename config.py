NUM_COLS = ['Number_of_vehicles_involved', 'Number_of_casualties']
ORD_COLS = ['Time','Age_band_of_driver', 'Driving_experience', 
                'Service_year_of_vehicle', 'Light_conditions', 'Age_band_of_casualty', 
                ]
NOM_COLs = ['Day_of_week', 'Vehicle_driver_relation', 'Road_surface_type', 'Road_surface_conditions',
            'Type_of_collision', 'Vehicle_movement', 'Work_of_casuality', 'Cause_of_accident']


Time_dict = {'Day': 0, 'Night': 1}
Age_band_of_driver_dict = {'Under 18' : 1, '18-30' : 2, '31-50' : 3, 'Over 51' : 4}
Driving_experience_dict = {'Below 1yr' : 1, '1-2yr' : 2, '2-5yr' : 3, '5-10yr' : 4, 'Above 10yr' : 5, 'No Licence' : 0}
Service_year_of_vehicle_dict = {'Below 1yr' : 1, '1-2yr' : 2, '2-5yrs' : 3, '5-10yrs' : 4, 'Above 10yr' : 5}
Light_conditions_dict = {'Darkness - no lighting' : 1, 'Darkness - lights lit' : 2, 'Daylight' : 3}
Age_band_of_casualty_dict = {'Under 18' : 1, '18-30' : 2, '31-50' : 3, 'Over 51' : 4}

Accident_severity_dict = {1: 'Slight Injury', 2: 'Serious Injury', 3: 'Fatal injury'}