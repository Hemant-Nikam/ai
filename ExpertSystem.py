print("🏥 Hospital Expert System")
print("---------------------------")

name = input("Enter Patient Name: ")
print(f"Welcome, {name}! Please answer the following questions about your symptoms.\n")

fever = input("Do you have Fever? (yes/no): ")
cough = input("Do you have Cough? (yes/no): ")
cold = input("Do you have Cold? (yes/no): ")
pain = input("Do you have Body Pain? (yes/no): ")
breathing = input("Do you have Breathing Problem? (yes/no): ")

print("\n===== Medical Report =====\n")

print("Patient Name:", name)

# Expert System Rules
if fever == "yes" and cough == "yes" and cold == "yes":

    disease = "Flu"

    doctor = "General Physician"

    medicine = "Paracetamol"

elif fever == "yes" and pain == "yes":

    disease = "Viral Fever"

    doctor = "Medical Specialist"

    medicine = "Crocin"

elif breathing == "yes":

    disease = "Asthma or Lung Infection"

    doctor = "Lung Specialist"

    medicine = "Inhaler"

elif cold == "yes":

    disease = "Common Cold"

    doctor = "ENT Specialist"

    medicine = "Cold Syrup"

else:

    disease = "Normal"

    doctor = "Regular Checkup"

    medicine = "No medicine needed"


print("Possible Disease:", disease)

print("Suggested Doctor:", doctor)

print("Suggested Medicine:", medicine)

print("\nThank You!")