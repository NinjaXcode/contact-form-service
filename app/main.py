from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Received message from {name} ({email}): {message}")
        return "Message sent successfully!"
    return '''
        <form method="POST">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            Message:<br><textarea name="message"></textarea><br>
            <input type="submit" value="Send">
        </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)