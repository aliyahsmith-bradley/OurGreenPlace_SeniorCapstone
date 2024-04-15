from website.userModels import User

# Test routes within website 
def test_home(client):
    response = client.get("/")
    assert b"<title>Home</title>" in response.data 

def test_explore(client):
    response = client.get("/explore")
    assert b"<title>Explore</title>" in response.data 

def test_deforestation(client):
    response = client.get("/deforestationInMD")
    assert b"<title>Deforestation in MD</title>" in response.data 

def test_featured(client):
    response = client.get("/featuredContent")
    assert b"<title>Featured Content Page</title>" in response.data

def test_howToHelp(client):
    response = client.get("/howToHelp")
    assert b"<title>How To Help</title>" in response.data 

def test_map(client):
    response = client.get("/map")
    assert b"<title>Green Space Map</title>" in response.data

def test_stat(client):
    response = client.get("/statistics")
    assert b"<title>Statistics</title>" in response.data

# Test Sign Up Page  
def test_signup(client, app):
    response = client.post(
        "/signup", 
        data={
            "firstName": "Jane", 
            "lastName": "Doe", 
            "email": "janedoe@gmail.com", 
            "username": "janedoeee", 
            "password": "12345678", 
            "passwordConfirmation": "12345678"
            }
    )

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().firstName == "Jane"

# Tests Login Page 
def test_login(client):
    client.post(
        "/signup", 
        data={
            "firstName": "Jane", 
            "lastName": "Doe", 
            "email": "janedoe@gmail.com", 
            "username": "janedoeee", 
            "password": "12345678", 
            "passwordConfirmation": "12345678"
            }
    )

    client.post(
        "/login", 
        data={ 
            "email": "janedoe@gmail.com",  
            "password": "12345678", 
            }
    )

    response = client.get("/explore")

    assert response.status_code == 200 

