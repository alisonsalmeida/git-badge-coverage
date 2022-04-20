import os

from sanic import Sanic, response
from sanic.request import Request

import requests


app = Sanic(__name__)


@app.get('/code-check')
async def get_lint(request: Request):
    lint = request.args['lint'][0] if 'lint' in request.args else 0
    lint = float(lint)

    style = request.args['style'][0] if 'style' in request.args else 'for-the-badge'
    color = None

    if lint < 2:
        color = 'red'

    elif 2 <= lint < 4:
        color = 'orange'

    elif 4 <= lint < 6:
        color = 'yellow'

    elif 6 <= lint < 8:
        color = 'yellowgreen'

    elif 8 <= lint < 9:
        color = 'green'

    else:
        color = 'brightgreen'

    url = f'https://img.shields.io/badge/linting-{lint}-{color}?style={style}'
    req = requests.get(url)
    return response.raw(body=req.content.decode(), content_type='image/svg+xml;charset=utf-8')


@app.get('/code-coverage')
async def get_coverage(request: Request):
    coverage = request.args['coverage'][0] if 'coverage' in request.args else 0
    coverage = int(coverage)

    style = request.args['style'][0] if 'style' in request.args else 'for-the-badge'
    color = None

    if coverage < 20:
        color = 'red'

    elif 20 <= coverage < 40:
        color = 'orange'

    elif 40 <= coverage < 60:
        color = 'yellow'

    elif 60 <= coverage < 80:
        color = 'yellowgreen'

    elif 80 <= coverage < 99:
        color = 'green'

    else:
        color = 'brightgreen'

    url = f'https://img.shields.io/badge/codecov-{coverage}%25-{color}?logo=codecov&style={style}'
    req = requests.get(url)
    return response.raw(body=req.content.decode(), content_type='image/svg+xml;charset=utf-8')


if __name__ == '__main__':
    port = os.environ.get('PORT', None) or 3000
    port = int(port)

    app.run(host='0.0.0.0', port=port)
