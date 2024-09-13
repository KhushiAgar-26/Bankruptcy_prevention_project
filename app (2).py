
#pip install streamlit

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open("E:\\project bankruptcy\\finalized_model.sav",'rb'))

#creating a function for prediction
def bankrupt_prediction(input_data):
    prediction=loaded_model.predict([input_data])
    print(prediction)
    if (prediction[0]==0):
      return 'Bankrupt'
    else:
      return 'Not Bankrupt'

def main():
    
    #giving a title
    st.title('Bankrupt prediction Web App')
    
    #getting the input data from the user
    
    industrial_risk=st.text_input('industrial risk value')
    management_risk=st.text_input('management risk value')
    financial_flexibility=st.text_input('financial_flexibility value')
    credibility=st.text_input('credibility value')
    competitiveness=st.text_input('competitiveness value')
    operating_risk=st.text_input('operating risk value')
    
    #code for prediction
    bankrupt=''
    
    #creating a buttom for prediction
    if st.button('Bankrupt Test Result'):
        bankrupt=bankrupt_prediction([industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk])
        
    st.success(bankrupt)
    

if __name__ == '__main__':
    main()








































































































