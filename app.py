from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

hospital_data = pd.read_csv('cleaned_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    city = request.form.get('city')
    hospital_type = request.form.get('hospital_type')

    filtered_hospitals = hospital_data[(hospital_data['City'] == city) & (hospital_data['Hospital Type'] == hospital_type)]

    sorted_hospitals = filtered_hospitals.sort_values(by='User Ratings(out of 5)', ascending=False)

    return render_template('results.html', hospitals=sorted_hospitals.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
