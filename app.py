import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from prediction import *
from PIL import Image

model = joblib.load('Model/finalModel_xgb.pkl')

st.set_page_config(page_title="Accident Severity Prediction App",
                   page_icon="🚦", layout="wide")


#creating option list for dropdown menu
options_sex = ["Female", "Male"]
options_age = ['18-30', '31-50', 'Over 51', 'Under 18']
options_educational_level = ["Illiterate", 'Writing & reading', 'Elementary school', 'Junior high school', 'High school', "Above high school"]
options_driver_exp = ['5-10yr', '2-5yr', 'Above 10yr', '1-2yr', 'Below 1yr', 'No Licence', 'unknown']

options_day = ['Sunday', "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
options_owner_of_vehicle = ['Owner', "Governmental", "Organization", "Other"]
options_acc_area = ['Other', 'Office areas', 'Residential areas', ' Church areas',
       ' Industrial areas', 'School areas', '  Recreational areas',
       ' Outside rural areas', ' Hospital areas', '  Market areas',
       'Rural village areas', 'Unknown', 'Rural village areasOffice areas',
       'Recreational areas']
options_Lanes_or_Medians = ['Two-way (divided with broken lines road marking)',
       'Undivided Two way', 'other', 'Double carriageway (median)',
       'One way', 'Two-way (divided with solid lines road marking)',
       'Unknown']
options_road_allignment = ['Tangent road with flat terrain',
       'Tangent road with mild grade and flat terrain', 'Escarpments',
       'Tangent road with rolling terrain', 'Gentle horizontal curve',
       'Tangent road with mountainous terrain and',
       'Steep grade downward with mountainous terrain',
       'Sharp reverse curve',
       'Steep grade upward with mountainous terrain'
       ]
options_Types_of_Junction = ['No junction', 'Y Shape', 'Crossing', 'O Shape', 'Other',
       'Unknown', 'T Shape', 'X Shape']
options_Road_surface_type = ['Asphalt roads', 'Earth roads', 'Asphalt roads with some distress',
       'Gravel roads', 'Other']
options_Road_surface_conditions = ['Dry', 'Wet or damp', 'Snow', 'Flood over 3cm. deep']
options_Type_of_collision = ['Collision with roadside-parked vehicles',
       'Vehicle with vehicle collision',
       'Collision with roadside objects', 'Collision with animals',
       'Other', 'Rollover', 'Fall from vehicles',
       'Collision with pedestrians', 'With Train', 'Unknown']
options_Light_conditions = ['Daylight', 'Darkness - lights lit', 'Darkness - no lighting',
       'Darkness - lights unlit']
options_Weather_conditions = ['Normal', 'Raining', 'Raining and Windy', 'Cloudy', 'Other',
       'Windy', 'Snow', 'Unknown', 'Fog or mist']
options_Vehicle_movement = ['Going straight', 'U-Turn', 'Moving Backward', 'Turnover',
       'Waiting to go', 'Getting off', 'Reversing', 'Unknown', 'Parked',
       'Stopping', 'Overtaking', 'Other', 'Entering a junction']
options_Pedestrian_movement = ['Not a Pedestrian', "Crossing from driver's nearside",
       'Crossing from nearside - masked by parked or statioNot a Pedestrianry vehicle',
       'Unknown or other',
       'Crossing from offside - masked by  parked or statioNot a Pedestrianry vehicle',
       'In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing)',
       'Walking along in carriageway, back to traffic',
       'Walking along in carriageway, facing traffic',
       'In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing) - masked by parked or statioNot a Pedestrianry vehicle']
options_Number_of_vehicles_involved = [2, 1, 3, 6, 4, 7]       
options_Cause_of_accident = ['Moving Backward', 'Overtaking', 'Changing lane to the left',
       'Changing lane to the right', 'Overloading', 'Other',
       'No priority to vehicle', 'No priority to pedestrian',
       'No distancing', 'Getting off the vehicle improperly',
       'Improper parking', 'Overspeed', 'Driving carelessly',
       'Driving at high speed', 'Driving to the left', 'Unknown',
       'Overturning', 'Turnover', 'Driving under the influence of drugs',
       'Drunk driving']

features = ['Time', 'Day_of_week', 'Age_band_of_driver', 'Sex_of_driver',
       'Educational_level', 'Driving_experience', 'Owner_of_vehicle',
       'Area_accident_occured', 'Lanes_or_Medians', 'Road_allignment',
       'Types_of_Junction', 'Road_surface_type', 'Road_surface_conditions',
       'Light_conditions', 'Weather_conditions', 'Type_of_collision',
       'Number_of_vehicles_involved', 'Number_of_casualties',
       'Vehicle_movement', 'Pedestrian_movement', 'Cause_of_accident',
       ]

# st.markdown(
#     """
# <style>
# .reportview-container .markdown-text-container {
#     font-family: serif;
# }
# .sidebar .sidebar-content {
#     background-image: linear-gradient(#cf872e,#2e7bcf);
#     color: white;
# }
# .Widget>label {
#     color: white;
#     font-family: serif;
# }
# [class^="st-b"]  {
#     color: white;
#     font-family: monospace;
# }
# .st-bb {
#     background-color: transparent;
# }
# .st-at {
#     background-color: #0c0080;
# }
# footer {
#     font-family: monospace;
# }
# .reportview-container .main footer, .reportview-container .main footer a {
#     color: #0c0080;
# }
# header .decoration {
#     background-image: none;
# }

# </style>
# """,
#     unsafe_allow_html=True,
# )
st.markdown("<h1 style='text-align: center;'>Accident Severity Prediction Application 🚧</h1>", unsafe_allow_html=True)

image = Image.open('RTA1.png')
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(image, use_column_width=True)
def main():
    with st.form('prediction_form'):

        st.subheader("Enter the input for following features:")
        
        hour = st.slider("Pickup Hour: ", 0, 23, value=0, format="%d")
        sex = st.selectbox("Select sex of driver: ", options=options_sex)
        driver_age = st.selectbox("Select driver's age: ", options=options_age)
        educational_level = st.selectbox("Select driver's educational level: ", options=options_educational_level)
        driving_experience = st.selectbox("Select driving experience: ", options=options_driver_exp)
        day_of_week = st.selectbox("Select day of the week: ", options=options_day)
        owner_of_vehicle = st.selectbox("Select owner of vehicle: ", options=options_owner_of_vehicle)
        accident_area = st.selectbox("Select accident Area: ", options=options_acc_area)
        Types_of_Junction = st.selectbox("Select type of junction: ", options=options_Types_of_Junction)
        Road_surface_type = st.selectbox("Select surface of road: ", options=options_Road_surface_type)
        Road_surface_conditions = st.selectbox("Select surface conditions: ", options=options_Road_surface_conditions)
        Type_of_collision = st.selectbox("Select type of collison: ", options=options_Type_of_collision)
        Light_conditions = st.selectbox("Select light conditions: ", options=options_Light_conditions)
        Weather_conditions = st.selectbox("Select weather conditions: ", options=options_Weather_conditions)
        Vehicle_movement = st.selectbox("Select vehicle movement: ", options=options_Vehicle_movement)
        Pedestrian_movement = st.selectbox("Select pedestrian movement: ", options=options_Pedestrian_movement)
        Number_of_vehicles_involved = st.selectbox("Select no. of vehiclles involved: ", options=options_Number_of_vehicles_involved)
        Cause_of_accident = st.selectbox("Select cause of accident: ", options=options_Cause_of_accident)
        Number_of_casualties = st.slider("Pickup count of casualties: ", 1, 8, value=0, format="%d")
        Lanes_or_Medians  = st.selectbox("Select Lanes or Medians: ", options=options_Lanes_or_Medians)
        road_allignment  = st.selectbox("Select type of road allignment: ", options=options_road_allignment)
        
        
        submit = st.form_submit_button("Predict")


    if submit:
       Time = encodeTime(hour)
       sex = encodeSex(sex)
       educational_level = encodeEdu(educational_level)
       driving_experience = encodeDrivingExp(driving_experience) 
       driver_age = encodeAgeBand(driver_age)

       # data = np.array([Time, day_of_week, driver_age, sex,
       # educational_level, driving_experience, owner_of_vehicle,
       # accident_area, Lanes_or_Medians, road_allignment,
       # Types_of_Junction, Road_surface_type, Road_surface_conditions,
       # Light_conditions, Weather_conditions, Type_of_collision,
       # Number_of_vehicles_involved, Number_of_casualties,
       # Vehicle_movement, Pedestrian_movement, Cause_of_accident,
       # ]).reshape(1,-1)

       data1 = np.array([driving_experience, sex, driver_age, educational_level, Time]).reshape(1,-1)
       data2 = np.array([Number_of_vehicles_involved, Number_of_casualties]).reshape(1,-1)
       data3 = np.array([day_of_week, owner_of_vehicle, accident_area, Lanes_or_Medians, road_allignment, Types_of_Junction, Road_surface_type,
       Road_surface_conditions, Light_conditions, Weather_conditions, Type_of_collision, Vehicle_movement, Pedestrian_movement, Cause_of_accident])

       pred = get_prediction(data1, data2, data3, model=model)

       if pred == 'Slight injury':
              st.write('Thank God! It was a Slight Injury!')
       elif pred == 'Serious Injury':
              st.write('It seems like Serious Injury!')
       else:
              st.write('OMG it\'s a Fatal Injury. Hope the driver recovers fast.')
       #st.write(f"The predicted severity is:  {pred}")

if __name__ == '__main__':
    main()