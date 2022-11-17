import streamlit as st
with st.sidebar:
  st.title("¡Bienvenido a tu app de Salud Mental!")
  st.image("https://www.uam.es/uam/media/imgl/1606893115743/2022-03-07-cabello-img.jpg")
  st.write("La salud mental tiene un impacto directo en nuestra forma de pensar, sentir y actuar. Determina cómo respondemos ante el estrés, cómo nos relacionamos con otras personas y cómo tomamos decisiones. Es por esto tan importante cuidar de lla como cuidamos de nuestro cuerpo físico. 😃")

st.header ("*¡Infórmate más!*")
st.write("Haz click en cada una de las cajas que se muestran a continuación")
Ansiedad = st.checkbox('Ansiedad')

if Ansiedad:
    st.write('La ansiedad puede ser normal en situaciones estresantes, cómo hablar en público o realizar una prueba. La ansiedad es solo un indicador de una enfermedad subyacente cuando los sentimientos se vuelven excesivos en todo momento e interfieren con la vida cotidiana.')
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnWzwMwIViwoH_SORLvxn_ISqQ2rgT3g7EQLTGujuUYQ&s")
    st.write("Deslice la barra según sus emociones")
    miedo=st.select_slider("1. ¿Ha sentido miedo ultimamente?",
    options=["si", "en ocasiones","normalmente no", "no"])
    st.write("Usted", miedo, "ha sentido miedo.")
    angustia=st.select_slider("2. ¿Se ha sentido angustiado?", 
    options=["si","a veces","rara vez","no"])
    st.write("Usted",angustia,"se ha sentido angustiado.")
    concentracion=st.select_slider("3. ¿Presenta problemas para concentrarse?",
    options=["si","en ocasiones","normalmenteno","no"])
    st.write("Usted",concentracion,"presenta problemas para concentrarse.")
    memoria=st.select_slider("4. Dificultad para recordar cosas", 
    options=["Sin dificultad","Normal","Me cuesta mucho"])
    st.write(memoria,"de recordar cosas.")
    pensamientos=st.select_slider("5. ¿Ha tenido pensamientos o imágenes catastróficas?", 
    options=["si","seguido","rara vez","nunca"])
    st.write("Usted",pensamientos,"ha tenido imágenes catastróficas.")
    st.write("*¡Si quieres saber más, haz click en el siguiente enlace!*")
    st.write("https://youtu.be/34ZVrmJxEUo")

Depresión=st.checkbox("Depresión")

if Depresión:
  st.write("La depresión es un trastorno mental caracterizado fundamentalmente por un bajo estado de ánimo y sentimientos de tristeza, asociados a alteraciones del comportamiento, del grado de actividad y del pensamiento.")
  st.write("Deslice la barra según sus emociones.")
  desanimado=st.select_slider("1. ¿Últimamente se ha sentido desanimado, deprimido ó sin esperanza?", 
  options=["si","en ocasiones","no"])
  st.write("Usted",desanimado,"se siente desanimado.")
  placer=st.select_slider("2. ¿Siente poco interés o placer en hacer algunas cosas?", 
  options=["solo en algunas ocasiones","no muy seguido"])
  st.write("Usted",placer,"se siente con poco interés en realizar ciertas actividades.")
  dormir=st.select_slider("3. ¿Duerme demasiado, o incluso tiene problemas para dormir?", 
  options=["Prefiero dormir","Me cuesta mucho trabajo conciliar el sueño"])
  st.write(dormir,".")
  pensamientos=st.select_slider("4. ¿Ha pensado en la muerte?", 
  options=["seguido","en ocasiones","nunca"])
  st.write("Usted",pensamientos,"piensa en la muerte.")
  amor=st.select_slider("5. Falta de amor propio, aprecio hacia amigos o familiares", 
  options=["si","casi no","no"])
  st.write("Usted",amor,"siente falta de amor hacia usted mismo o terceros.")
  st.write("*¡Si quieres saber más, haz click en el siguiente enlace!*")
  st.write("https://youtu.be/vJHYZL-KADg")

Estrés=st.checkbox("Estrés")

if Estrés:
  st.write("El estrés es la respuesta física o mental a una causa externa, como tener muchas tareas o padecer una enfermedad. Un estresor o factor estresante puede ser algo que ocurre una sola vez o a corto plazo, o puede suceder repetidamente durante mucho tiempo.")
  st.write("Deslice la barra según sus emociones")
  ahogo=st.select_slider("1. ¿Ha sentido sensación de ahogo?",
  options=["muy seguido","en ocasiones","nunca"])
  st.write("Usted",ahogo,"presenta sensación de ahogo.")
  comer=st.select_slider("2. ¿Siente mayor necesidad de comer?",
  options=["muy seguido","seguido","solo en ocasiones","casi nunca","nunca"])
  st.write(comer,"siente necesidad de comer.")
  temblores=st.select_slider("3. ¿Presenta temblores o TICs?",
  options=["muy frecuentemente","rara vez","casi nunca"])
  st.write("Usted",temblores,"presenta temblores/TICs.")
  calma=st.select_slider("4. ¿Presenta dificultad para mantener la calma en situación de problemas?",
  options=["me cuesta trabajo","con facilidad"])
  st.write(calma,"mantener la calma.")
  dolores=st.select_slider("5. ¿Constantemente se presentan dolores de cabeza o abdominales?", 
  options=["muy seguido","en ocasiones","rara vez","casi nunca"])
  st.write(dolores,"presenta dolores físicos")
  st.write("*¡Si quieres saber más, haz click en el siguiente enlace!*")
  st.write("https://youtu.be/r0mQj2Y_sqI")


SaludMental=st.radio("¿Alguna vez has recibido algún tratamiento psicológico?", ["SI", "NO"])
if SaludMental== "SI":
  st.write("En las sesiones de terapia psicológica, se puede trabajar el desarrollo de habilidades y estrategias que nos ayuden a reducir o controlar los eventos estresantes o los cambios vitales. Además, la terapia resulta sumamente útil para identificar nuevos objetivos y desarrollar un plan para lograrlos. La Universidad Autónoma de Chihuahua a través del DAIE cuenta con un equipo profesional de psicólogos que brindan atención a las y los estudiantes universitarios de manera permanente y gratuita. Para agendar una cita puedes comunicarte al teléfono (614) 4391520 en la extensión 8011.")
if SaludMental== "NO":
  st.write("Si conoces a alguien que requiera ayuda con su salud mental comuncarse a (614) 4391520 en la extensión 8011")
col1,col2,col3=st.columns( [1,2,3] )

st.header ("*¿Sabías que... condiciones mentales cómo la depresión incrementan el riesgo de padecer enfermedades físicas como diabetes?*")
