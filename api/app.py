from flask import Flask,render_template,request,redirect,session
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField,FloatField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange


app = Flask(__name__,template_folder="templates")
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "xQlduscds"

class EnterYourInfos(FlaskForm):
    F1= FloatField("intercolumnar distance :",validators=[NumberRange(-5,30)])
    F2= FloatField("upper margin :",validators=[NumberRange(-5,30)])
    F3= FloatField("lower margin :",validators=[NumberRange(-5,30)])
    F4= FloatField("exploitation :",validators=[NumberRange(-5,30)])
    F5= FloatField("row number:",validators=[NumberRange(-5,30)])
    F6= FloatField("modular ratio :",validators=[NumberRange(-5,30)])
    F7= FloatField("interlinear spacing :",validators=[NumberRange(-5,30)])
    F8= FloatField("weight :",validators=[NumberRange(-5,30)])
    F9= FloatField("peak number :",validators=[NumberRange(-5,30)])
    F10= FloatField("modular ration/interlinear spacing :",validators=[NumberRange(-5,30)])
    submit = SubmitField("Submit")
   

class Try(FlaskForm):
    submit = SubmitField("Try Again With  new value")

@app.route('/', methods=["GET","POST"])
def index():
    form = EnterYourInfos()
    if request.method == "POST" and form.validate_on_submit():
        import joblib
        model = joblib.load("finalized_model.sav")
        pred = model.predict([[form.F1.data, form.F2.data,form.F3.data,form.F4.data,form.F5.data,form.F6.data,form.F7.data,form.F8.data,form.F9.data,form.F10.data]])
        session["result"]=pred.tolist()
        return redirect("/results") 
    return render_template('base.html',form=form)



@app.route("/results",methods=["GET","POST"])
def show_result():
    pred = session['result']
    form = Try()
    if request.method == 'POST' and form.validate_on_submit:
        return redirect('/')
    return render_template("result.html",prediction = pred,form=form)


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)


