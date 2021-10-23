from flask import Flask, render_template
import os
import logging

app = Flask(__name__)
logo_image_folder=os.path.join('static','assets')
app.config['UPLOAD_FOLDER']=logo_image_folder
@app.route('/')
def index():
    
    logo_image=os.path.join(app.config['UPLOAD_FOLDER'],'zt-img.png')
    favicon=os.path.join(app.config['UPLOAD_FOLDER'],'favicon.ico')
    return render_template("index.html",logo_image=logo_image,favicon=favicon)

if __name__=="__main__":
    app.run(debug= True)