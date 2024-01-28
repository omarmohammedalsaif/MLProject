import numpy as np
#import pickle
import streamlit as st
#
import sklearn 
# -*- coding: utf-8 -*-

from skops.io import dump, load
loaded = load("C:/Users/عمر محمد السيف/Downloads/my-model.skops", trusted=True) 

#loaded = pickle.load(open('C:/Users/عمر محمد السيف/Desktop/trained_model.sav',"rb"))


#funcation

def diabetes(input_data):
    
    
    #input_data =(5 , 166 , 72 , 19, 175,25.8,0.587,51)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded.predict(input_data_reshaped)
    return (prediction)
    
    if (prediction[0]== 0):
        return ('The person is not diabetic')
    else:
        return ('The person is  diabetic')
    
def main():
    
   # the name of the websit
    st.title('Diabetes Prediction Web App')
    Age= st.text_input('Enter your Age: ')
    Gender= st.text_input('Enter the Gender: ')
    Polyuria = st.text_input('Enter yes or no : ')
    Polydipsia = st.text_input('Enter',placeholder='Enter yes or no : ')
    sudden_weight_loss = st.text_input('Enter Yes or no: ')
    weakness = st.text_input('Enter yes Or no: ')
    Polyphagia = st.text_input('Enter yes or No: ')
    Genital_thrush = st.text_input('ENTER yes or no: ')
    visual_blurring = st.text_input('Enter YES or no: ')
    Itching= st.text_input('Enter yes OR no: ')
    Irritability = st.text_input('Enter yes or NO: ')
    delayed_healing = st.text_input('ENter yes or no : ')
    partial_paresis = st.text_input('Enter yes or no:: ')
    muscle_stiffness = st.text_input('Enter yes or no: ')
    Alopecia = st.text_input('Enter yes or no:- ')
    Obesity	 = st.text_input('Enter yes or no-: ')
   



    dignosis = ''
    # creating a button for perdiction
    if st.button('Diabetes test Result'):
        dignosis = diabetes([Age, Gender, Polyuria, Polydipsia, sudden_weight_loss,
       weakness, Polyphagia, Genital_thrush, visual_blurring,
       Itching, Irritability, delayed_healing, partial_paresis,
       muscle_stiffness, Alopecia, Obesity])


    st.success(dignosis)

if __name__ == '__main__':
    main()


