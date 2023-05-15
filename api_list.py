# -*- coding: utf-8 -*-

import json

class APIList:
    def __init__(self):
        with open('APIList.json', encoding='utf-8') as file:
            self.apis = json.load(file)

    def get_apis(self):
        return self.apis

    def get_selected_apis(self, selected_api_names):
        selected_apis = []
        for category in self.apis:
            for subcategory in category.get("subcategories", []):
                for api in subcategory.get("apis", []):
                    if api["name"] in selected_api_names:
                        selected_apis.append(api)
        return selected_apis
