# weaveroa-api-usage-wizard
"WeaverOA Question Wizard for how to use api"
# WeaverOA API Usage Wizard

The WeaverOA API Usage Wizard is a project aimed at simplifying the process of generating API usage question templates using the power of ChatGPT, a state-of-the-art language model developed by OpenAI.

## Project Overview

The WeaverOA API Usage Wizard allows developers to generate question templates for API usage based on their selected APIs and specific requirements. By leveraging the capabilities of ChatGPT, the project automates the process of generating question templates, reducing the manual effort required.

The project consists of the following components:
- `templates` directory: Contains HTML templates for the user interface.
- `APIList.json`: JSON file containing the API data.
- `api_list.py`: Python module for handling API data.
- `favicon.ico`: Icon file for the web application.
- `main.py`: Python script for running the Flask web application.
- `prompt_generator.py`: Python module for generating question templates using ChatGPT.
- `template_engine.py`: Python module for rendering HTML templates.
- `user_interface.py`: Python module for handling user interactions and API requests.

## Usage

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Modify the `APIList.json` file to include your desired API data.
3. Run the Flask web application by executing `python main.py`.
4. Access the application in your web browser at `http://localhost:8000`.
5. Select the desired APIs, specify the requirements, and click on the "Generate Prompt" button.
6. The generated question template will be displayed in the "ChatGPT Question Template" section.

## Customization

You can customize the project by modifying the API data in the `APIList.json` file. Add, remove, or edit API entries according to your needs.

You can also customize the generated question template by modifying the logic in the `prompt_generator.py` module. Adjust the template generation process to suit your specific requirements.

## Error Handling

The project includes error handling to ensure a smooth user experience. If any errors occur, an appropriate error message will be displayed to the user.

## Acknowledgements

This project utilizes the powerful language model ChatGPT developed by OpenAI, as well as Flask, HTML, JavaScript, and other tools and technologies. We would like to express our gratitude to OpenAI for providing advanced language models and technologies, as well as to the contributors and maintainers of Flask and other open-source projects. These tools and technologies make this project possible and enhance the experience and efficiency for developers and users.

If you have any questions, suggestions, or feedback, please feel free to contact us. Thank you for your support and usage!

---
*Note: This project is a prototype development based on the ChatGPT generative model, which generates output based on the provided input. The generated question templates may not be entirely accurate or aligned with specific requirements. In real-world applications, it is recommended to validate and adjust the generated templates to ensure their suitability and accuracy.*
