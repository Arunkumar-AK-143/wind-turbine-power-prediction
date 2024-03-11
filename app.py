import streamlit as st

import pickle
import numpy as np
model=pickle.load(open('Pickle_lasso_wind.pkl','rb'))


def predict_ActivePower(WindDirection,month,WindSpeed):
    input=np.array([[WindDirection,month,WindSpeed]]).astype(np.float64)
    pred=model.predict(input)
    return np.float64(pred)

def main():
    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">wind turbine Status Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    
    WindDirection=st.slider('Enter Wind Direction Value',0.0,500.0)
    month=st.slider('Enter month Value',0.0,12.0)
    WindSpeed=st.slider('Enter WindSpeed(m/s)Value',0.0,20.0)
    
   
    

    if st.button("Predict"):
        output=predict_ActivePower(WindDirection,month,WindSpeed)
        st.title('The prediction of wind turbine active power is {}'.format(output))

    

if __name__=='__main__':
    main()