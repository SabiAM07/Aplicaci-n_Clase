import streamlit as st
col1,col2=st.columns( [1,2] )
col1.title ("¡Bienvenido a tu app de Salud Mental!")
col2.image ("https://www.uam.es/uam/media/imgl/1606893115743/2022-03-07-cabello-img.jpg", width=400)

st.write ("La salud mental tiene un impacto directo en nuestra forma de pensar, sentir y actuar. Determina cómo respondemos ante el estrés, cómo nos relacionamos con otras personas y cómo tomamos decisiones. Es por esto tan importante cuidar de lla como cuidamos de nuestro cuerpo físico. 😃")

st.header ("*¡Infórmate acerca de tu Salud Mental!*")

Ansiedad = st.checkbox('Ansiedad')

if Ansiedad:
    st.write('La ansiedad puede ser normal en situaciones estresantes, cómo hablar en público o realizar una prueba. La ansiedad es solo un indicador de una enfermedad subyacente cuando los sentimientos se vuelven excesivos en todo momento e interfieren con la vida cotidiana.')
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnWzwMwIViwoH_SORLvxn_ISqQ2rgT3g7EQLTGujuUYQ&s")
    st.write("Desliza la barra según tus emociones (dónde cero representa lo mínimo y diez lo máximo)")
    miedo=st.slider("¿Has sentido miedo ultimamente?", 0, 5, 10)
    angustia=st.slider("¿Has sentido angustia?", 0, 5, 10)
    concentracion=st.slider("¿Tienes problemas para concentrarte?", 0, 5, 10)
    memoria=st.slider("Dificultad para recordar cosas", 0, 5, 10)
    pensamientos=st.slider("¿Has tenido pensamientos o imagenes catastróficas?", 0, 5, 10)
    st.write("*¡Si quieres saber más, haz click en el siguiente enlace!*")
    st.write("https://youtu.be/34ZVrmJxEUo")

Depresión=st.checkbox("Depresión")

if Depresión:
  st.write("La depresión es un trastorno mental caracterizado fundamentalmente por un bajo estado de ánimo y sentimientos de tristeza, asociados a alteraciones del comportamiento, del grado de actividad y del pensamiento.")
  st.write("Desliza la barra según tus emociones (dónde cero representa lo mínimo y diez lo máximo)")
  desanimado=st.slider("¿Te has sentido desanimado, deprimido ó sin esperanza?", 0, 5, 10)
  placer=st.slider("¿Sientes poco interes o placer en hacer algunas cosas?", 0, 5, 10)
  dormir=st.slider("¿Duermes demasiado, o incluso tienes problemas en dormirte?", 0, 5, 10)
  pensamientos=st.slider("¿Has pensado en la muerte?", 0, 5, 10)
  amor=st.slider("Falta de amor propio, aprecio hacia amigos o familiares", 0, 5, 10)
  st.write("*¡Si quieres saber más, haz click en el siguiente enlace!*")
  st.write("https://youtu.be/vJHYZL-KADg")

Estrés=st.checkbox("Estrés")

if Estrés:
  st.write("El estrés es la respuesta física o mental a una causa externa, como tener muchas tareas o padecer una enfermedad. Un estresor o factor estresante puede ser algo que ocurre una sola vez o a corto plazo, o puede suceder repetidamente durante mucho tiempo.")
  st.write("Desliza la barra según tus emociones (dónde cero representa lo mínimo y diez lo máximo)")
  ahogo=st.slider("Sensación de ahogo", 0, 5, 10)
  comer=st.slider("Mayor necesidad de comer", 0, 5, 10)
  temblores=st.slider("Temblores o TICs", 0, 5, 10)
  calma=st.slider("Dificultad para mantener la calma", 0, 5, 10)
  dolores=st.slider("Dolores de cabeza o abdominales constantes", 0, 5, 10)
  st.write("*¡Si quieres saber más, haz click en el siguiente enlace!*")
  st.write("https://youtu.be/r0mQj2Y_sqI")


SaludMental=st.radio("¿Alguna vez has recibido algún tratamiento psicológico?", ["SI", "NO"])
if SaludMental== "SI":
  st.write("En las sesiones de terapia psicológica, se puede trabajar el desarrollo de habilidades y estrategias que nos ayuden a reducir o controlar los eventos estresantes o los cambios vitales. Además, la terapia resulta sumamente útil para identificar nuevos objetivos y desarrollar un plan para lograrlos. La Universidad Autónoma de Chihuahua a través del DAIE cuenta con un equipo profesional de psicólogos que brindan atención a las y los estudiantes universitarios de manera permanente y gratuita. Para agendar una cita puedes comunicarte al teléfono (614) 4391520 en la extensión 8011.")
if SaludMental== "NO":
  st.write("Si conoces a alguien que requiera ayuda con su salud mental comuncarse a (614) 4391520 en la extensión 8011")
col1,col2,col3=st.columns( [1,2,3] )

st.header ("*¿Sabías que... condiciones mentales cómo la depresión incrementan el riesgo de padecer enfermedades físicas como diabetes?*")
