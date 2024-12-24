from flask import Flask

#Creating a flask app instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, DK'
    

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
    app.run(port=5000)
    app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, processes=3)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, processes=3, use_reloader=False)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, processes=3, use_reloader=False, use_evalex=False)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, processes=3, use_reloader=False, use_evalex=False, use_debugger=False)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, processes=3, use_reloader=False, use_evalex=False, use_debugger=False, use_reloader_reloader=False)

