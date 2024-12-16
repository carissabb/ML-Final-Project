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

## Model Generation  
**Note:** These steps are optional for running the application, as it already uses the `.pkl` files in the **`models`** folder, which are considered up-to-date with the current state of the model.  

To train the random forest classifier, open the `.ipynb` file titled **`RandomForestClassifier.ipynb`**. This notebook contains the necessary code to run and evaluate the model, as well as save its state for use in the application. After executing all cells in the notebook, four `.pkl` files will be generated. These files represent the model's current state, along with the necessary scalers and encoders.  

If you need the latest version of these `.pkl` files for your application, replace the current `.pkl` files in the **`models`** folder with the newly created ones.  


---

## Application  

This repository includes an application that predicts a user's obesity level based on their input. The model classifies their obesity level and provides a detailed guide for maintaining their current level or recommendations for reducing it.  

---

## Application Usage  

1. **Create an OpenAI API Key:**  
   Visit [https://openai.com](https://openai.com) to create an API user account and generate an API key for the project.  
   - *Note:* You may need to deposit a small amount (e.g., $5), which is sufficient for this project.

2. **Set Your API Key:**  
   Navigate to **`main.py`** and replace `"YOUR OPENAI API KEY HERE"` with your API key.

3. **Install Dependencies:**  
   Open a terminal and run the following command:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Backend:**  
   Start the local backend by running:  
   ```bash
   python main.py
   ```

5. **Launch the Application:**  
   Use the following command to start the application:  
   ```bash
   streamlit run app.py
   ```  
