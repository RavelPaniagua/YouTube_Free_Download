from flask import Flask, render_template, url_for,redirect,jsonify,json
from pytube import YouTube
from flask import request
import os


app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
@app.route("/home",methods = ['GET','POST'])
def home():
	
	if request.method == 'POST':
		url = request.form['url']
		#bloque de informacion del video
		path = 'C:'
		yt = YouTube(url)
		print(yt)
		titulo = yt.title
		descripcion = yt.description
		duracion = yt.length
		fecha_de_publicacion = yt.publish_date
		image = yt.thumbnail_url


		return render_template("index.html",url=url,titulo=titulo,descripcion=descripcion,duracion=duracion,fecha_de_publicacion=fecha_de_publicacion,image=image)
	else:
		return render_template("index.html")


@app.route("/descarga",methods=['GET'])
def descargar():
	dwl = int(request.args.get('dwl',0))
	url = request.args.get('url',0)
	yt = YouTube(url)
	yt.streams.get_highest_resolution().download()
	
	if dwl != 0:
		dwl='DESCARGA COMPLETA!'
		return dwl
	else:
		dwl='Error al Intentar Descargar el video'

if __name__ == "__main__":
	#app.run("0.0.0.0",8080,debug=True)
	app.run(debug=False,port=8080)
