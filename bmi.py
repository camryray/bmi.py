import streamlit as st

def BMI(w, h):
    return w/(h*h)
#w = float(input('請輸入體重(KG)?'))
w = float(st.number_input('請輸入體重(KG)？'))
h = float(st.number_input('請輸入身高(M)？'))
comfirm_input = st.button('輸入確認')
if comfirm_input:
   bmi = BMI(w, h)
   # print('BMI為', bmi)
   st.write('BMI為', bmi)
   if (bmi < 18):
       st.write('體重過輕')
   elif (bmi < 24):
       st.write('體重正常')
   elif (bmi < 27):
       st.write('體重過重')
   else:
       st.write('體重肥胖')
