import streamlit as st
import joblib


model=joblib.load('placement.pkl')
def main():
    st.title("welcome")
    cgpa=st.number_input("enter number")

    if st.button('predict'):
        result=model.predict([[cgpa]])
        st.success(f'your data predict{result}')


if __name__=='__main__':
    main()