from flask import Flask, request
app = Flask(__name__)

@app.route('/hello-json')
def index2():
    return '{"text": "Hello World from Dictionary"}'

@app.route('/hello-html')
def index3():
    return "<h1>Hello World</h1><p>Subtext</p>"

@app.route('/hello-html-error')
def index4():
    return ("<h1>Hello World</h1><p>Subtext</p>", 404)

@app.route('/hello/<name>')
def whatevername(name):
   return 'Hello ' + str(name)

@app.route('/hello/<name>/change/<value>') 
def whatevername2(name, value):
    return 'Hello' + str(name) + ", your change is " + str((int(value) - 10))

@app.route('/hello')
def index133():
    if ('name' in request.args):
        return 'Hello ' + request.args['name']
    else:
        return 'Hello World'

@app.route('/reflect', methods = ['POST', 'GET'])
def reflect():
    x = request.data.decode()
    return 'Hello ' + str(x)


@app.route('/reflect/plex', methods = ['POST', 'GET'])
def reflect2():
    payload = request.json
    dict2 = {}
    for i in payload:
        dict2["plex_" + i] = payload[i]
    return dict2



    





app.run(host='0.0.0.0', port=81, debug = True)
