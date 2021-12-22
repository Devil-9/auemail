import smtplib
import random
from flask import request
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/otp", methods=["POST"])
def otp():
    email = request.form.get("email")
    pasw = 'dciqxxrmqypqezns'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        ran = random.randint(100000, 1000000)
        smtp.starttls()
        smtp.ehlo()
        smtp.login("avnishraj2812@gmail.com", pasw)
        subject = 'OTP VERIFICATION BY Rent Mech'
        body = f'Your one time verification password is {ran}'
        msg = f'Subject: {subject}\n\n\n {body}'
        smtp.sendmail('lcs2019075@iiitl.ac.in', email, msg)
    
    response = {'otp': ran}
    return jsonify(response), 200

#app.run(host = '0.0.0.0', port = 5000)
