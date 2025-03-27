import streamlit as st

st.title("🎈 My new app for DV4S!")
st.write(
    "Vediamo come cazzo funziona! [docs.streamlit.io](https://docs.streamlit.io/)."
)


value = st.slider('Select a value', 0, 100, 30)
st.write('You selected:', value )

button_pressed = st.button('Push me for Sport List')
if button_pressed:
    st.write('Sport List')
