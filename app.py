import streamlit as st

st.header('Define Number Type Apps', divider='blue')
st.write('Ini adalah aplikasi untuk menentukan bilangan ganjil dan genap serta hasil perkaliannya.')

number = st.number_input("Masukkan sebuah bilangan")

if number % 2 == 0:
    st.write(f"Bilangan {number} adalah bilangan genap.")
    st.write(f"Hasil perkalian {number} dengan 2 adalah {number * 2}.")
else:
    st.write(f"Bilangan {number} adalah bilangan ganjil.")
    st.write(f"Hasil perkalian {number} dengan 3 adalah {number * 3}.")






