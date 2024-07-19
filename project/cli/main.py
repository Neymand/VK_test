import json
from pydantic import BaseModel, Field, EmailStr

class Parsing:
    """
    Парсинг JSON
    Создание Pydentic
    """

    def __init__(self, js, save):
        self.rout_js = js
        self.rout_save = save

    def open_js_file(self):
        with open(self.rout_js, "r") as f:
            self.rout_js = json.load(f)

    def parse_json_schema(self):
        model_name = self.rout_js.get("title", "GeneratedModel").replace(' ', '_')
        properties = self.rout_js.get("properties", {})
        required = self.rout_js.get("required", [])

        fields = []
        for field, field_info in properties.items():
            field_type = self.convert_type(field_info.get("type"))
            default = None if field in required else Field(None)
            fields.append(f"{field}: {field_type} = {default}")

        model_definition = f"from pydantic import BaseModel\n\nclass {model_name}(BaseModel):\n"
        if fields:
            model_definition += "\n    ".join([""] + fields)
        else:
            model_definition += "    pass"

        with open(self.rout_save, "w") as f:
            self.rout_save = f.write(model_definition)

        print("Final geherate pydantic")



    def convert_type(self, json_type):
        type_mapping = {
            "string": "str",
            "integer": "int",
            "boolean": "bool",
            "number": "float",
            "array": "list",
            "object": "dict"
        }
        return type_mapping.get(json_type, "Any")




class Pars_rest(Parsing):
    """
    Парсинг JSON
    Создание REST файла
    """

    def create_controller_file(self):
        model_name = self.rout_js['title'].replace(' ', '_')
        attributes = self.rout_js['properties']

        # Начало файла
        content = f"""from fastapi import FastAPI, HTTPException\nfrom pydantic import BaseModel

app = FastAPI()
_fake_db = []
class {model_name}(BaseModel):\n
"""

        for attr, attr_props in attributes.items():
            attr_props = self.convert_type(attr_props['type'])
            content += f"    {attr}: {attr_props}\n"

        # Создание фейковой базы данных и endpoint-ов
        content += f"""
@app.post("/{model_name.lower()}/", response_model={model_name})
def create_{model_name.lower()}(item: {model_name}):
    _fake_db.append(item)
    return item

@app.get("/{model_name.lower()}/{{item_id}}", response_model={model_name})
def read_{model_name.lower()}(item_id: int):
    if item_id >= len(_fake_db) or item_id < 0:
        raise HTTPException(status_code=404, detail="{model_name} not found")
    return _fake_db[item_id]
        """

        with open(self.rout_save, "w") as f:
            self.rout_save = f.write(content)

        print("Final generate REST")