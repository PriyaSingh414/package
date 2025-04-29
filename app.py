import streamlit as st
import joblib


model=joblib.load('placement.pkl')
def main():
    st.title("welcome")
    cgpa=st.slider("Choose your package from slider",min_value=0.0,max_value=10.0,step=0.1)
    st.write("cgpa is ",cgpa)

    if st.button('predict'):
        result=model.predict([[cgpa]])
        st.success(f'your data predict{result}')


if __name__=='__main__':
    main()
