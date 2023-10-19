from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul>
      <li><a href="/animals/dogs">Dogs</a></li>
      <li><a href="/animals/cats">Cats</a></li>
      <li><a href="/animals/rabbits"</a>Rabbits</a></li>
    </ul>
  '''
  for pet in pets:
    print(pet)

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html=f'''
  <h1>List of {pet_type}</h1>
  '''
  html+="<ul>"
  for idx, item in enumerate(pets[pet_type]):
    html += "<li>" + f'<a href="/animals/{pet_type}/{idx}">' + item["name"] + "</a></li>"
  html += "</ul>"
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  pet_dict = {
    "name" : pet["name"],
    "src" : pet["url"],
    "description" : pet["description"],
    "breed" : pet["breed"],
    "age" : pet["age"]
  }

  return f'''
    <h1>{pet_dict["name"]}</h1>
    <p><img src={pet_dict["src"]}></p>
    <p>{pet_dict["description"]}</p>
    <ul>
      <li>Breed: {pet_dict["breed"]}</li>
      <li>Age: {pet_dict["age"]}</li>
    </ul>'''

    

