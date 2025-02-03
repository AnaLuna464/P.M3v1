import streamlit as st
import json 
import urllib.request

#PRIMERO LA URL QUE CONDUCE A NUESTRO MODELO MAS LA CLAVE API QUE NOS PERMITE ACCEDER A EL
url = 'http://26639feb-ab23-4601-a19e-b8d6dcc1d173.eastus2.azurecontainer.io/score' # URL of the API
api_key = 'oDJGJJz8PRmZB0e2IN5bSPiCvYUX1KEx'

#FUNCION DE PREDICCION
def get_prediction(data):
    body = str.encode(json.dumps(data))
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        return json.loads(result)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(json.loads(error.read()))
        return None

#CONFIGURACION DE LA APP
st.title('Heart disease prediction')
st.write('This is a simple price prediction app')


#DEFINIR LAS VARIABLES QUE NUESTRO MODELO CONOCE

age = st.number_input('Age', min_value=1 , max_value=90, value=1)
sex = st.selectbox('Sex', ['1', '0'])
cp = st.selectbox('Chest pain', ['1', '2', '3', '4'])
trestbps = st.number_input('Resting blood pressure', min_value=90, max_value=180, value=90)
chol = st.number_input('Cholesterol', min_value=150, max_value=450, value=150)
fbs = st.selectbox('Fasting blood sugar > 120 mg/dl', ['0', '1'])
restecg = st.selectbox('Resting electrocardiographic results', ['0', '1', '2'])
thalach = st.number_input('Maximum heart rate achieved', min_value=90, max_value=200, value=90)
exang = st.selectbox('Exercise induced angina', ['0', '1'])
oldpeak = st.number_input('ST depression induced by exercise relative to rest', min_value=0.0, max_value=6.2, value=0.1)
slope = st.selectbox('The slope of the peak exercise ST segment', ['1', '2', '3'])
ca = st.selectbox('Number of major vessels (0-3) colored by flourosopy', ['0', '1', '2', '3'])
thal = st.selectbox('Thalassemia', ['3', '6', '7'])


#DICCIONARIO DE DATOS
data = {
    "Inputs": {
        "input1": [
            {
                'age': age,
                'sex': sex,
                'cp': cp,
                'trestbps': trestbps,
                'chol': chol,
                'fbs': fbs,
                'restecg': restecg,
                'thalach': thalach,
                'exang': exang,
                'oldpeak': oldpeak,
                'slope': slope,
                'ca': ca,
                'thal': thal,
            }
        ]
    },
    "GlobalParameters": {}
}

# Botón predict
if st.button('Chances of heart disease'):
    result = get_prediction(data)

    if result:
        st.write('Chances of heart disease: ', result['Results']['WebServiceOutput0'][0]['predicted_heart_condition'])
    else:
        st.write('Something went wrong')