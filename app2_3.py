import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib as jb
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np
import plotly as px
import plotly.express as px 
import math as e
from matplotlib import ticker
import plotly.graph_objects as go  
import os 
import json


# Data import and Pandas dataframe (CVD_cleaned.xlsx)
df = pd.read_excel("CVD_cleaned.xlsx", engine="openpyxl") #esto es lo que se tiene que poner para estar publico
#df = pd.read_csv(r'C:\Users\annie\OneDrive\Escritorio\Bootcamp Analisis de Datos\Visual\Proyecto 3\CVD_cleaned.csv')

#Configuration to set the page title, icon, layout and sidebar state
st.set_page_config(
    page_title="Cardiovascular Diseases Analysis",
    page_icon="❤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar menu
with st.sidebar:
    menu_option = option_menu(
        "Menu",
        [
            "Introduction",
            "Data Preview",
            "Prediction Model Dictionary",
            "Prediction Model"
        ],
        icons=[
            'heart',
            'table',
            'check-square',
            'robot'
        ],
        menu_icon="stethoscope",  
        default_index=0,
        orientation="vertical"
    )
# Define `sub_menu_option` with a default value other than the conditional
sub_menu_option = None  

    # Submenu for Data Preview
if menu_option == "Data Preview":
        sub_menu_option = option_menu(
            "Data Preview Options",
            [
                "PBI",
                "Hospital Data",
                "US Data"
            ],
            icons=[
                'globe',
                'hospital',
                'bar-chart-line'
            ],
            menu_icon="menu-app",
            default_index=0,
            orientation="vertical"
        )

# Show "INTRODUCTION" when selected from the menu
if menu_option == "Introduction":
    # App title
    st.title('Cardiovascular Diseases')

    # Introduction--> What's CVD?
    st.write('''
    ### What's CVD?
    The heart is the muscular organ that pumps blood carrying oxygen and nutrients throughout the body with the help of the circulatory system (heart, blood and blood vessels).  
    
    Cardiovascular diseases (CVD) are a group of disorders of the heart and blood vessels. 
    Some of them are: 
    - **Coronary heart disease**: Disease of blood vessels supplying the heart (Heart attack).
    - **Cerebrovascular disease**: Disease of blood vessels supplying the brain (Stroke).
    - **Peripheral arterial disease**: Disease of blood vessels supplying the arms and legs.
    - **Rheumatic heart disease**: Damage to the heart muscle and heart valves from rheumatic fever, caused by streptococcal bacteria.
    - **Congenital heart disease**: Birth defects that affect the normal development and functioning of the heart.
    - **Deep vein thrombosis and pulmonary embolism**: Blood clots in the leg veins, which can dislodge and move to the heart and lungs.
    
    According to the **World Health Organization (WHO)**, cardiovascular diseases (CVD) are the leading cause of death globally. The risk of suffering is higher in older people and increases with some preview pathologies like hypertension, diabetes, obesity, and smoking.
    ''')

    # Introduction--> What are the risk factors?
    st.write('''
    ### What are the risk factors?
    The most important risk factors of heart disease are having an unhealthy diet, physical inactivity, tobacco use and drinking too much alcohol. Genetic factors play a role in high blood pressure and heart disease.
    - **Unhealthy diet**: Having a diet high in saturated fats, trans fat and cholesterol is linked to heart diseases, as well as eating too much salt which can raise the blood pressure.
    - **Physical inactivity**: It can increase the chances of high blood pressure, obesity, high cholesterol and diabetes, which are all risk factors. 
    - **Tobacco use**: Smoking can damage the heart and blood vessels; nicotine raises blood pressure and the carbon monoxide from cigarettes reduces the amount of oxygen that your blood can carry.
    - **Drinking too much alcohol**: It increases the levels of triglycerides, the fatty substance in the blood that increases the risk of heart disease. 
    ''')

    # Introduction--> What are the symptoms?
    st.write('''        
    ### What are the symptoms?
    The symptoms of cardiovascular disease may vary based on your condition but might include: 
    - Chest pain, chest tightness, chest pressure and chest discomfort
    - Pain, weakness or numbness in your legs and/or arms
    - Pain or discomfort in the arms, neck, shoulder, jaw and back
    - Shortness of breath
    - Easily tiring during exercise or activity
    - Changes in your heart rhythm
    - Very fast or slow heartbeat, palpitations or fluttering in your chest
    - Dizziness, lightheadedness or fainting
    - Weakness or fatigue
    - Swelling of the hands, legs, ankles or feet
    - Fever
    - Skin rashes or unusual spots
    - Dry or persistent cough
    ''')

    # Objective of the project
    st.write("""
    ## Objectives of the project 
    The objective of this project is to be able to inform society of the importance of cardiovascular diseases and to have an AI tool that can predict the probability of a person having a cardiovascular disease which is in the "Prediction Model" section. This tool will help the user to know if they are at risk of having a cardiovascular disease and give them some tips to prevent and take care of their health.
    """)

    # Image upload
    image_path = r"Heart_blue_red.jpeg"
    try:
        image = Image.open(image_path)
        st.image(image, caption="Heart visualization", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")


# Just show the information of the selection from the submenu
#Verify if the user selected "PBI" in the submenu
if sub_menu_option == "PBI":
    st.title("🗺️ Power BI Dashboard")
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiYzIwYjA5ODUtZTZkMS00ZGQwLWFjMTQtMWNiNTlhNzNlNDlhIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
    #Just to show "PBI" when selected from the submenu
    st.markdown(f"""
        <iframe title="Mapa Power BI" width="900" height="600"
        src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)

if sub_menu_option == "Hospital Data":
    st.title("📊 Hospital Data")
    st.write("## General information of the dataset")
    # Descripción del dataset
    st.write('''
    ### Data description
    There are 3 types of input features:
    - **Objective**: Factual information  
    - **Examination**: Results of medical examination  
    - **Subjective**: Information given by the patient.  

    **Features:**
    - **Age**   
    - **Height** | (cm)  
    - **Weight** | (kg)  
    - **Gender** | (1 = female, 2 = male)  
    - **Systolic blood pressure**  
    - **Diastolic blood pressure**  
    - **Cholesterol** | 1: normal, 2: above normal, 3: well above normal  
    - **Glucose** | 1: normal, 2: above normal, 3: well above normal  
    - **Smoking** 
    - **Alcohol intake** 
    - **Physical activity**   
    - **Cardiovascular disease**  
    ''')

    # Introducción al dataset
    st.write("""
    ### Introduction
    This dataset was obtained from the Kaggle platform and contains health-related information for approximately 70,000 patients in a hospital.  
    The objective is to analyze the general health characteristics of patients and their likelihood of developing cardiovascular disease. 
    The data includes a wide range of variables that capture vital signs, medical history, lifestyle factors, and laboratory results, which can be used to identify patterns and correlations with cardiovascular disease risk. 
    """)

    # Image 1 "Relationship between age and cardiovascular disease"
    image_path = r"Img1. Relationship between age and cvd.jpeg"
    try:
        image = Image.open(image_path)
        st.image(image, caption="Relationship between age and cardiovascular disease", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")

    st.write('''
    The graph shows a positive relationship between age and cardiovascular disease, with higher ages (45-65 years) more commonly associated with the presence of the disease. This aligns with...
    ''')
    

    #Image 2 "Relationship between smokers and gender"
    # Image upload
    image_path = r"Img2. Smokers by gender.png"
    try:
        image = Image.open(image_path)
        st.image(image, caption="Smokers by gender", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")
        
    st.write('''The graph indicates that men have a higher proportion of smokers compared to women. Since smoking is a significant risk factor for cardiovascular diseases, this suggests that men may be at a higher risk for developing such conditions due to their higher smoking rates. This gender difference in smoking behavior could contribute to disparities in cardiovascular health between men and women.''')

#Image 3 "Relacion entre peso y presion diastolica"
        # Image upload
    image_path = r"Img3. Weight and diastolic pressure.png"
    try:
        image = Image.open(image_path)
        st.image(image, caption="Weight and diastolic pressure", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")
        
    st.write('''This graph examines the connection between weight ranges (0-50, 50-60, 60-70, 70-80, 80-90) and diastolic blood pressure categories (Normal, Low, Hypotension, Emergency).
        From the graph, it appears that as weight increases, there is a trend towards higher diastolic blood pressure. Individuals in higher weight ranges (70-90) are more likely to fall into the "Normal" or potentially "Emergency" diastolic pressure categories, while those in lower weight ranges (0-60) are more associated with "Low" or "Hypotension."
        This suggests that higher weight may be linked to increased diastolic blood pressure, which is a risk factor for cardiovascular diseases.''')
    
        
#Image 4 " Relacion entre colesterol y glucosa"
        # Image upload
    image_path = r"Img4. Relationship between cholesterol and glucose.png"
    try:
        image = Image.open(image_path)
        st.image(image, caption="Relationship between cholesterol and glucose", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")
        
    st.write('''It is evident that as glucose levels increase from category 1 to category 3, cholesterol levels also tend to rise. 
            This positive correlation suggests that individuals with higher glucose levels are more likely to have elevated cholesterol levels. 
            Both high glucose (indicative of diabetes or prediabetes) and high cholesterol are significant risk factors for cardiovascular diseases, including heart attacks and strokes.
            Poor glucose control can lead to dyslipidemia (abnormal cholesterol levels), and both conditions contribute to the development of atherosclerosis (plaque buildup in arteries).''')

#Image 5 "Distribucion de la presion diastólica con respecto al genero"
            # Image upload
    image_path = r"Img5. Diastolic pressure by gender.png"
    try:
        image = Image.open(image_path)
        st.image(image, caption="Diastolic pressure by gender", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")
#Image 6  "Distribucion de la presion sistolica con respecto al genero"
            # Image upload
    image_path = r"Img6. Sistolic pressure by gender.png"
    try:
        image = Image.open(image_path)
        st.image(image, caption="Sistolic pressure by gender", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")

    st.write('''
    ### Combined Conclusions by Gender:
- Men:

They are at a higher risk of elevated both diastolic and systolic pressure, which are significant risk factors for cardiovascular diseases.

Implementing specific preventive and management strategies, such as regular health check-ups, lifestyle modifications, and stress management, is crucial for this group.

- Women:

While they tend to have lower diastolic and systolic pressure levels, continuous monitoring is essential to ensure early detection of any significant changes, especially during critical life stages like pregnancy or menopause.
''')
    
    #Image 7 "Cantidad de valores por rango de presion sistolica"
            # Image upload
    image_path = r"Img7. Sistolic pressure range.png"
    try:
        image = Image.open(image_path)
        st.image(image, caption="Sistolic pressure range", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")
        
    st.write('''
    ### Key Observations:
Distribution of Values:

The graph likely shows a distribution where most values fall within the Normal or Elevated ranges, with fewer values in the Hypertension and Emergency categories.

However, if there is a significant number of values in the Hypertension or Emergency ranges, this would indicate a high prevalence of uncontrolled blood pressure in the population.

Health Implications:

A high number of values in the Hypertension ranges (Stage 1 and Stage 2) suggests a population at risk for cardiovascular diseases, stroke, and kidney problems.

A high number of values in the Emergency range would indicate a critical need for immediate medical interventions and public health campaigns.

''')
    
    #Image 8 " Cantidad de valores por rangos de presion diastolica
            # Image upload
    image_path = r"Img8. Distolic pressure range.png"
    try:
        image = Image.open(image_path)
        st.image(image, caption="Distolic pressure range", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")
        
    st.write('''Analysis by Diastolic Pressure Range: Normal Range:

This category represents individuals with healthy diastolic blood pressure levels.


Low Range:

This category includes individuals with slightly lower than normal diastolic pressure.


Hypotension:

This range represents abnormally low diastolic blood pressure, which can cause symptoms like dizziness and fainting.


Emergency:

This category represents critically low diastolic pressure levels requiring immediate medical attention.

''')
    
    st.write('''
    ### Key observations 2:
Distribution of Values:

The majority of values fall within the Normal range (13,916), suggesting that most of the population has healthy diastolic blood pressure levels.

A smaller number of values are in Hypotension (176) and Emergency (47) ranges, indicating a minor but significant portion of the population with low or critically low diastolic pressure.

Health Implications:

The presence of values in the Hypotension and Emergency ranges highlights the need for medical attention for those with abnormally low diastolic pressure, as it can lead to complications like organ damage or shock.

Intervention Strategies:

For individuals in the Low and Hypotension ranges, lifestyle adjustments such as increased fluid intake, dietary changes, and monitoring for symptoms like dizziness are important.

Individuals in the Emergency range require immediate medical intervention to stabilize their blood pressure and prevent further complications.
''')



elif sub_menu_option == "US Data":
    st.title("📊 US Data")
    st.write("## General information of the dataset")
    st.write("### Preview of data")
    st.dataframe(df.head())
    st.write("### Descriptive statistics")
    st.write(df.describe())
    st.write("### Graphs visualisation")
    
    # Function to plot categorical columns
    def plot_categorical_columns(df, column):
        # Set the figure size
        plt.figure(figsize=(8, 6))
        
        # Create the count plot with sorted values
        sorted_values = df[column].value_counts().index
        sns.countplot(x=column, data=df, palette="Set1", order=sorted_values)
        
        # Calculate the total number of entries
        total = len(df)
        
        # Adjust the y-axis limits to provide extra space for annotations
        plt.ylim(0, df[column].value_counts().max() * 1.15)
        
        # Set the annotations on top of each column to show the exact number of entries and percentage
        for p in plt.gca().patches:
            height = p.get_height()
            percentage = f'{height / total * 100:.1f}%'
            plt.gca().annotate(f'{height}\n({percentage})', (p.get_x() + p.get_width() / 2., height), 
                            ha='center', va='center', fontsize=10, color='black', xytext=(0, 12), 
                            textcoords='offset points')
        
        # Set the title and labels
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
        st.pyplot(plt.gcf())

    # Filter out specific columns from the selectbox options
    exclude_columns = ['Diabetes', 'Checkup', 'Age_Category', 'Heart_Disease']
    categorical_columns = [col for col in df.select_dtypes(include=['object', 'category']).columns if col not in exclude_columns]
    
    selected_column = st.selectbox("Selecciona una columna para visualizar:", categorical_columns)
    
    # Call the function to plot the selected categorical column
    plot_categorical_columns(df, selected_column)

    st.write('''From the plots above, we can see that the most columns coincide with the target variable in that most of the subjects do not have heart disease and most of them don't smoke, don't have other diseases, they exercise often and over 50% have good health.''')

if sub_menu_option == "US Data":
    # For the columns Age_Category', 'Checkup' and 'Diabetes', we need to plot them separately because we need to make room for the x-axis labels by rotating them for better readability.
    # Other than that, we'll use the same code as before.
    # Define the columns to plot
    columns_to_plot = ['Age_Category', 'Checkup', 'Diabetes']

    # Add a selectbox to choose the column to plot
    selected_column_to_plot = st.selectbox("Selecciona una columna para visualizar (con etiquetas rotadas):", columns_to_plot)

    # Set the figure size
    plt.figure(figsize=(10, 6))

    # Create the count plot with adjusted bar width and sorted values
    sorted_values = df[selected_column_to_plot].value_counts().index
    sns.countplot(x=selected_column_to_plot, data=df, palette="Set1", order=sorted_values, width=0.6)

    # Calculate the total number of entries
    total = len(df)

    # Adjust the y-axis limits to provide extra space for annotations
    plt.ylim(0, df[selected_column_to_plot].value_counts().max() * 1.15)

    # Add annotations on top of each column to show the exact number of entries
    for p in plt.gca().patches:
        height = p.get_height()
        percentage = f'{height / total * 100:.1f}%'
        plt.gca().annotate(f'{height}\n({percentage})', (p.get_x() + p.get_width() / 2., height), 
                            ha='center', va='center', fontsize=10, color='black', xytext=(0, 12), 
                            textcoords='offset points')

    # Rotate the x-labels for better readability
    plt.xticks(rotation=45)

    # Set the title and labels
    plt.title(f'Distribution of {selected_column_to_plot}')
    plt.xlabel(selected_column_to_plot)
    plt.ylabel('Count')

    # Display the plot
    st.pyplot(plt.gcf())

# Show prediction model
if menu_option == "Prediction Model":
    st.write("### Prediction based on entered data")
    columns_to_predict = st.multiselect("Select the information for the prediction model", df.columns)
    target = st.selectbox("Select the target variable", df.columns)
    
    if columns_to_predict and target:
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score
    
        # Prepare data
        X = df[columns_to_predict]
        y = df[target]
    
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
        # Train model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
    
        # Evaluation
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        st.write(f"Model accuracy: {accuracy:.2f}")
    
        # Predict new data
        st.write("### Enter new data for prediction")
        user_input = {}
        for col in columns_to_predict:
            user_input[col] = st.number_input(f"{col}", value=float(X[col].mean()))
    
        if st.button("Predict"):
            user_df = pd.DataFrame([user_input])
            prediction = model.predict(user_df)[0]
            st.write(f"The prediction for the entered data is: {prediction}")

# Show prediction model dictionary
if menu_option == "Prediction Model Dictionary":
    st.write("### Prediction Model Dictionary")
    st.write('''
                •	Exang (Exercise induced angina): Refers to whether the patient experienced angina (chest pain) induced by exercise during a stress test. It’s typically a binary value: 
                    
    - 1: The patient experienced angina.
    - 0: The patient did not experience angina.
             
•	Old Peak (Depression of the ST segment): This variable measures the depression of the ST segment in an electrocardiogram (ECG) after exercise. ST segment depression can indicate ischemia (lack of oxygen in the heart muscle). 
    
    - The value of "Old Peak" refers to how many millimeters the ST segment is depressed.
             
•	Slope (Slope of the ST segment during exercise): This value measures the slope of the ST segment during exercise in a stress test. 
    
    - 1: Upsloping (a positive result, typically indicating no problem).
    - 2: Flat (neutral, not particularly concerning).
    - 3: Downsloping (which can be indicative of a higher risk of heart problems).
•	Ca (Number of major vessels colored by fluoroscopy): This value indicates how many of the main coronary arteries show significant blockages during an imaging test, such as fluoroscopy. It is a numerical value: 
    
    - 0: No blockage observed.
    - 1, 2, or 3: Indicates increasing degrees of obstruction in the coronary arteries.
    
•	Thal (Thalassemia or defect in myocardial perfusion): Refers to a diagnosis of thalassemia (a blood disorder) or a defect in myocardial perfusion (blood flow to the heart). 

    - 3: Normal (no defects).
    - 6: Fixed defect (indicating damage to the heart muscle).
    - 7: Reversible defect (indicating abnormal blood flow under stress but normal perfusion at rest).
•	Restecg (Resting electrocardiographic results): Refers to the results of an ECG taken while the patient is at rest. 
    
    - 0: Normal (no abnormality detected in the ECG at rest).
    - 1: ST-T wave abnormality (changes in the ST-T segment that may indicate ischemia).
    - 2: Left ventricular hypertrophy (enlargement of the left ventricle, often due to high blood pressure or heart disease).
•	Thalach (Maximum heart rate achieved): Refers to the highest heart rate achieved during a stress test or physical exertion. 
    
    - The value is expressed in beats per minute (bpm) and reflects how the heart responds to exercise. 
    A higher maximum heart rate can indicate better cardiovascular fitness, while a low maximum heart rate may signal potential heart issues.''')

    st.write('''
    ### Important terminology:
Gender = 1 male, 0 female
             
CP = Chest Pain type
             
Trestbps = Resting blood pressure (in mm Hg on admission to the hospital)
             
Chol = Serum Cholesterol in mg/dl
             
Fbs = Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
             
Restecg = Resting electrocardiographic results (values 0, 1, 2)
             
Thalach = Maximum heart rate achieved''')
