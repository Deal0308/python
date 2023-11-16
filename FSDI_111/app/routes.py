from flask import Flask  

# OOP

app = Flask(__name__)           # create an app instance

@app.get('/')                    # at the end point /
def index():                        # call method hello
    me ={                           
        "first_name": "Michael",
        "last_name": "Deal",
        "hobbies": "Bodybuilding",
        "is_active": True,
    
    }
    return me

