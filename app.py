import numpy as np
import pandas as pd
import pickle
import train_predict
from flask import Flask, jsonify, render_template, request,redirect, url_for
from flask_ngrok import run_with_ngrok
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# load the dataset but only keep the top n words, zero the rest
top_words = 10000
max_words = 500

#load the csv file saved


# webapp
app = Flask(_name_, template_folder='./') 

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# db = SQLAlchemy(app)

run_with_ngrok(app)


@app.route('/', methods=['POST', 'GET'])
def main():
   
    
        # while True:
        #     file_name = input("Enter file name to predict or z to exit: ")
        #     if file_name == 'z':
        #         break
                
        #     raw_features = extract.start(file_name)
            
        #     raw_baseline_angle = raw_features[0]
        #     baseline_angle, comment = categorize.determine_baseline_angle(raw_baseline_angle)
        #     print("Baseline Angle: "+comment)
            
        #     raw_top_margin = raw_features[1]
        #     top_margin, comment = categorize.determine_top_margin(raw_top_margin)
        #     print("Top Margin: "+comment)
            
        #     raw_letter_size = raw_features[2]
        #     letter_size, comment = categorize.determine_letter_size(raw_letter_size)
        #     print("Letter Size: "+comment)
            
        #     raw_line_spacing = raw_features[3]
        #     line_spacing, comment = categorize.determine_line_spacing(raw_line_spacing)
        #     print("Line Spacing: "+comment)
            
        #     raw_word_spacing = raw_features[4]
        #     word_spacing, comment = categorize.determine_word_spacing(raw_word_spacing)
        #     print("Word Spacing: "+comment)
            
        #     raw_pen_pressure = raw_features[5]
        #     pen_pressure, comment = categorize.determine_pen_pressure(raw_pen_pressure)
        #     print("Pen Pressure: "+comment)
            
        #     raw_slant_angle = raw_features[6]
        #     slant_angle, comment = categorize.determine_slant_angle(raw_slant_angle)
        #     print("Slant: "+comment)
            
        #     print("Emotional Stability: ", clf1.predict([[baseline_angle, slant_angle]]))
        #     print("Mental Energy or Will Power: ", clf2.predict([[letter_size, pen_pressure]]))
        #     print("Modesty: ", clf3.predict([[letter_size, top_margin]]))
        #     print("Personal Harmony and Flexibility: ", clf4.predict([[line_spacing, word_spacing]]))
        #     print("Lack of Discipline: ", clf5.predict([[slant_angle, top_margin]]))
        #     print("Poor Concentration: ", clf6.predict([[letter_size, line_spacing]]))
        #     print("Non Communicativeness: ", clf7.predict([[letter_size, word_spacing]]))
        #     print("Social Isolation: ", clf8.predict([[line_spacing, word_spacing]]))
        #     print("---------------------------------------------------")
		
	#=================================================================================================
		
# else:
# 	print(("Error: label_list file not found."))
        
    return render_template('index.html')





if _name_ == '_main_':
    app.run()