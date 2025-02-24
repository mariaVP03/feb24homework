import pickle
import streamlit as st

# Load the models
with open('classifier.pkl', 'rb') as rf_file:
    rf_model = pickle.load(rf_file)

with open('svm.pkl', 'rb') as svm_file:
    svm_model = pickle.load(svm_file)

with open('knn.pkl', 'rb') as knn_file:
    knn_model = pickle.load(knn_file)

# Function to get the selected model
def get_model(model_name):
    if model_name == "Random Forest":
        return rf_model
    elif model_name == "SVM":
        return svm_model
    elif model_name == "KNN":
        return knn_model

@st.cache_data()
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History, model_name):   
    # Pre-processing user input    
    Gender = 0 if Gender == "Male" else 1
    Married = 0 if Married == "Unmarried" else 1
    Credit_History = 0 if Credit_History == "Unclear Debts" else 1  
    LoanAmount = LoanAmount / 1000  # Normalize loan amount
    
    # Get selected model
    model = get_model(model_name)
    
    # Making predictions 
    pred = model.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
    
    return 'Approved' if pred == 1 else 'Rejected'

# Main function
def main():       
    html_temp = """ 
    <div style="background-color:yellow;padding:13px"> 
    <h1 style="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
      
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # User inputs
    Gender = st.selectbox('Gender', ("Male", "Female"))
    Married = st.selectbox('Marital Status', ("Unmarried", "Married")) 
    ApplicantIncome = st.number_input("Applicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History', ("Unclear Debts", "No Unclear Debts"))

    # Model selection
    model_name = st.selectbox('Choose Model', ("Random Forest", "SVM", "KNN"))

    result = ""

    # Predict button
    if st.button("Predict"): 
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History, model_name) 
        st.success(f'Your loan is {result}')
        print(LoanAmount)

if __name__ == '_main_': 
    main()
