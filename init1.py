#Import Flask Library
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, session, url_for, redirect
import time
import random
import os
import base64
import process_image
import output
import pymysql.cursors
#Initialize the app from Flask
app = Flask(__name__)


db = pymysql.connect(host='192.168.99.100',port=3306,user='root',password='root',db='mnist',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
ALLOWED_EXTENSIONS = 'png,jpg'
UPLOAD_PATH = os.getcwd()
#Define a route to hello function
@app.route('/')
def hello():
    return render_template('upload.html')

@app.route('/upload')
def upload():
	return render_template('upload.html')

@app.route('/result')
def result():
    return render_template('result.html')


#Authenticates the login
@app.route('/pic_identity',methods=['GET','POST'])
def upload_file():
        if	request.method	=='POST':
                if 'file' not in request.files:
                        flash('No file part')
                        return	redirect(request.url)
                file = request.files['file']
                if	file.filename	==	'':
                        flash('No	selected	file')
                        return	redirect(request.url)
                if	file	and	allowed_file(file.filename):
                        filename	=	secure_filename(file.filename)
                        ext = filename.rsplit('.',1)[1]
                        new_filename = 'uploaded'+'.'+ext
                        file.save(os.path.join(UPLOAD_PATH,new_filename))
                        process_image.main(new_filename,ext)
                        result,result_int = output.conv_fc('processed_image.'+ext)
                        query = 'INSERT INTO image_information VALUES(%s,%s,%s)'
                        cursor.execute(query,(filename,time.strftime('%Y.%m.%d %H:%M:%S ',time.localtime(time.time())),int(result_int)))
                        db.commit()




                        return	render_template('result.html',result = result)


def allowed_file(filename):
        return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
        app.run('0.0.0.0',port=5000,debug=True)

