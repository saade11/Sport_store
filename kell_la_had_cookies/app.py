# from flask import Flask, request,flash, make_response, render_template, redirect, url_for, Response, send_from_directory, jsonify, session
# import pandas as pd
# import os
# import uuid
# #create the flask instance
# app = Flask(__name__, template_folder='templates') # this is here to tell flask where our files will be located 
# app.secret_key = 'SOME KEY'

# @app.route('/', methods= ['GET'])
# def index():
#     return render_template('index.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username == 'samer' and password == 'saade':
#             flash ('Login Successful ')
#             return render_template('index.html', message='')
#         else:
#             flash('Incorrect Username or Password')
#             return render_template('index.html', message='')
# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     if request.method == 'GET':
# #         return render_template('index.html')
# #     elif request.method == 'POST':
# #         username = request.form.get('username')
# #         password = request.form.get('password')
        
# #         if username == 'neuralline' and password == 'password':
# #             return "success"
# #         else:
# #             return "failure"
        
# # @app.route('/file_upload', methods=['POST'])
# # def file_upload():
# #     file = request.files['file']
# #     if file.content_type == 'text/plain':
# #         return file.read().decode()
# #     elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type=='application/vnd.ms-excel':
# #         df = pd.read_excel(file)
# #         return df.to_html()
    
# # @app.route('/convert_csv', methods=['POST'])
# # def convert_csv():
# #     file = request.files['file']
# #     df = pd.read_excel(file)
# #     response = Response(
# #         df.to_csv(),
# #         mimetype= 'text/csv',
# #         headers= {'Content-Disposition': 'attachement; filename=result.csv'} 
# #     )
# #     return response

# # @app.route('/convert_csv2', methods=['POST'])
# # def convert_csv2():
# #     file = request.files['file']
# #     df = pd.read_excel(file)
    
# #     if not os.path.exists('downloads'):
# #         os.makedirs('downloads')
    
# #     filename = f'{uuid.uuid4()}.csv'
# #     df.to_csv(os.path.join('downloads', filename))
    
# #     return render_template('downloads.html', filename=filename)
    
# # @app.route('/download/<filename>')
# # def download(filename):
# #     return send_from_directory('downloads', filename, download_name='result.csv')

# # @app.route('/handle_post', methods=['POST'])
# # def handle_post():
# #     greeting = request.json['greeting']
# #     name = request.json['name']
    
# #     with open('file.txt', 'w') as f:
# #         f.write(f'{greeting},{name}')
    
# #     return jsonify({'message':'Successfully written!'}) 
# # @app.route('/index', methods=['GET'])
# # def index():
# #     return render_template('index.html')

# # @app.route('/other', methods = ['GET'])
# # def other():
# #     return render_template('other.html')


# # @app.route('/redirect_endpoint')
# # def redirect_endpoint():
# #     return redirect(url_for('other'))
# # @app.route('/greet/<name>')
# # def grett(name):
# #     return f"Hello {name}"

# # @app.route('/hello', methods=['GET', 'POST'])
# # def hello():
#     # if request.method == 'GET':
#     #     return "you make a GET request"
#     # elif request.method == 'POST':
#     #     return "you made a POST request"
#     # else:
#     #     return "you didn't request correctly"
#     # response = make_response('hello world')
#     # response.status_code = 202
#     # #response.headers['content-type'] = 'application/octet-stream'
#     # return response

# # @app.route('/add/<number1>/<number2>')
# # def add(number1,number2):
# #     return f"{number1} + {number2} = {int(number1)+int(number2)}"

# # @app.route('/handle_url_params')
# # def handle_params():
# #     if 'greeting' in request.args.keys() and 'name' in request.args.keys():
# #         greeting = request.args.get('greeting')
# #         name = request.args.get('name')
# #         return f"{greeting}, {name}"
# #     else:
# #         return 'Parameter missing'
    
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=4444, debug=True)
    