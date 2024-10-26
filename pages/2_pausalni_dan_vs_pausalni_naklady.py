import streamlit as st
import math

st.set_page_config(layout="wide")
st.title("Výpočet Daně pro IT OSVČ")
col1 = st.columns(1)[0]
rocni_prijem = col1.number_input("Roční Příjmy", value=1500000,max_value=2000000)
dan_sleva = 30840
dan_sazba = 0.15
pausal_naklady = math.ceil(rocni_prijem * 0.6)
sazba_socialni_pojisteni = 0.292  
sazba_zdravotni_pojisteni = 0.135  
pausal_zaklad = math.ceil(rocni_prijem - pausal_naklady)
pausal_dan = math.ceil((pausal_zaklad * dan_sazba) - dan_sleva)
pausal_zdravotni = math.ceil((pausal_zaklad * 0.5) * sazba_zdravotni_pojisteni)
if pausal_zdravotni < 35616:
    pausal_zdravotni = 35616
pausal_socialni = math.ceil((pausal_zaklad * 0.5) * sazba_socialni_pojisteni)
cisty_prijem = rocni_prijem - pausal_dan - pausal_socialni - pausal_zdravotni

pasmo = {
    "pasmo_1": {"dan": 100, "socialni": 4430, "zdravotni":2968}, 
    "pasmo_2": {"dan": 4963, "socialni": 8191, "zdravotni":3591}
}

selected_pasmo = pasmo["pasmo_1"] if rocni_prijem <= 1500000 else pasmo["pasmo_2"]

pd_zdravotni = selected_pasmo["zdravotni"]
pd_socialni = selected_pasmo["socialni"]
pd_dan = selected_pasmo["dan"]
pd_celkem = (pd_dan * 12) + (pd_socialni * 12) + (pd_zdravotni * 12)



st.write("## Paušální náklady čistá mzda")
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Roční Příjmy", value=f"{rocni_prijem:,}")
col2.metric(value=f"{pausal_naklady:,}", label="Paušální náklady")
col3.metric(value=f"{pausal_dan + pausal_zdravotni + pausal_socialni:,}", label="Daň a odvody celkem")
col4.metric(label="Čistý Příjem", value=f"{cisty_prijem:,}")
col1.metric(label="Sociální pojištění", value=f"{pausal_socialni:,}")
col2.metric(label="Zdravotní pojištení", value=f"{pausal_zdravotni:,}")
col3.metric(label="Daň", value=f"{pausal_dan:,}")
col4.metric(label="Empty", value=None, label_visibility="hidden")
col1.metric(label="Sociální měsíčně", value=f"{pausal_socialni/12:,.2f}")
col2.metric(label="Zdravotní měsíčně", value=f"{pausal_zdravotni/12:,.2f}")
col3.metric(label="Dan mesíčně", value=f"{pausal_dan/12:,.2f}")
col4.metric(label="Čisty měsíční příjem", value=f"{(cisty_prijem) /12:,.2f}")



st.write("## Paušální daň čistá mzda")
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Roční Příjmy", value=f"{rocni_prijem:,}")
col2.metric("Empty", value=None, label_visibility="hidden")
col3.metric(label="Daň a odvody celkem",value=f"{pd_celkem:,}")
col4.metric(label="Čistý Příjem", value=f"{rocni_prijem - pd_celkem:,}")
col1.metric(label="Sociální pojištění", value=f"{pd_socialni * 12:,}")
col2.metric(label="Zdravotní pojištení", value=f"{pd_zdravotni * 12:,}")
col3.metric(label="Daň", value=f"{pd_dan * 12:,}")
col4.metric(label="Empty", value=None, label_visibility="hidden")
col1.metric(label="Sociální měsíčně", value=f"{pd_socialni:,}")
col2.metric(label="Zdravotní měsíčně", value=f"{pd_zdravotni:,}")
col3.metric(label="Dan měsíčně", value=f"{pd_dan:,}")
col4.metric(label="Čisty měsíční příjem", value=f"{(rocni_prijem-pd_celkem)/12:,.2f}")
