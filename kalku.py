import streamlit as st

# Function to calculate Chemical Oxygen Demand (COD)
def calculate_cod(vb, vc, nfas, vsample):
    cod_value = ((vb - vc) * nfas * 8000) / vsample
    return cod_value

# Function to determine environmental quality class
def determine_quality_class(cod_value):
    if cod_value >= 0 and cod_value <= 10:
        return "termasuk Kelas 1"
    elif cod_value > 10 and cod_value <= 25:
        return "termasuk Kelas 2"
    elif cod_value > 25 and cod_value <= 40:
        return "termasuk Kelas 3"
    elif cod_value > 40 and cod_value <= 80:
        return "termasuk Kelas 4"
    else:
        return "tidak termasuk dalam kelas baku mutu yang ditetapkan"

# Streamlit UI
def main():
    st.title('Kalkulator Chemical Oxygen Demand (COD)')

    st.write('Masukkan Nilai Parameter:')

    vb = st.number_input('Volume larutan FAS untuk Blanko (mL)', min_value=0.0)
    vc = st.number_input('Volume larutan FAS untuk Contoh Uji (mL)', min_value=0.0)
    nfas = st.number_input('Number of equivalent for Sample (FAS)', min_value=0.0)
    vsample = st.number_input('Volume Contoh Uji (mL)', min_value=0.0)

    if st.button('Calculate COD'):
        cod_result = calculate_cod(vb, vc, nfas, vsample)
        st.write(f'Nilai Chemical Oxygen Demand sebesar {cod_result:.2f} mg O2/L')

        # Determine environmental quality class
        quality_class = determine_quality_class(cod_result)
        st.write(f'Hasil dari Kadar COD {quality_class} berdasarkan Baku Mutu Lingkungan (BML)')

if __name__ == '__main__':
    main()
