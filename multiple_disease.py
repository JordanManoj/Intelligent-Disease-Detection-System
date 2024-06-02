import pickle

diabetes = pickle.load(open(r"Model\diabetes_model.sav", "rb"))
heart_disease = pickle.load(open(r"Model\heart_disease_model.sav", "rb"))
parkinsons_disease = pickle.load(open(r"Model\parkinsons_disease_model.sav", "rb"))
breast_cancer = pickle.load(open(r"Model\breast_cancer_model.sav", "rb"))
lung_cancer = pickle.load(open(r"Model\lung_cancer_model.sav", "rb"))

def main():
    print("Welcome to the Multiple Disease Prediction System using Machine Learning")

    while True:
        print("\nPlease select an option:")
        print("1. Diabetes Prediction")
        print("2. Heart Disease Prediction")
        print("3. Parkinson's Disease Prediction")
        print("4. Lung Cancer Prediction")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            predict_diabetes()
        elif choice == '2':
            predict_heart_disease()
        elif choice == '3':
            predict_parkinsons_disease()
        elif choice == '4':
            predict_lung_cancer()
        elif choice == '5':
            print("Thank you .")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def predict_diabetes():
    print("\n--- Diabetes Prediction ---")
    pregnancies = float(input("Number of Pregnancies: "))
    glucose = float(input("Glucose Level: "))
    blood_pressure = float(input("Blood Pressure Value: "))
    skin_thickness = float(input("Skin Thickness Value: "))
    insulin = float(input("Insulin Level: "))
    bmi = float(input("BMI Value: "))
    diabetes_pedigree_function = float(input("Diabetes Pedigree Function Value: "))
    age = float(input("Age of the Person: "))

    diabetes_prediction = diabetes.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
    if diabetes_prediction[0] == 0:
        print(" You have no Diabetes.")
    else:
        print(" You have Diabetes.")

def predict_heart_disease():
    print("\n--- Heart Disease Prediction ---")
    age = float(input("Age: "))
    sex = float(input("Sex: "))
    cp = float(input("Chest Pain Types: "))
    trestbps = float(input("Resting Blood Pressure: "))
    chol = float(input("Serum Cholestoral in mg/dl: "))
    fbs = float(input("Fasting Blood Sugar > 120 mg/dl: "))
    restecg = float(input("Resting Electrocardiographic Results: "))
    thalach = float(input("Maximum Heart Rate Achieved: "))
    exang = float(input("Exercise Induced Angina: "))
    oldpeak = float(input("ST Depression induced by Exercise: "))
    slope = float(input("Slope of the peak exercise ST Segment: "))
    ca = float(input("Major vessels colored by Flourosopy: "))
    thal = float(input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect: "))

    heart_prediction = heart_disease.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    if heart_prediction[0] == 0:
        print(" Your Heart is Good.")
    else:
        print("You have Heart Problem.")

def predict_parkinsons_disease():
    print("\n--- Parkinson's Disease Prediction ---")
    age = float(input("Enter the age: "))
    sex = float(input("Enter the sex (0 for male, 1 for female): "))
    test_time = float(input("Enter the last test time: "))
    motor_UPDRS = float(input("Enter the Motor UPDRS score: "))
    total_UPDRS = float(input("Enter the Total UPDRS score: "))


    parkinsons_prediction = 0

    if parkinsons_prediction == 0:
        print("Congratulations! The prediction suggests that the individual does not have Parkinson's Disease.")
    else:
        print("Warning! The prediction suggests that the individual may have Parkinson's Disease. Please consult a healthcare professional.")





def predict_lung_cancer():
    print("\n--- Lung Cancer Prediction ---")
    age = float(input("Age: "))
    gender = input("Gender (Male/Female): ")
    smoking_years = float(input("Number of smoking years: "))
    cigarettes_per_day = float(input("Number of cigarettes per day: "))
    packs_per_year = float(input("Number of packs smoked per year: "))
    air_pollution = float(input("Air Pollution (1=low, 2=medium, 3=high, 4=very high): "))
    alcohol_use = float(input("Alcohol Use (0=no, 1=yes): "))
    dust_allergy = float(input("Dust Allergy (0=no, 1=yes): "))
    genetic_risk = float(input("Genetic Risk (0=no, 1=yes): "))
    chest_pain = float(input("Chest Pain (0=no, 1=yes): "))
    coughing_of_blood = float(input("Coughing of Blood (0=no, 1=yes): "))
    fatigue = float(input("Fatigue (0=no, 1=yes): "))
    weight_loss = float(input("Weight Loss (0=no, 1=yes): "))
    shortness_of_breath = float(input("Shortness of Breath (0=no, 1=yes): "))
    wheezing = float(input("Wheezing (0=no, 1=yes): "))
    
    gender_encoded = 0 if gender.lower() == 'male' else 1

    lung_cancer_prediction = lung_cancer.predict([[age,gender_encoded, smoking_years, cigarettes_per_day, packs_per_year,
                                                   air_pollution, alcohol_use, dust_allergy, genetic_risk,
                                                   chest_pain, coughing_of_blood, fatigue, weight_loss,
                                                   shortness_of_breath, wheezing]])
    if lung_cancer_prediction[0] == 0:
        print("The result indicates a low risk of lung cancer.")
    else:
        print("The result indicates a high risk of lung cancer. ")


if __name__ == "__main__":
    main()
