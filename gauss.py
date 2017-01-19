# gauss.py - python module to connect to module uplod api
import json, requests

def module_upload(apikey, modules, api_path, delete_old_modules):
    data = {
        "apikey": apikey,
        "delete_old_applications": delete_old_modules,
        "applications": modules
    }
    
    headers = {'X-Requested-With': 'XMLHttpRequest'}

    return requests.post(api_path, data = json.dumps(data), headers=headers)

# parse_module_list expects a module list generated
# by the command: "module available -t"
# Expected format: "module_name/version"
def parse_module_list(module_list):
    modules = []

    for line in module_list.split("\n"):
        # convention: module name starts with a-zA-Z
        # skip all others
        if line and line[0].isalpha():
            name = line.split("/", 1)[0]
            # check if version information exists and
            # only add module in that case
            if len(line.split("/", 1)) == 2:
                version = line.split("/", 1)[1]
                modules.append(
                    {
                        "name": name,
                        "version": version
                    }
                )

    return modules

# parse_module_file expects a file with a module list generated
# by the command: "module available -t"
# Expected format: "module_name/version"
def parse_module_list_file(module_file):
    modules = []

    # open module file
    with open(module_file) as f:
        content = f.read()

    return parse_module_list(content)
