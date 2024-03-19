from flask import *

app=Flask(__name__)



@app.route('/')
def admin():
    return render_template('index.html')

@app.route('/coding')
def coding():
    return render_template('coding.html')

@app.route('/canva')
def canva():
    return render_template('canva_poster.html')

@app.route('/video')
def Videography():
    return render_template('Videography.html')

@app.route('/cultural')
def cultural():
    return render_template('cultural.html')

@app.route('/madad')
def madad():
    return render_template('madad.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/treasure_hunt')
def th():
    return render_template('treasure_hunt.html')

@app.route('/craft')
def craft():
    return render_template('craft.html')

@app.route('/typo')
def typo():
    return render_template('typo.html')



@app.route('/ppt')
def ppt():
    return render_template('ppt.html')

@app.route('/photography')
def photo():
    return render_template('photography.html')


@app.route('/stress_interview')
def strinv():
    return render_template('stress_interview.html')

@app.route('/gamming')
def gamming():
    return render_template('gamming.html')




if __name__=='__main__':
    app.run(debug=True)