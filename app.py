import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            max_tokens=100,
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Summarize the documents required to obtain that certificate in India in bullet points.

Animal: Life certificate
Names: 
1. Aadhaar Number
2. Mobile Number
3. Pension Payment Order(PPO) number
Animal: Death certificate
Names:
1. Proof of birth of the deceased.
2. Cremation/Burial Certificate.
3. Certificates of Institutes – Hospital/Doctors.
Animal: {}
Names:""".format(
        animal.capitalize()
    )
