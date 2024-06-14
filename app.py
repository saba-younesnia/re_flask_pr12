from flask import *
import sqlite3

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name=request.form.get('name')
        db=sqlite3.connect('db1.db')
        result=db.execute("SELECT * FROM students")
        data=result.fetchall()
        names = []
        for mytuple in data:
            n = mytuple[1] + '_' + mytuple[2]
            if n==name:
                avg_score=(float(mytuple[3])+float(mytuple[4])+float(mytuple[5]))/3
            names.append(n)
        return render_template('index.html',names=names,name=name,avg_score=avg_score)
    else:
        db=sqlite3.connect('db1.db')
        result=db.execute("SELECT * FROM students")
        data=result.fetchall()
        names=[]
        for mytuple in data:
            n=mytuple[1]+'_'+mytuple[2]
            names.append(n)
        return render_template('index.html',names=names)
if __name__ == '__main__':
    app.run()
