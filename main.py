from flask import Flask, request, abort
import string, secrets, json


app = Flask(__name__)

def generate_random_password(length, lowercase, uppercase, digits):
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (
                sum(c.islower() for c in password) >= lowercase
                and sum(c.isupper() for c in password) >= uppercase
                and sum(c.isdigit() for c in password) >= digits
            ):
            break
    result = {
        "password": password   
    }
    return(json.dumps(result))

@app.route("/")
def help():
    return "Operation not implemented. Your request has been logged."
    

@app.route("/generate-password")
def generate_password():
    try:
        length = int(request.args.get('length'))
        lowercase = int(request.args.get('lowercase'))
        uppercase = int(request.args.get('uppercase'))
        digits = int(request.args.get('digits'))
      
    except:
        abort(500)

    #Enforce password policy
    if ((length < 20) or (lowercase < 10) or (uppercase < 10) or (digits < 10)):
        print(f'bad password policy!')
        abort(403)
    else:
        try:
            return(generate_random_password(length, lowercase, uppercase, digits))
        except:
            abort(500)
    

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")