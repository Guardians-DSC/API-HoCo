from flask import jsonify

def input_not_given(valid_params):
    return jsonify(f'Parameters required: {valid_params}')
