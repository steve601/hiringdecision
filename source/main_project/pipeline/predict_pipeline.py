import sys
import pandas as pd
from source.commons import load_object
from source.exception import UserException
from source.logger import logging

class PredicPipeline:
    def __init__(self):
        pass
    
    logging.info('Preprocessing user input and making predictions')
    def predict(self,features):
        model_path = 'elements\model.pkl'
        scaler_path = 'elements\scaler.pkl'
        # loaeding objects
        model = load_object(model_path)
        scaler = load_object(scaler_path)
        
        data_scaled = scaler.transform(features)
        prediction = model.predict(data_scaled)
        
        return prediction
logging.info('This class is responsible for mapping all the inputs from html to flask')
class UserData:
    def __init__(self,educationlevel, experienceyears, previouscompanies,
       interviewscore,skillscore,personalityscore,recruitmentstrategy):
        self.edu = educationlevel
        self.exp = experienceyears
        self.comp = previouscompanies
        self.int = interviewscore
        self.skill = skillscore
        self.person = personalityscore
        self.recr = recruitmentstrategy
    logging.info("Converting user's input to df")  
    # let's write a function that returns the user input as a pandas dataframe
    def get_data_as_df(self):
        try:
            user_data = {
                "educationlevel":[self.edu],
                "experienceyears":[self.exp],
                "previouscompanies":[self.comp],
                "interviewscore":[self.int],
                "skillscore":[self.skill],
                "personalityscore":[self.person],
                "recruitmentstrategy":[self.recr]
            }
            return pd.DataFrame(user_data)
        except Exception as e:
            raise UserException(e,sys)
        