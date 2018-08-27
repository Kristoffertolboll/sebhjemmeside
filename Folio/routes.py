from flask import Flask
from flask import render_template, request, flash, session, url_for, redirect


app = Flask(__name__)



mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'kristofferlocktolboll@gmail.com',
    "MAIL_PASSWORD": 'Magnumsniper123'
}



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mail', methods=['GET', 'POST'])
def send_mail():
    r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                          data = {'secret' :
                                  '6Ldj2GcUAAAAAPKmauoHuu6WvLzL97mWfPVQcnzS',
                                  'response' :
                                  request.form['g-recaptcha-response']})
    google_response = json.loads(r.text)
    print('JSON: ', google_response)

    name = request.form['name']
    message = request.form['message']
    

    html = render_template('email.html', name=name)
    if google_response['success']:
    	html = render_template('email.html', name=name)
        msg = Message('Thank you for contacting me', sender='kristofferlocktolboll@gmail.com', recipients=[request.form['email']], html=html)
        mail.send(msg)
        msg1 = Message( 
        	'Ny besked fra' + name + ' ',
        	sender = 'kristofferlocktolboll@gmail.com',
        	recipients = ['kristofferlocktolboll@gmail.com'],
        	body = 'Ny besked fra: ' + name + '\n med Ip Adressen: ' + request.remote_addr + '\n Beskedens tekst:  ' + message + ' ') 
        mail.send(msg1)
        return render_template('index.html')
    else:
        return render_template('index.html')








app.run(debug=True)