# ML-Final-Project

## Random Forest Classifier to predict obesity levels for particular features including:
    - Gender
    - Age
    - Height
    - Weight
    - family_history_with_overweight
    - FAVC		Do you eat high caloric food frequently?
    - FCVC	Do you usually eat vegetables in your meals?
    - NCP	How many main meals do you have daily?
    - CAEC	Do you eat any food between meals?
    - SMOKE Do you smoke?
    - CH2O	How much water do you drink daily?
    - SCC	Do you monitor the calories you eat daily?
    - FAF	How often do you have physical activity?
    - TUE	How much time do you use technological devices?
    - CALC	How often do you drink alcohol?
    - MTRANS  Which transportation do you usually use?
    
    TARGET FEATURE:
    - NObeyesdad	Obesity level


## Application

This repository possess an application that users can to predict their own obesity level. The model will classify their obesity level and will provide the user with a detailed guide to either maintaining their current obesity level, or reccomendations for reducing their obesity levels. 


## Application Usage:
1. The user needs to go to https://openai.com to create an api user account and generate an api key for the project.
    ### The user may need to provide some money in order to effectively use the api, 5 dollars is more than enough

2. Once the api is created, navigate to main.py and replace "YOUR OPENAI API KEY HERE" with their own key.

3. The user needs to install the necessary requirements by going to the terminal in putting in the command:

    ### pip install -r requirements.txt

4. The user needs to run the local back end by running:
    ### python main.py

5. To launch the application, type the following command:
    ### streamlit run app.py
