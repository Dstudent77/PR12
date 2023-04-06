import requests

api_url = 'http://localhost:8000'

def test_healthcheck():
    response = requests.get(f'{api_url}/__health')
    assert response.status_code == 200

class TestDocuments():
    def test_get_empty_docs(self):
        response = requests.get(f'{api_url}/v1/docs')
        assert response.status_code == 200
        assert len(response.json()) == 0
        
    def test_create_doc(self):
        body = { "title": "New title", "body": "Prosto text" }
        response = requests.post(f'{api_url}/v1/docs', json=body)
        assert response.status_code == 200
        assert response.json().get('title') == 'New title'
        assert response.json().get('body') == 'Prosto text'
        assert response.json().get('id') == 0
    
    def test_get_doc_by_id(self):
        response = requests.get(f'{api_url}/v1/docs/0')
        assert response.status_code == 200
        assert response.json().get('title') == 'New title'
        assert response.json().get('body') == 'Prosto text'
        assert response.json().get('id') == 0
        
    def test_get_not_empty_docs(self):
        response = requests.get(f'{api_url}/v1/docs')
        assert response.status_code == 200
        assert len(response.json()) == 1