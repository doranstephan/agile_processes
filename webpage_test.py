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
    
    
    html = "<h3>Hello World!</h3>" \
               "This is a webpage being run on python<br/>" \
<<<<<<< HEAD
               "There may be some changes here in the future This is a testtesttest"
=======
               "There may be some changes here in the future This is a test, another test"
>>>>>>> 92e1afcfe044d1ac6607b94c7796d7b522706faa
    return html.format()
def test_answer():
    assert 2==2

   
if __name__ == "__main__":
    app.run(host='localhost', port=67)
  
    
    
    