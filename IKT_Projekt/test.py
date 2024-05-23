
import streamlit as st
import pandas as pd

st.title('IKT-SS24, Projekt')
st.header('Thema', divider='rainbow')
st.text('Klassifikation von Spam-Buchungsanfragen auf einem Immobilienportal')
st.header('Datensatz', divider='rainbow')
st.text('in unternehmensinterner Datensatz, der Spam-Buchungsanfragen enthält. Dieser Datensatz besteht aus folgenden Merkmalen der Buchungsanfragen: Inhalt der Nachricht, E-Mail.')

st.header('Kurzbeschreibung', divider='rainbow')
st.text('Das Ziel dieses Projekts ist es, die Sicherheit von Buchungsanfragen auf einem Immobilienportal zu erhöhen, indem anfällige und gefährliche Anfragen automatisch vom System erkannt und blockiert werden. Hierbei sollen ML-Techniken angewendet werden, um legitime Buchungsanfragen von Spam zu unterscheiden. Dies schützt sowohl das Unternehmen als auch die Nutzer vor potenziellen Betrugsversuchen und anderen schädlichen Aktivitäten.')
st.image('SPAMprojekt.png', caption='Flussdiagramm der aktuellen Spam-Überprüfungs-Prozesse' )