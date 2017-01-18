# example_module_upload.py - show usage of gauss.py 

import gauss, commands

api_path = "http://insert.api/path/for/upload"
apikey = "insertYourAPIKeyHere"

# example 1 - console output of module command 
module_list = commands.getoutput("module available -t")
modules = gauss.parse_module_list(module_list)

# example 2 - read input from file:
modules = gauss.parse_module_list_file("/path/to/file/that/contains/output/of/moduleAvailable-t/command")

# initiate upload providing apikey, api_path, modules
# delete_old_modules option is set to 1
response = gauss.module_upload(apikey, modules, api_path, 1)

# print response or write response to logfile
print(response.status_code)
print(response.text)
