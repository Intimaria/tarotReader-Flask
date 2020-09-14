from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from Tarot import Spread

app = Flask(__name__)
app.config["SECRET_KEY"] = "what.does.the.future.hold"

class TarotForm(FlaskForm):
  comment = StringField("Concentrate and ask the oracle a meaningful question:")
  submit = SubmitField("Throw Cards")
  
  
@app.route('/', methods=["GET", "POST"])
def index():
  spread_form = TarotForm()
  new_question = spread_form.comment.data
  my_reading = Spread()
  my_reading.question[0] = new_question
  new_reading = my_reading.get_spread()
  return render_template('index.html', 
                          form=spread_form, 
                          question= my_reading.question[0], 
                          spread_reading=new_reading)
if __name__ == '__main__':
  app.run(debug=True)

