import streamlit as st
import pandas as pd
import numpy as np
import joblib
from prediction import *
from config import *
from PIL import Image
import pickle
from xgboost import XGBClassifier

def load_encoding():
       with open(r'model/checkpoint.pkl', 'rb') as file:
              data = pickle.load(file)
       return data

data = load_encoding()

# Load model and encoding
xgb = XGBClassifier()
xgb.load_model(r'model/model_xgb.bin')

le_Day_of_week = data['le_Day_of_week']
le_Vehicle_driver_relation = data['le_Vehicle_driver_relation']
le_Road_surface_type = data['le_Road_surface_type']
le_Road_surface_conditions = data['le_Road_surface_conditions']
le_Type_of_collision = data['le_Type_of_collision']
le_Vehicle_movement = data['le_Vehicle_movement']
le_Work_of_casuality = data['le_Work_of_casuality']
le_Cause_of_accident = data['le_Cause_of_accident']


st.set_page_config(page_title="Accident Severity Prediction App",
                     page_icon="🚦", layout="wide")


#creating option list for dropdown menu
options_time = ["Day", "Night"]
options_day = ['Sunday', "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
options_age = ['18-30', '31-50', 'Over 51', 'Under 18']
options_Vehicle_driver_relation = ['Employee', 'Owner']
options_driver_exp = ['5-10yr', '2-5yr', 'Above 10yr', '1-2yr', 'Below 1yr', 'No Licence']
options_Service_year_of_vehicle = ['Below 1yr', '1-2yr', '2-5yrs', '5-10yrs', 'Above 10yr']
options_Road_surface_type = ['Asphalt roads', 'Earth roads', 'Asphalt roads with some distress',
                            'Gravel roads', 'other']
options_Road_surface_conditions = ['Dry', 'Wet or damp', 'Snow', 'Flood over 3cm. deep']
options_Light_conditions = ['Darkness - no lighting', 'Darkness - lights lit', 'Daylight']
options_Type_of_collision = ['Collision with roadside-parked vehicles',
                            'Vehicle with vehicle collision',
                            'Collision with roadside objects', 'Collision with animals',
                            'Rollover', 'Fall from vehicles',
                            'Collision with pedestrians', 'With Train']
options_Vehicle_movement = ['Going straight', 'U-Turn', 'Moving Backward', 'Turnover',
                            'Waiting to go', 'Getting off', 'Reversing', 'Parked',
                            'Stopping', 'Overtaking', 'Entering a junction']
options_Age_band_of_casualty = ['Under 18', '18-30', '31-50', 'Over 51']
options_Work_of_casuality = ['Driver', 'Employee', 'Self-employed', 'Student', 'Unemployed']
options_Cause_of_accident = ['Moving Backward', 'Overtaking', 'Changing lane to the left',
              'Changing lane to the right', 'Overloading',
              'No priority to vehicle', 'No priority to pedestrian',
              'No distancing', 'Getting off the vehicle improperly',
              'Improper parking', 'Overspeed', 'Driving carelessly',
              'Driving at high speed', 'Driving to the left', 
              'Overturning', 'Turnover', 'Driving under the influence of drugs',
              'Drunk driving']

features = ['Time', 'Day_of_week', 'Age_band_of_driver', 'Vehicle_driver_relation',
       'Driving_experience', 'Service_year_of_vehicle', 'Road_surface_type',
       'Road_surface_conditions', 'Light_conditions', 'Type_of_collision',
       'Number_of_vehicles_involved', 'Number_of_casualties', 'Vehicle_movement',
       'Age_band_of_casualty', 'Work_of_casuality', 'Cause_of_accident'
       ]


st.markdown("<h1 style='text-align: center;'>Accident Severity Prediction Application 🚧</h1>", unsafe_allow_html=True)

image = Image.open('doc/theme.png')
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(image, use_column_width=True)   

def main():
       with st.form('prediction_form'):

              st.subheader("Enter the input for following features:")

              time = st.selectbox("Select time: ", options = options_time)
              day_of_week = st.selectbox("Select day of the week: ", options=options_day)
              driver_age = st.selectbox("Select driver's age: ", options=options_age)
              vehicle_relation = st.selectbox("Select vehicle relation: ", options = options_Vehicle_driver_relation)
              driving_experience = st.selectbox("Select driving experience: ", options=options_driver_exp)
              service_year_of_vehicle = st.selectbox("Select service year of vehicle: ", options = options_Service_year_of_vehicle)
              road_surface_type = st.selectbox("Select surface of road: ", options=options_Road_surface_type)
              road_surface_conditions = st.selectbox("Select surface conditions: ", options=options_Road_surface_conditions)
              light_conditions = st.selectbox("Select light conditions: ", options = options_Light_conditions)
              type_of_collision = st.selectbox("Select type of collison: ", options=options_Type_of_collision)
              number_of_vehicles_involved = st.slider("Pickup count of vehicles involved: ", 1, 7, value=0, format="%d")
              number_of_casualties = st.slider("Pickup count of casualties: ", 1, 8, value=0, format="%d")
              vehicle_movement = st.selectbox("Select vehicle movement: ", options=options_Vehicle_movement)
              age_band_of_casualty = st.selectbox("Select casualty's age: ", options=options_Age_band_of_casualty)
              work_of_casuality = st.selectbox("Select work of casuality: ", options = options_Work_of_casuality)
              cause_of_accident = st.selectbox("Select cause of accident: ", options=options_Cause_of_accident)

              submit = st.form_submit_button("Predict")


       if submit:
              time = Time_dict[time]
              day_of_week = le_Day_of_week.transform([day_of_week])
              driver_age = Age_band_of_driver_dict[driver_age]
              vehicle_relation = le_Vehicle_driver_relation.transform([vehicle_relation])
              driving_experience = Driving_experience_dict[driving_experience]
              service_year_of_vehicle = Service_year_of_vehicle_dict[service_year_of_vehicle]
              road_surface_type = le_Road_surface_type.transform([road_surface_type])
              road_surface_conditions = le_Road_surface_conditions.transform([road_surface_conditions])
              light_conditions = Light_conditions_dict[light_conditions]
              type_of_collision = le_Type_of_collision.transform([type_of_collision])
              vehicle_movement = le_Vehicle_movement.transform([vehicle_movement])
              age_band_of_casualty = Age_band_of_casualty_dict[age_band_of_casualty]
              work_of_casuality = le_Work_of_casuality.transform([work_of_casuality])
              cause_of_accident = le_Cause_of_accident.transform([cause_of_accident])

              user_inp = np.array([time, *day_of_week, driver_age, *vehicle_relation, driving_experience,
                            service_year_of_vehicle, *road_surface_type, *road_surface_conditions,
                            light_conditions, *type_of_collision, number_of_vehicles_involved,
                            number_of_casualties, *vehicle_movement, age_band_of_casualty,
                            *work_of_casuality, *cause_of_accident]).reshape(1,-1)

              pred = get_prediction(xgb, user_inp)

              if pred == 'Slight injury':
                     st.write('Thank God! It was a Slight Injury!')
              elif pred == 'Serious Injury':
                     st.write('It seems like Serious Injury!')
              else:
                     st.write('OMG it\'s a Fatal Injury. Hope the driver recovers fast.')
           

if __name__ == '__main__':
       main()