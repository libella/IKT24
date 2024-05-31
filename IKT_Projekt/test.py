
import streamlit as st
import pandas as pd

st.title('Spam-Projekt, IKT-SS24')
st.subheader('Irina Ukhanova')
st.header('Thema', divider='rainbow')
container1 = st.container(border=False)
container1.write("Klassifikation von Spam-Buchungsanfragen auf einem Immobilienportal")
st.header('Datensatz', divider='rainbow')
container2 = st.container(border=False)
container2.write("Ein unternehmensinterner Datensatz, der Spam-Buchungsanfragen enthält. Dieser Datensatz besteht aus folgenden Merkmalen der Buchungsanfragen: Inhalt der Nachricht, E-Mail.")

st.header('Kurzbeschreibung', divider='rainbow')
container3 = st.container(border=False)
container3.write("Das Ziel dieses Projekts ist es, die Sicherheit von Buchungsanfragen auf einem Immobilienportal zu erhöhen, indem anfällige und gefährliche Anfragen automatisch vom System erkannt und blockiert werden. Hierbei sollen ML-Techniken angewendet werden, um legitime Buchungsanfragen von Spam zu unterscheiden. Dies schützt sowohl das Unternehmen als auch die Nutzer vor potenziellen Betrugsversuchen und anderen schädlichen Aktivitäten.")
st.header('Status Quo', divider='rainbow')
st.image('IKT_Projekt/img/SPAMprojekt.png', caption='Flussdiagramm der aktuellen Spam-Überprüfungs-Prozesse' )

st.header('Data Processing ', divider='rainbow')
container4 = st.container(border=False)
container4.write(st.page_link("https://huggingface.co/flair/ner-german-large", label="Name Entity Recognition"))
