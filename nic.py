from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! TEST</p>"

@app.route("/kotki")
def kotki():
    return "<p>Widze ze lubisz kotki</p>"

@app.route("/kotki/<ile>/<kolor>")
def kotkiile(ile, kolor):
    if kolor == "czarny":
        return "Brawo wygrałeś odwiedź moją stronę: https://niunek.github.io"
    elif int(ile) <= 10:
        return "<p>masz mniej niż 10 kotków</p>"
    else:
        return "<p>Masz więcej niż 10 kotków </p>" "twoja liczba to "+ ile + " twój kolor to " + kolor 
    
if __name__ == "__main__":
    app.run(debug=True)