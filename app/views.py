from helpers import render_to_template, render_to_json

@render_to_json
#@render_to_template('index.html')
def index(request):
    return {'body': 'index'}

def post(request, post_id):
    return {
        'body': 'post',
        'id': post_id,
    }

