import requests

BASE_URL = 'http://127.0.0.1:5000'

# testing for get all resources
def test_get_resources():
    response = requests.get(f'{BASE_URL}/resources')
    assert response.status_code == 200
    assert isinstance(response.json(),dict)


# testing for get resource by id
def test_get_resource_by_id():
    response = requests.get(f'{BASE_URL}/resources/1')
    assert response.status_code == 200
    #data validation test
    assert 'name' in response.json()
    assert 'type' in response.json()


# testing for get resource by id not found
def test_get_resource_by_id_not_found():
    response = requests.get(f'{BASE_URL}/resources/500')
    assert response.status_code == 404
    assert response.json() == {"error": "Resource not found"}

# testing for auth
def test_get_secure_resource():
    headers = {'Authorization': 'Bearer valid_token'}
    response = requests.get(f'{BASE_URL}/secure-resource',headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Secure Resource"
}
    
 # testing for auth with no token
def test_get_secure_resource_fail():
    response = requests.get(f'{BASE_URL}/secure-resource')
    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"
}
    

# testing for xml content
def test_xml_content():
    response = requests.get(f'{BASE_URL}/xml-resource')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/xml'
    assert response.text.startswith('<resource>')