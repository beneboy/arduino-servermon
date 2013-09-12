from flask import Flask, render_template, request, redirect
from do_serial import ser
app = Flask(__name__)

red = 0
green = 0
blue = 0

@app.route("/")
def index():
    return render_template('base.html', red=red, green=green, blue=blue)


@app.route("/applycolour/", methods=['POST',])
def apply_colour():
    red = min(int(request.form['red']), 255)
    green = min(int(request.form['green']), 255)
    blue = min(int(request.form['blue']), 255)

    ser.write(chr(red))
    ser.write(chr(green))
    ser.write(chr(blue))
    print "Done sending"
    print ser.readline(),
    print ser.readline(),
    print ser.readline(),
    return redirect('/')



if __name__ == "__main__":
    app.run(host='0.0.0.0')
