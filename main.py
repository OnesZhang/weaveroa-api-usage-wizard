# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from api_list import APIList
from prompt_generator import PromptGenerator

app = Flask(__name__)
api_list = APIList()
prompt_generator = PromptGenerator()


@app.route("/", methods=["GET"])
def index():
    apis = api_list.get_apis()
    return render_template("index.html", apis=apis)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500


@app.route("/generate-prompt", methods=["POST"])
def generate_prompt():
    payload = request.get_json()
    selected_api_names = payload.get("selectedAPIs", [])
    requirements = payload.get("requirements", "")

    selected_apis = api_list.get_selected_apis(selected_api_names)

    prompt_template = prompt_generator.generate_prompt_template(selected_apis, requirements)

    response = {"promptTemplate": prompt_template}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="localhost", port=8000)
