import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib as jb
from streamlit_option_menu import option_menu
from PIL import Image

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
            "Prevention",
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
    # Título de la aplicación
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
    image_path = r"C:\Users\annie\OneDrive\Escritorio\Bootcamp Analisis de Datos\Visual\Proyecto 3\Heart_blue_red.jpeg"
    try:
        image = Image.open(image_path)
        st.image(image, caption="Heart visualization", use_container_width=True)
    except FileNotFoundError:
        st.error("No se encontró el archivo en la ruta especificada.")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")

# Just to show "PBI" when selected from the submenu
#Verify if `sub_menu_option` has a value before accessing it
if sub_menu_option == "PBI":
    st.title("🗺️ Power BI Dashboard")

    powerbi_url="https://app.powerbi.com/view?r=eyJrIjoiYzIwYjA5ODUtZTZkMS00ZGQwLWFjMTQtMWNiNTlhNzNlNDlhIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
# Incrustar el mapa de Power BI en Streamlit
st.markdown(f"""
    <iframe title="Mapa Power BI" width="900" height="600"
    src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>
""", unsafe_allow_html=True)

if sub_menu_option == "Hospital Data":
    st.title("📊 Hospital Data")

if sub_menu_option == "US Data":
    st.title("📊 US Data")