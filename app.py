from flask import Flask ,render_template,request
from model import get_bot_response

app = Flask(__name__)

def is_upi_query(user_input):
   user_input=user_input.lower()
   upi_keywords=["upi","payment","transaction","upi id","bhim","paytm","google pay","phonepe","gpay"]
   return any(keyword in user_input for keyword in upi_keywords)


@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        if is_upi_query(user_input):
         bot_response = get_bot_response(user_input)
        else:
           bot_response="sorry i can only assist with the UPI-related queries."


    return render_template("gui.html", user_input=user_input, bot_response=bot_response)

if __name__=="__main__":
  app.run(debug=True)
