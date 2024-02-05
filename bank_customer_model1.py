import numpy as np
import streamlit as st
import joblib
import pickle

model_path = 'C:/Users/عمر محمد السيف/Desktop/omer/model_svc.pkl'
model = joblib.load(model_path)

def bank_customer(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return 'The person is not churn'
    else:
        return 'The person is churn'
def main():
    st.title('Bank Customer Churn Prediction')

    # Add similar input prompts for other features
    credit_score = st.text_input('Enter your credit score: ')
    
    country = st.selectbox(' Country : ',('France','Germany','Spain'),index=None,
   placeholder="Select your Country..",)
    if country == 'France':
        country = 0
    elif country == 'Germany':
        country = 1
    else:
        country = 2
        
    
    
    gender =  st.selectbox(' Gender  ',('Male','Female'),index=None,
   placeholder="Select your Gender..",)
    if gender == 'Male':
        gender = 0
    
    else:
        gender = 1
    
    age = st.slider('Age', min_value=18.0, max_value=100.0,step=1.0, format="%.1f")
    
    tenure = st.text_input('How long do you stay in the bank by years: ')
    
    balance = st.text_input(' Blance: ')
    
    products_number = st.selectbox(' Products Number: ', (1,2,3,4),index=None,
   placeholder="Select your Products Number..",)
    
    
    credit_card = st.selectbox('do you have credit card: ',('Yes','No'),index=None,
   placeholder="do you have credit card..",)
    if credit_card == 'No':
        credit_card = 0
    
    else:
        credit_card = 1
    
    
    active_member= st.selectbox('are you account is active: ',('Yes','No'),index=None,
   placeholder="are you account is active..",)
    if active_member == 'No':
        active_member = 0
    
    else:
        active_member = 1
    
    estimated_salary = st.text_input(' Salary: ')
    
    Results = ''

    if st.button('Bank Customer Churn'):
        Results = bank_customer([credit_score, country, gender, age, tenure,
        balance, products_number, credit_card, active_member,
        estimated_salary])
    
    st.success(Results)
if __name__ == '__main__':
    main()


