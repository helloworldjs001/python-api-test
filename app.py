from flask import Flask, request, jsonify


app = Flask(__name__)

# Sample Dataset
resources = {
    1: {"name":"Resource 1" ,"type": "Type A"},
    2: {"name":"Resource 2" ,"type": "Type B"},
}


# get all resources
@app.route('/resources',methods=['GET'])
def get_resources():
    return jsonify(resources), 200



# get a single resource by id
@app.route('/resources/<int:resource_id>',methods=['GET'])
def get_resource(resource_id):
    resource = resources.get(resource_id)
    if resource:
        return jsonify(resource), 200
    else:
        return jsonify({"error": "Resource not found"}), 404
    

# auth route
@app.route('/secure-resource',methods=['GET'])
def get_secure_resource():
    auth_header = request.headers.get('Authorization')
    if auth_header == 'Bearer valid_token':
        return jsonify({"message": "Secure Resource"}), 200
    else:
        return jsonify({"error": "Unauthorized"}), 401



# xml data
@app.route('/xml-resource',methods=['GET'])
def get_xml_resource():
    response = """<resource>
                    <id>1</id>
                    <name>Resource 1</name>
                    <type>Type A</type>
                    </resource>"""
    return response, 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run(debug=True)