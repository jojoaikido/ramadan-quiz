import streamlit as st

# Seiteneinstellungen
st.set_page_config(page_title="Ramadhan Quiz", page_icon="🌙")

st.title("🌙 Ramadhan & Selbstreform Quiz")
st.write("Teste dein Wissen über den heiligen Monat!")

# Quiz-Daten und Logik
# Wir nutzen session_state, damit die App sich die Eingaben merkt
if 'score' not in st.session_state:
    st.session_state.score = 0

# Frage 1: Kalender [cite: 99, 100]
st.subheader("Frage 1")
st.write("Wann wurde der islamische Kalender eingeführt?")
st.write("اسلامی کیلنڈر کا آغاز کب ہوا؟")
q1 = st.radio("Wähle eine Option:", ["Erste Offenbarung", "Nach der Hijra (Auswanderung)", "Es gibt keinen"], key="q1")

# Frage 2: Monat [cite: 108, 109]
st.subheader("Frage 2")
st.write("Der wievielte Monat ist Ramadhan?")
st.write("اسلامی کیلنڈر کے لحاظ سے رمضان کا مہینہ کتنے نمبر پر ہے؟")
q2 = st.radio("Wähle eine Option:", ["8", "9", "11"], key="q2")

# Frage 3: Fidya [cite: 126, 127]
st.subheader("Frage 3")
st.write("Wie nennt man die Entrichtung für versäumte Tage?")
st.write("رمضان کے روزہ چھوٹنے کی صورت میں کیا ادا جاتا ہے؟")
q3 = st.radio("Wähle eine Option:", ["Zakat", "Fidya", "Fitrana"], key="q3")

# Auswertung
if st.button("Ergebnis prüfen"):
    aktueller_score = 0
    # Überprüfung der Antworten basierend auf den Folien:
    if q1 == "Nach der Hijra (Auswanderung)": # 
        aktueller_score += 1
    if q2 == "9": # 
        aktueller_score += 1
    if q3 == "Fidya": # 
        aktueller_score += 1
    
    st.success(f"Du hast {aktueller_score} von 3 Fragen richtig beantwortet!")
    
    if aktueller_score == 3:
        st.balloons()
        st.write("✨ MashAllah! Alles richtig.")
