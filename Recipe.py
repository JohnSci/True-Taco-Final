import docx, requests      # These are the libraries that are used in the files to create them in Python


'''Down here, I will create the function that will get the taco API and find the specific parts to 
take to the Word Document that will be created.'''

def recipe_print():

    data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()    # This is the API where I get the random taco recipes
    seasoning_data = data['seasoning']
    condiment_data = data['condiment']
    mixin_data = data['mixin']
    base_layer_data = data['base_layer']
    shell_data = data['shell']
    document = docx.Document()
    document.add_paragraph('Random Taco Cookbook', 'Title')
    document.add_picture('Omega Taco.jpg', width=docx.shared.Inches(3), height=docx.shared.Inches(3))
    document.add_paragraph('Picture by: Jason Leung')


    document.save('TacoFinish.docx')

recipe_print()

