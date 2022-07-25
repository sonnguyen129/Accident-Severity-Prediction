import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def get_prediction(data1, data2, data3, model):
  """
  Predict the class of a given data point.
  """
  data1Cols = ['Driving_experience', 'Sex_of_driver', 'Age_band_of_driver', 'Educational_level', 'Time']
    
  data3Cols = ['Day_of_week_Friday', 'Day_of_week_Monday', 'Day_of_week_Saturday', 'Day_of_week_Sunday', 'Day_of_week_Thursday', 'Day_of_week_Tuesday', 'Day_of_week_Wednesday', 'Owner_of_vehicle_Governmental', 'Owner_of_vehicle_Organization', 'Owner_of_vehicle_Other', 'Owner_of_vehicle_Owner', 'Area_accident_occured_  Market areas', 'Area_accident_occured_  Recreational areas', 'Area_accident_occured_ Church areas', 'Area_accident_occured_ Hospital areas', 'Area_accident_occured_ Industrial areas', 'Area_accident_occured_ Outside rural areas', 'Area_accident_occured_Office areas', 'Area_accident_occured_Other', 'Area_accident_occured_Recreational areas', 'Area_accident_occured_Residential areas', 'Area_accident_occured_Rural village areas', 'Area_accident_occured_Rural village areasOffice areas', 'Area_accident_occured_School areas', 'Area_accident_occured_Unknown', 'Lanes_or_Medians_Double carriageway (median)', 'Lanes_or_Medians_One way', 'Lanes_or_Medians_Two-way (divided with broken lines road marking)', 'Lanes_or_Medians_Two-way (divided with solid lines road marking)', 'Lanes_or_Medians_Undivided Two way', 'Lanes_or_Medians_Unknown', 'Lanes_or_Medians_other', 'Road_allignment_Escarpments', 'Road_allignment_Gentle horizontal curve', 'Road_allignment_Sharp reverse curve', 'Road_allignment_Steep grade downward with mountainous terrain', 'Road_allignment_Steep grade upward with mountainous terrain', 'Road_allignment_Tangent road with flat terrain', 'Road_allignment_Tangent road with mild grade and flat terrain', 'Road_allignment_Tangent road with mountainous terrain and', 'Road_allignment_Tangent road with rolling terrain', 'Types_of_Junction_Crossing', 'Types_of_Junction_No junction', 'Types_of_Junction_O Shape', 'Types_of_Junction_Other', 'Types_of_Junction_T Shape', 'Types_of_Junction_Unknown', 'Types_of_Junction_X Shape', 'Types_of_Junction_Y Shape', 'Road_surface_type_Asphalt roads', 'Road_surface_type_Asphalt roads with some distress', 'Road_surface_type_Earth roads', 'Road_surface_type_Gravel roads', 'Road_surface_type_Other', 'Road_surface_conditions_Dry', 'Road_surface_conditions_Flood over 3cm. deep', 'Road_surface_conditions_Snow', 'Road_surface_conditions_Wet or damp', 'Light_conditions_Darkness - lights lit', 'Light_conditions_Darkness - lights unlit', 'Light_conditions_Darkness - no lighting', 'Light_conditions_Daylight', 'Weather_conditions_Cloudy', 'Weather_conditions_Fog or mist', 'Weather_conditions_Normal', 'Weather_conditions_Other', 'Weather_conditions_Raining', 'Weather_conditions_Raining and Windy', 'Weather_conditions_Snow', 'Weather_conditions_Unknown', 'Weather_conditions_Windy', 'Type_of_collision_Collision with animals', 'Type_of_collision_Collision with pedestrians', 'Type_of_collision_Collision with roadside objects', 'Type_of_collision_Collision with roadside-parked vehicles', 'Type_of_collision_Fall from vehicles', 'Type_of_collision_Other', 'Type_of_collision_Rollover', 'Type_of_collision_Unknown', 'Type_of_collision_Vehicle with vehicle collision', 'Type_of_collision_With Train', 'Vehicle_movement_Entering a junction', 'Vehicle_movement_Getting off', 'Vehicle_movement_Going straight', 'Vehicle_movement_Moving Backward', 'Vehicle_movement_Other', 'Vehicle_movement_Overtaking', 'Vehicle_movement_Parked', 'Vehicle_movement_Reversing', 'Vehicle_movement_Stopping', 'Vehicle_movement_Turnover', 'Vehicle_movement_U-Turn', 'Vehicle_movement_Unknown', 'Vehicle_movement_Waiting to go', "Pedestrian_movement_Crossing from driver's nearside", 'Pedestrian_movement_Crossing from nearside - masked by parked or statioNot a Pedestrianry vehicle', 'Pedestrian_movement_Crossing from offside - masked by  parked or statioNot a Pedestrianry vehicle', 'Pedestrian_movement_In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing)', 'Pedestrian_movement_In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing) - masked by parked or statioNot a Pedestrianry vehicle', 'Pedestrian_movement_Not a Pedestrian', 'Pedestrian_movement_Unknown or other', 'Pedestrian_movement_Walking along in carriageway, back to traffic', 'Pedestrian_movement_Walking along in carriageway, facing traffic', 'Cause_of_accident_Changing lane to the left', 'Cause_of_accident_Changing lane to the right', 'Cause_of_accident_Driving at high speed', 'Cause_of_accident_Driving carelessly', 'Cause_of_accident_Driving to the left', 'Cause_of_accident_Driving under the influence of drugs', 'Cause_of_accident_Drunk driving', 'Cause_of_accident_Getting off the vehicle improperly', 'Cause_of_accident_Improper parking', 'Cause_of_accident_Moving Backward', 'Cause_of_accident_No distancing', 'Cause_of_accident_No priority to pedestrian', 'Cause_of_accident_No priority to vehicle', 'Cause_of_accident_Other', 'Cause_of_accident_Overloading', 'Cause_of_accident_Overspeed', 'Cause_of_accident_Overtaking', 'Cause_of_accident_Overturning', 'Cause_of_accident_Turnover', 'Cause_of_accident_Unknown']

  df1 = pd.DataFrame(data1, columns=data1Cols)
  df2 = pd.DataFrame(data2, columns=['Number_of_vehicles_involved', 'Number_of_casualties'])

  # Preparing dict
  colsDict = dict()
  index = list(range(123))
  for col, index in zip(data3Cols, index):
    colsDict[col] = index

  #Preparing data3
  zeros = np.zeros(123).astype(int)
  for value in data3:
    for col in data3Cols:
      if col.__contains__(value):
        zeros[colsDict[col]] = 1
        break
  
  #Making df3
  df3 = pd.DataFrame(zeros.reshape(1,-1), columns=data3Cols)

  #Making final_df
  final_df = pd.concat([df1, df2, df3], axis=1)

  prediction = model.predict(final_df)[0]
  accident_severity = {2: 'Fatal injury', 1 : 'Serious injury' , 0:'Slight injury'}


  return accident_severity[prediction]









