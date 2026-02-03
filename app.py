from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        resume = request.form["resume"]
        job = request.form["job"]

        prompt = f"""
        Compare this resume with the job description.
        Give match percentage and missing skills.

        Resume:
        {resume}

        Job Description:
        {job}
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

