import requests, docx


def recipe_print():

    data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
    seasoning_data = data['seasoning']
    condiment_data = data['condiment']
    mixin_data = data['mixin']
    base_layer_data = data['base_layer']
    shell_data = data['shell']
    document = docx.Document('Random Taco Cookbook')
    document.add_paragraph(seasoning_data)
    document.save('Taco Final')


    for book in range(3):
        recipe_print()
