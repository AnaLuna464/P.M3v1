import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib as jb
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np
import plotly as px

# Data import and Pandas dataframe (CVD_cleaned.xlsx)
df = pd.read_xlsx('CVD_cleaned.xlsx')

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

elif sub_menu_option == "Hospital Data":
    st.title("📊 Hospital Data")

elif sub_menu_option == "US Data":
    st.title("📊 US Data")
    st.write("## General information of the dataset")
    st.write("### Preview of data")
    st.dataframe(df.head())
    st.write("### Descriptive statistics")
    st.write(df.describe())
    st.write("### Columns visualization")
    
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



