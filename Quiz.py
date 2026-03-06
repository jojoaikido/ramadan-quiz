import streamlit as st

# Seiteneinstellungen
st.set_page_config(page_title="Ramadhan Quiz", page_icon="🌙")

st.title("🌙 Ramadhan & Selbstreform Quiz")
st.write("Teste dein Wissen über den heiligen Monat!")

# Quiz-Daten aus den Folien
if 'score' not in st.session_state:
    st.session_state.score = 0

# Frage 1: Kalender
st.subheader("Frage 1")
st.write("Wann wurde der islamische Kalender eingeführt?")
st.write("اسلامی کیلنڈر کا آغاز کب ہوا؟")
q1 = st.radio("Wähle eine Option:", ["Erste Offenbarung", "Nach der Hijra (Auswanderung)", "Es gibt keinen"], key="q1")

# Frage 2: Monat
st.subheader("Frage 2")
st.write("Der wievielte Monat ist Ramadhan?")
st.write("اسلامی کیلنڈر کے لحاظ سے رمضان کا مہینہ کتنے نمبر پر ہے؟")
q2 = st.radio("Wähle eine Option:", ["8", "9", "11"], key="q2")

# Frage 3: Fidya
st.subheader("Frage 3")
st.write("Wie nennt man die Entrichtung für versäumte Tage?")
st.write("رمضان کے روزہ چھوٹنے کی صورت میں کیا ادا جاتا ہے؟")
q3 = st.radio("Wähle eine Option:", ["Zakat", "Fidya", "Fitrana"], key="q3")

if st.button("Ergebnis prüfen"):
    score = 0
    if q1 == "Nach der Hijra (Auswanderung)": score += 1 [cite: 102, 106]
    if q2 == "9": score += 1 [cite: 110, 113]
    if q3 == "Fidya": score += 1 [cite: 129, 132]
    
    st.success(f"Du hast {score} von 3 Fragen richtig beantwortet!")
    if score == 3:
        st.balloons()