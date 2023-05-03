import streamlit as st

st.header(":green[Aplikasi Kalkulator Penjumlahan]")
st.write("Silahkan input angka numerik yang akan dihitung!:memo::sparkling_heart:")

number1 = st.number_input("Masukkan bilangan pertama")
st.write(f"bilangan pertama adalah {number1}")

number2 = st.number_input("Masukkan bilangan kedua")
st.write(f"Bilangan kedua adalah {number2}")

if st.button("Hitung"):
	hasil = number1+number2
	st.success(f"Hasil penjumlahan dari {number1} + {number2} = {hasil}")
	st.balloons ()
else:
	st.write('Silahkan klik tombol "Hitung" jika kamu ingin melakukan kalkulasi')