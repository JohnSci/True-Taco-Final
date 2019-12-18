import docx, requests      # These are the libraries that are used in the files to create them in Python


'''Down here, I will create the function that will get the taco API and find the specific parts to 
take to the Word Document that will be created.'''

def recipe_print():



    data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()    # This is the API where I get the random taco recipes
    seasoning_data = data["seasoning"]['recipe']    # Gathering the data for the seasoning
    seasoning_name = data["seasoning"]['name']      # This is where I get just the name for the seasoning
    condiment_data = data['condiment']['recipe']    # Gathering data for the condiments
    condiment_name = data['condiment']['name']      # Getting the name of the condiments
    mixin_data = data['mixin']['recipe']            # This is data for the mixing
    mixin_name = data['mixin']['name']              # This is just the name for the mixin
    base_layer_data = data['base_layer']['recipe']  # This is the data for the base layer
    base_name = data['base_layer']['name']          # This is the name for the base layer
    shell_data = data['shell']['recipe']            # Gathering data for the shell
    shell_name = data['shell']['name']              # This is where I get the name of the shell

    # This is where the document is made and where I piece each thing together
    document = docx.Document()
    document.add_paragraph('Random Taco Cookbook', 'Title')     # That is the name of the taco cookbook
    document.add_picture('Omega Tacos.jpg')     # This is my edited image I received from Unsplash
    document.add_paragraph('Picture by: Jason Leung')   # Citing the photographer of the image
    document.add_paragraph('Recipes found at: https://taco-1150.herokuapp.com/random/?full_taco=true')  # Citing the API that creates the recipes
    document.add_paragraph('Code created by: Paul Snowdey Jr.')
    document.add_page_break()       # This is where the recipes will start
    document.add_paragraph(seasoning_name, 'Title')
    document.add_paragraph(seasoning_data)
    document.add_paragraph(mixin_name, 'Title')
    document.add_paragraph(mixin_data)
    document.add_paragraph(base_name, 'Title')
    document.add_paragraph(base_layer_data)
    document.add_paragraph(shell_name, 'Title')
    document.add_paragraph(shell_data)
    document.add_page_break()
    document.add_paragraph


    document.save('TacoFinish.docx')

for taco in range(3):
    recipe_print()
