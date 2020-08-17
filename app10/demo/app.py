from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import pandas
import ssl
import geopy.geocoders
from geopy.geocoders import ArcGIS
import datetime

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
geopy.geocoders.options.default_ssl_context = ctx

app = Flask(__name__)

def style_line(s):
    '''Rendering odd and even rows with different color'''
    return ['background-color: #D4E6F1' if i%2!=0 else 'background-color: #85C1E9' for i in range(len(s))]

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/success/', methods=['POST'])
def success():
    global filename
    if request.method == 'POST':
        file = request.files["file"]
        # file.save(secure_filename("uploaded_"+file.filename))
        # df = pandas.read_csv("uploaded_"+file.filename)
        # try:
        df = pandas.read_csv(file)
        if "address" in df.columns or "Address" in df.columns:
            nom = ArcGIS(timeout=300)
            df["Latitude"] = round(df["Address"].apply(nom.geocode).apply(lambda x: x.latitude if x != None else None), 2)
            df["Longitude"] = round(df["Address"].apply(nom.geocode).apply(lambda x: x.longitude if x != None else None), 2)
            filename = datetime.datetime.now().strftime("uploads/%Y-%m-%d-%H-%M-%S-%f"+".csv")
            df.to_csv(filename, sep=',', encoding='utf-8', index = False, header=True)
            # build the table on the success page
            html = df.to_html(index=False, na_rep="NA", classes='datatable')
            return render_template("index.html", text=html, btn="download.html")
        # expect:
        else:
            return render_template("index.html", text="Please make sure you have an address column in your CSV file!")

@app.route('/downloads/')
def download():
    return send_file(filename, attachment_filename="myfile.csv", as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run()