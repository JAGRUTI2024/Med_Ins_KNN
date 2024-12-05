from flask import Flask, jsonify, request
import config
from Project.utils import MedicalInsurance

app=Flask(__name__)
@app.route("/")
def get_home():
    return "Hello! Welcome"

@app.route("/predict_charges", methods=["POST", "GET"])
def get_medical():
    if request.method=="POST":
        data=request.form
        age=int(data["age"])
        bmi=float(data["bmi"])
        children=int(data["children"])
        smoker=data["smoker"]
        region=data["region"]

        obj=MedicalInsurance(age, bmi, children, smoker, region)
        charges=obj.get_charges()

        return jsonify({"Result": f"Predicted MedicalInns Charges {charges}"})
if __name__=="__main__":
    app.run()
    
