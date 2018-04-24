# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:34:27 2018

@author: Padraigh Jarvis
"""
from flask import Flask


app = Flask(__name__)
hostName ='127.0.0.1'



@app.route("/")
def hello():
    
    
    html = "<h3>Hello World3!</h3>" \
			   "This is a webpage being run on python<br/>" \
			   "There may be some changes here in the future This is a testtesttes"\
			   "There may be some changes here in the future This is a test, another tessst"\
			   "There may be some changes here in the future This is a testtesttest"\
			   "There may be some changes here in the future This is a test, another test, ryan testsssss"
    return html.format()

   
if __name__ == "__main__":
    app.run(host='localhost', port=67)
  
    
    
    