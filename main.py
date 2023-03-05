from flask import Flask, request
from event_parser import meeting_details_parse

app = Flask(__name__)

@app.route('/parse',methods=['POST'])
def parse():
    return meeting_details_parse(request.json["message"],request.json["contact_list"])

if __name__=="__main__":
    app.run(port=5002,debug=True)