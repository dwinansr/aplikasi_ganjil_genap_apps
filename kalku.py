import streamlit as st
import base64
import requests
from streamlit_lottie import st_lottie

# Function to calculate Chemical Oxygen Demand (COD)
def calculate_cod(vb, vc, nfas, vsample):
    cod_value = ((vb - vc) * nfas * 8000) / vsample
    return cod_value
        

# file json format (File path)
lottie_url = "https://lottie.host/763d8378-248d-49ea-be0a-e2f54c16261d/JhnKfnqKfV.json"

# Fungsi untuk memproses lottie url
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Memproses animasi lottie
lottie_json = load_lottie_url(lottie_url)


# Function to determine environmental quality class
def determine_quality_class(cod_value):
    if cod_value >= 0 and cod_value <= 10:
        return "memenuhi Baku Mutu Lingkungan (BML) dalam Kelas 1 berdasarkan PP No.22 Tahun 2021. Kelas 1 merupakan air yang peruntukannya dapat digunakan untuk air baku air minum, dan/atau peruntukan lain yang mempersyaratkan mutu air yang sama dengan kegunaan tersebut."
    elif cod_value > 10 and cod_value <= 25:
        return "memenuhi Baku Mutu Lingkungan (BML) dalam Kelas 2 berdasarkan PP No.22 Tahun 2021. Kelas 2 merupakan air yang peruntukannya dapat digunakan untuk prasarana/sarana rekreasi air, pembudidayaan ikan air tawar, peternakan, air untuk mengairi pertanaman, dan/atau peruntukan mempersyaratkan mutu air yang sama dengan kegunaan tersebut."
    elif cod_value > 25 and cod_value <= 40:
        return "memenuhi Baku Mutu Lingkungan (BML) dalam Kelas 3 berdasarkan PP No.22 Tahun 2021. Kelas 3 merupakan air yang peruntukannya dapat digunakan untuk pembudidayaan ikan air tawar, peternakan, air untuk mengairi tanaman, dan/atau peruntukan lain yang mempersyaratkan mutu air yang sama dengan kegunaan tersebut."
    elif cod_value > 40 and cod_value <= 80:
        return "memenuhi Baku Mutu Lingkungan (BML) dalam Kelas 4 berdasarkan PP No.22 Tahun 2021. Kelas 4 merupakan air yang peruntukannya dapat digunakan untuk mengairi pertanaman dan/atau peruntukan lain yang mempersyaratkan mutu air yang sama dengan kegunaan tersebut."
    else:
        return "tidak memenuhi Baku Mutu Lingkungan (BML) yang telah ditetapkan dalam PP No.22 Tahun 2021"

    
def img_to_base64(image_path):
    """Convert image to base64"""
    with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    
    # Import gambar & konversi ke base64
img_path = "img/icon_aka.png"  
img_base64 = img_to_base64(img_path)
st.sidebar.markdown(
    f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto;">',
    unsafe_allow_html=True,
)


