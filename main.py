import streamlit as st
import pandas as pd
import math

st.title("Výpočet čisté mzdy")
col1, col2 = st.columns(2)
hruba_mzda = col1.number_input("Hrubá měsíční mzda", min_value=18900, value=40000)
pocet_deti = col2.number_input("Počet Dětí", min_value=0, value=0, max_value=10)
zamestnanec_zdravotni = math.ceil((4.5 / 100) * hruba_mzda)
zamestnanec_socialni = math.ceil((7.1 / 100) * hruba_mzda)
dan = math.ceil((15 / 100) * hruba_mzda)
dan_sleva = 2570
zamestnavatel_zdravotni = math.ceil((9 /100) * hruba_mzda)
zamestnavatel_socialni = math.ceil((24.8 /100) * hruba_mzda)
deti_sleva=0
deti1= 1267
deti2= 1860
deti3= 2320
if (pocet_deti == 1):
    deti_sleva = deti1
elif (pocet_deti ==2):
    deti_sleva = deti1 + deti2
elif (pocet_deti >=3):
    deti_sleva = deti1 + deti2 + ((pocet_deti - 2) * deti3)
st.write("## Čistá mzda")
st.write("### Zaměstnanec")
cista_mzda =  hruba_mzda - zamestnanec_socialni - zamestnanec_zdravotni -  dan + dan_sleva + deti_sleva


col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Čistá mzda", value=f"{cista_mzda} Kč")
col2.metric(label="Zaměstnanec sociální", value=f"{zamestnanec_socialni} Kč")
col3.metric(label="Zaměstnanec zdravotní", value=f"{zamestnanec_zdravotni} Kč")
col4.metric(label="Daň", value=f"{dan} Kč")

st.write("### Zaměstnavatel")
col1, col2 = st.columns(2)
col1.metric(label="Zaměstnavatel sociální", value=f"{zamestnavatel_socialni} Kč")
col2.metric(label="Zaměstnavatel zdravotní", value=f"{zamestnavatel_zdravotni} Kč")

data = {
    "Popis": 
    [
        "Základ daně:",
        "Pojistné zaměstnavatel:",
        "   - z toho sociální pojištění",
        "   - z toho zdravotní pojištění",
        "Pojistné:",
        "   - z toho sociální pojištění",
        "   - z toho zdravotní pojištění",
        "Daň celkem:",
        "   Daň:",
        "   Daňova sleva:",
        "   Daňové zvýhodnění na děti:"


    ],
    "Částka":
    [
        hruba_mzda,
        -(zamestnavatel_zdravotni + zamestnavatel_socialni),
        -zamestnavatel_socialni,
        -zamestnavatel_zdravotni,
        -(zamestnanec_zdravotni+zamestnanec_socialni),
        -zamestnanec_socialni,
        -zamestnanec_zdravotni,
        -(dan-dan_sleva-deti_sleva),
        -dan,
        dan_sleva,
        deti_sleva
    ]
}

df = pd.DataFrame(data)

def highlight_alternate_rows(s):
    return ['background-color: rgb(243, 243, 243)' if i % 2 == 0 else '' for i in range(len(s))]

styled_df = df.style.apply(highlight_alternate_rows, axis=0)

html_table = styled_df.to_html(index=False, escape=False)

custom_css = """
<style>
    table {
        border-collapse: collapse;
        width: 100%;
    }
    th, td {
        border: none; 
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
    }
    tr {
    border: none; 
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(html_table, unsafe_allow_html=True)