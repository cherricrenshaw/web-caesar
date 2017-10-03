from flask import Flask, request 
from caesar import rotate_string

app=Flask( __name__ )
app.config ["DEBUG"]=True

form ="""

<!DOCTYPE html>



<html>

    <head>

        <style>

            form {{

                background-color: #eee;

                padding: 20px;

                margin: 0 auto;

                width: 540px;

                font: 16px sans-serif;

                border-radius: 10px;

            }}

            textarea {{

                margin: 10px 0;

                width: 540px;

                height: 120px;

            }}

            

        </style>

    </head>

    <body>

      <form method="POST" action="/encrypt">

        <label for="rot">Rotate by:</label>

        <input type="text" name="rot" id="rot" placeholder="0">

        <textarea name="text" id="text">{0}</textarea>

        <input type="submit">

      </form>

    </body>

</html>

"""

@app.route("/")

def index():
    return form.format("")

@app.route("/encrypt",methods=['POST'])
def encrypt():
    rot=request.form["rot"]
    text=request.form["text"]

    new= rotate_string(text,int(rot))
    return form.format(new)

app.run ()

