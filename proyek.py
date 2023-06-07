import streamlit as st

# Judul halaman
st.title("Aplikasi Web Sederhana")

# Teks
st.header("Ini adalah header")
st.subheader("Ini adalah subheader")
st.text("Ini adalah teks biasa")

# Gambar
st.image("gambar.jpg", caption="Ini adalah gambar")

# Tombol
if st.button("Klik di sini"):
    st.write("Tombol telah diklik!")

# Input teks
nama = st.text_input("Masukkan nama Anda", "John Doe")
st.write("Halo, ", nama, "!")

# Pilihan
options = ["Pilihan 1", "Pilihan 2", "Pilihan 3"]
pilihan = st.selectbox("Pilih opsi", options)
st.write("Anda memilih: ", pilihan)

# Slider
age = st.slider("Pilih usia Anda", 0, 100, 25)
st.write("Usia Anda: ", age)

# Tampilan data
data = {"Nama": ["John", "Jane", "Bob"], "Usia": [25, 30, 35]}
df = pd.DataFrame(data)
st.write(df)
