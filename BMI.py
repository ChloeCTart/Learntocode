import streamlit as st

st.header('BMI CALCULATOR')
col1, col2=st.columns(2,gap='large')

with col1:
    h=st.number_input('Enter your height (cm)', min_value=1, max_value=350)
    w=st.number_input('Enter your weight (kg)', min_value=1, max_value=500)
    bmi=round(w/((h/100)**2),2)
    if st.button('CALCULATE',type='primary'):
        st.write('BMI:',bmi)
        if bmi<18.5:
            st.write(':blue[You are underweight.]')
        elif bmi>=18.5 and bmi<=25:
            st.write(':green[You are healthy.]')
        else:
            st.write(':red[You are overweight.]')

with col2:
    st.image("https://benhvienvanhanh.vn/wp-content/uploads/2022/01/20190515_023832_291922_chi-so-BMI-gay-beo.max-1800x1800-1.jpg",
             caption='Take a look for reference.')
    
    