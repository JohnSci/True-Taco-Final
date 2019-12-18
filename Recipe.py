import docx, requests      # These are the libraries that are used in the files to create them in Python


'''Down here, I will create the function that will get the taco API and find the specific parts to 
take to the Word Document that will be created.'''

def recipe_print():



    data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()    # This is the API where I get the random taco recipes
    seasoning_data = data["seasoning"]['recipe']    #T This is where I get the
    seasoning_name = data["seasoning"]['name']
    condiment_data = data['condiment']['recipe']
    condiment_name = data['condiment']['name']
    mixin_data = data['mixin']['recipe']
    mixin_name = data['mixin']['name']
    base_layer_data = data['base_layer']['recipe']
    base_name = data['base_layer']['name']
    shell_data = data['shell']['recipe']
    shell_name = data['shell']['name']


    document = docx.Document()
    document.add_paragraph('Random Taco Cookbook', 'Title')
    document.add_picture('Omega Tacos.jpg')
    document.add_paragraph('Picture by: Jason Leung')
    document.add_paragraph('Recipes found at: https://taco-1150.herokuapp.com/random/?full_taco=true')
    document.add_paragraph('Code created by: Paul Snowdey Jr.')
    document.add_page_break()
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

recipe_print()
