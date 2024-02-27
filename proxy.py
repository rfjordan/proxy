from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    url = request.url.replace(request.host_url, '')
    if request.method == 'GET':
        resp = requests.get(url)
    elif request.method == 'POST':
        resp = requests.post(url, data=request.form, files=request.files)
    headers = [(name, value) for name, value in resp.raw.headers.items()]
    return Response(resp.content, resp.status_code, headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
