import streamlit as st
import pickle
import numpy as np


# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df_new.pkl','rb'))

st.title("Placement prediction of an MBA student")

# gender
gender = st.selectbox('Gender',['Male','Female'])

# sec_board
sec_board = st.selectbox('Secondary Examination Board',df['10th_board'].unique())

# sec_percent
sec_percent = st.number_input('Secondary Examination Percentage')

# h_sec_board
h_sec_board = st.selectbox('Higher Secondary Examination Board',df['12th_board'].unique())

# h_sec_subject
h_sec_subject = st.selectbox('Higher Secondary Stream',df['12th_subject'].unique())

# h_sec_percent
h_sec_percent = st.number_input('Higher Secondary Examination Percentage')

# degree_field
degree_field = st.selectbox('Field of Bachelor Degree',df['degree_field'].unique())

# degree_percent
degree_percent = st.number_input('Bachelor Degree Examination Percentage')

# work_exp
work_exp = st.selectbox('Have any work experience?',df['work_exp'].unique())

# etest_percent
etest_percent = st.number_input('Placement Eligibility Examination Percentage')

# mba_field
mba_field = st.selectbox('Field of MBA',df['mba_specialisation'].unique())

# mba_percent
mba_percent = st.number_input('MBA Examination Percentage')


if st.button('Predict'):
    # query
    if gender == 'Male':
        gender = 'M'
    else:
        gender = 'F'

    query = np.array([gender,sec_board,sec_percent,h_sec_board,h_sec_subject,h_sec_percent,degree_field,degree_percent,work_exp,etest_percent,mba_field,mba_percent])

    query = query.reshape(1,12)
    placement = pipe.predict(query)[0]

    if sec_percent <= 100 and h_sec_percent <= 100 and degree_percent <= 100 and etest_percent <= 100 and mba_percent <= 100:
        if gender == 'M':
            if sec_percent < 30 or h_sec_percent < 30 or degree_percent < 30 or etest_percent < 30 or mba_percent < 30:
                st.title('He is not eligible for placement as he got less than 30% marks in one of the Examination')
            else:
                if placement == 'Placed':
                    st.title('He will get placement')
                else:
                    st.title('He will not get placement')
        else:
            if sec_percent < 30 or h_sec_percent < 30 or degree_percent < 30 or etest_percent < 30 or mba_percent < 30:
                st.title('She is not eligible for placement as she got less than 30% marks in one of the Examination')
            else:
                if placement == 'Placed':
                    st.title('She will get placement')
                else:
                    st.title('She will not get placement')
    else:
        st.title('Examination percentage can not be greater than 100%')