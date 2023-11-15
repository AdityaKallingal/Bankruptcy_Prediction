import numpy as np
import pickle
import streamlit as st




# Set the background image URL
background_image_url = "https://images.unsplash.com/photo-1527874594978-ee4f8a05b4c1?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Create HTML and CSS to set the background image
background_html = f"""
    <style>
        body {{
            background-image: url('{background_image_url}');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
    </style>
"""

# Display the background image using markdown
st.markdown(background_html, unsafe_allow_html=True)











# loading the saved model
loaded_model = pickle.load(open("D:\ML_bankruptcy project\model.pkl", 'rb'))


# creating a function for Prediction

def bank_prediction_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Not Bankrupt'
    else:
      return 'Bankrupt'
  
    
  
def main():
    
    
    # giving a title
    st.title('Bankruptcy Prediction Web App')
    
    
    # getting the input data from the user
    
    
    roa_c = st.text_input("ROA(C) before interest and depreciation before interest", "0.50000")
    roa_a = st.text_input("ROA(A) before interest and % after tax", "0.50000")
    roa_b = st.text_input("ROA(B) before interest and depreciation after tax", "0.50000")
    eps_last_four_seasons = st.text_input("Persistent EPS in the Last Four Seasons", "0.50000")
    net_profit_before_tax = st.text_input("Per Share Net profit before tax (Yuan ¥)", "0.50000")
    debt_ratio = st.text_input("Debt ratio %", "0.50000")
    net_worth_assets = st.text_input("Net worth/Assets", "0.50000")
    net_profit_to_paid_in_capital = st.text_input("Net profit before tax/Paid-in capital", "0.50000")
    retained_earnings_to_total_assets = st.text_input("Retained Earnings to Total Assets", "0.50000")
    net_income_to_total_assets = st.text_input("Net Income to Total Assets", "0.50000")
    
    
    # code for Prediction
    bankruptcy = ''
    
    # creating a button for Prediction
    
    if st.button('Bankruptcy predicton Result'):
         bankruptcy = bank_prediction_prediction([roa_c,roa_a,roa_b ,eps_last_four_seasons,net_profit_before_tax,debt_ratio, net_worth_assets, net_profit_to_paid_in_capital,retained_earnings_to_total_assets,net_income_to_total_assets ])
        
        
    st.success(bankruptcy)
    
    
    
    
    
if __name__ == '__main__':
    main()