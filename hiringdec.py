from flask import Flask,request,render_template
from source.logger import logging
from source.main_project.pipeline.predict_pipeline import PredicPipeline,UserData

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('hiring.html')

@app.route('/predict',methods = ['POST'])
def do_prediction():
    forms_data = UserData(
        educationlevel=request.form.get('edu'),
        experienceyears=request.form.get('exp'),
        previouscompanies=request.form.get('comp'),
        interviewscore=request.form.get('int'),
        skillscore=request.form.get('skill'),
        personalityscore=request.form.get('person'),
        recruitmentstrategy=request.form.get('recr')
    )
    logging.info('Converting to a pandas dataframe')
    input_df = forms_data.get_data_as_df()
    
    logging.info('Initializing the predit class')
    predictpipe = PredicPipeline()
    result = predictpipe.predict(input_df)
    
    msg = 'Applicant is likely to be hired' if result == 1 else 'Applicant is unlikely to be hired'
    
    return render_template('hiring.html',text = msg)

if __name__ == "__main__":
    app.run(debug=True)