# Streamlit UI
def main():
    # Create a sidebar
    st.sidebar.title('Main Menu')

    # Add a selectbox to the sidebar
    select_box = st.sidebar.selectbox('', 
        ('Pengantar', 'Cara Kerja', 'Kalkulator COD', 'Our Group')
    )

    # Display some content based on the selected option
    if select_box == 'Pengantar':
        st.markdown ('# <div style="text-align: center;"> Chemical Oxygen Demand </div>', unsafe_allow_html=True)
        st.markdown("""
            :red[COD (Chemical Oxygen Demand)] adalah sebuah parameter yang mengukur 
            jumlah oksigen yang dibutuhkan untuk mengoksidasi senyawa organik 
            dalam air secara kimia. Penggunaan K2Cr2O7 (kalium dikromat) sebagai 
            oksidator dalam suasana asam digunakan untuk mengoksidasi materi organik 
            yang ada dalam sampel air. Hasil dari tes COD menunjukkan jumlah senyawa 
            organik yang dapat dioksidasi, dan digunakan untuk menilai tingkat 
            pencemaran air.

            ### Kelebihan
            - Hanya memakan waktu ±3 jam
            - Untuk menganalisis COD antara 50-800 mg/l, tidak dibutuhkan pengenceran 
              sampel.
            - COD mengukur semua bahan organik yang dapat dioksidasi dalam sampel, termasuk yang tidak dapat diurai oleh mikroorganisme.
            - Hasil pengukuran COD cenderung konsisten dan dapat diulang dengan hasil yang hampir sama.

            ### Kekurangan
            - Tidak dapat dibedakan antara zat yang tidak teroksidasi dengan zat-zat 
              yang teroksidasi secara biologis.
            - Metode ini tidak berlaku bagi contoh uji air yang mengandung ion klorida > 2000 mg/l.
            - Kadar klorida > 2000 ppm dapat mengganggu hasil tes COD, tapi dapat 
              dihilangkan dengan penambahan HgSO4.
                    
            ### Rumus Perhitungan
                    
        """)
        st.image ('img/rumus.png', use_column_width=True)


    elif select_box == 'Cara Kerja':
        st.markdown ('# <div style="text-align: center;"> Cara Kerja COD/KOK </div>', unsafe_allow_html=True)

        st.markdown("""
            ### Proses Pengukuran COD/KOK:

            1. **Persiapan Sampel:**
               - Campurkan 2 mL contoh inlet/outlet dengan 2 mL K2Cr2O7 dan 2 mL campuran Ag2SO4 dan H2SO4.
               - Masukkan campuran ke dalam reaktor dan biarkan selama 1 jam.
               - Dinginkan dan pindahkan ke dalam Erlenmeyer.

            2. **Titrasi:**
               - Titrasi dengan larutan FAS* 0,02 N menggunakan indikator feroin.
               - Tambahkan larutan FAS hingga terjadi perubahan warna dari merah kecoklatan, hijau, biru, dan kembali ke merah kecoklatan.

            3. **Proses Standarisasi:**
               - Timbang K2Cr2O7 langsung ditabung Erlenmeyer secara duplo.
               - Tambahkan air sebanyak 25 mL dan 10 mL H2SO4 pekat.
               - Titrasi dengan larutan FAS 0,02 N dengan indikator feroin.

            *FAS = larutan Ferro Ammonium Sulfat

            ### Catatan:
            - Pastikan standarisasi dilakukan dengan cermat untuk hasil yang akurat.
            - Lakukan pengukuran secara berulang untuk meminimalkan kesalahan.
        """)
        st.write ("")
        st.write ("")
        
        col1,col2,col3 = st.columns([1,2,1])

    # Menampilkan animasi lottie
        with col2:
            if lottie_json is not None:
                st_lottie(lottie_json)
            else:
                st.write("Failed to load Lottie animation.")


    elif select_box == 'Kalkulator COD':
        st.markdown ('# <div style="text-align: center;"> Kalkulator COD </div>', unsafe_allow_html=True)

        st.subheader('Masukkan Nilai Parameter:')

        vb = st.number_input('Volume larutan FAS untuk Blanko (mL)', min_value=0.0)
        vc = st.number_input('Volume larutan FAS untuk Contoh Uji (mL)', min_value=0.0)
        nfas = st.number_input('Normalitas FAS', min_value=0.0, format= '%.4f')
        vsample = st.number_input('Volume Contoh Uji (mL)', min_value=0.0)

        if st.button('Hitung COD'):
            cod_result = calculate_cod(vb, vc, nfas, vsample)
            st.success(f'Nilai Chemical Oxygen Demand sebesar {cod_result:.2f} mg O2/L')

            # Determine environmental quality class
            quality_class = determine_quality_class(cod_result)
            st.info(f'Hasil dari Kadar COD tersebut {quality_class}')
            st.image('img/tabel.png', use_column_width=True)

    if select_box == 'Our Group':
        st.markdown ('## <div style="text-align: center;"> Kelompok  9 </div>', unsafe_allow_html=True)

        # Team Members
        team_data = [
            {"name": "Dwi Nanda Sari","image_url": "img/Wi.jpg"},
            {"name": "Elsa Anggraeni", "image_url": "img/eca.jpg"},
            {"name": "M. Ihsan Taqiyuddin ", "image_url": "img/cicak2.JPG"},
            {"name": "Rasikhah Maharani Liliana Bakti", "image_url": "img/rasi.jpg"},
            {"name": "Reyhan Riselvi", "image_url": "img/ray.jpg"}
        ]

        # Display Team Members
        col1, col2, col3, col4, col5 = st.columns(5)

        for i, member in enumerate(team_data):
            with locals()[f"col{i % 5 + 1}"]:
                st.image(member["image_url"], use_column_width='auto', output_format='png', caption=f"{member['name']}")


        st.header(" ", divider="gray")
        st.caption('<div style="text-align: center; transform: skewX(-20deg);">Powered by Politeknik AKA BOGOR</div>', unsafe_allow_html=True)


if __name__ == '__main__':
    main()



