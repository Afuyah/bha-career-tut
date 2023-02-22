from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'title' : 'Frontend Engineer',
    'location':'Arusha, Tanzania',
    'salary': 'ksh 45000'
  },
  {
    'id': 2,
    'title' : 'Software Analyst',
    'location':'mombasa, Kenya',
    'salary': 'ksh 75000'
  },
  {
    'id': 3,
    'title' : 'Web developer',
    'location':'mombasa, Kenya',
    'salary': 'ksh 35000'
  },
  {
    'id': 4,
    'title' : 'Network Administrator',
    'location':'Kisumu, Kenya',
    'salary': 'ksh 47000'
 }
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                           company_name ='Bha')
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug= True)