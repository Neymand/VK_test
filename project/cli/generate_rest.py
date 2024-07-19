import main

file_js = r'C:\Users\super\Python_project\VK_project_1\VK_processing_JSON\project\rest\models\shim.json'
file_output = r'C:\Users\super\Python_project\VK_project_1\VK_processing_JSON\project\rest\routes\engine\models.py'

a = main.Rest_gen(file_js, file_output)

a.open_js_file()
a.create_controller_file()