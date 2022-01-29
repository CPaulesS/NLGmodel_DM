from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin
from keras import backend as K
import gpt_2_simple as gpt2
import message_formatter as mf

K.clear_session()

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api',methods=['POST'])
@cross_origin()
def generate_response():
    data = request.get_json(force=True)
    message_received = mf.check_punctuation(data['message'])
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)
    text_generated = gpt2.generate(sess,
                  length=150,
                  temperature=0.7,
                  model_name='124M',
                  prefix=message_received,
                  nsamples=1,
                  batch_size=1,
                  truncate='.',
                  include_prefix=False,
                  return_as_list=True
                  )
    response_generated = mf.correct_response(text_generated[0])
    K.clear_session()
    return jsonify(response=response_generated)

if __name__ == '__main__':
    app.run(port=9000, debug=True)