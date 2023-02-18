from flask import Flask, render_template, request, Response
from flask_cors import CORS
from run import process as processing
# engine: solution 1, 
# run: solution 2 #

app=Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file(): 
    file = request.files['file']
    filename=(file.filename).split(".")[0]
    if file:
        df=processing(file)
        return Response(
            df.to_csv(),
            mimetype='text/csv',
            headers={'Content-disposition': f"attachment; filename=result_{filename}.csv"}
        )
        # return send_file('output/result_'+(file.filename).split(".")[0]+".csv" , mimetype='text/csv',  as_attachment=True)

if __name__ == "__main__":
    app.run()