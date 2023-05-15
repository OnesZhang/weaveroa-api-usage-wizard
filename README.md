# weaveroa-api-usage-wizard
"WeaverOA Question Wizard for how to use api"
# WeaverOA API 使用向导

WeaverOA API 使用向导是一个旨在利用 ChatGPT 强大的语言模型简化生成 API 使用问题模板的过程的项目。

## 项目概述

WeaverOA API 使用向导允许开发者基于选择的 API 和特定需求生成问题模板。通过利用 ChatGPT 的能力，该项目自动化生成问题模板的过程，减少了手动工作的工作量。

项目包括以下组件：
- `templates` 目录：包含用户界面的 HTML 模板。
- `APIList.json`：包含 API 数据的 JSON 文件。
- `api_list.py`：处理 API 数据的 Python 模块。
- `favicon.ico`：Web 应用程序的图标文件。
- `main.py`：运行 Flask Web 应用程序的 Python 脚本。
- `prompt_generator.py`：使用 ChatGPT 生成问题模板的 Python 模块。
- `template_engine.py`：用于渲染 HTML 模板的 Python 模块。
- `user_interface.py`：处理用户交互和 API 请求的 Python 模块。

## 使用方法

1. 运行 `pip install -r requirements.txt` 安装所需的依赖项。
2. 修改 `APIList.json` 文件，包含您所需的 API 数据。
3. 执行 `python main.py` 运行 Flask Web 应用程序。
4. 在 Web 浏览器中访问 `http://localhost:8000` 来访问应用程序。
5. 选择所需的 API，指定需求，并单击“生成问题模板”按钮。
6. 生成的问题模板将显示在“ChatGPT 问题模板”部分。

## 自定义

您可以通过修改 `APIList.json` 文件中的 API 数据来自定义项目。根据需要添加、删除或编辑 API 条目。

您还可以通过修改 `prompt_generator.py` 模块中的逻辑来自定义生成的问题模板。调整模板生成过程以满足特定需求。

## 错误处理

项目包含错误处理，以确保用户体验的顺畅。如果发生任何错误，将向用户显示相应的错误消息。

## 致谢

本项目利用了由 OpenAI 开发的强大语言模型 ChatGPT，以及 Flask、HTML、JavaScript 和其他工具和技术。我们要感谢 OpenAI 提供先进的语言模型和技术，以及 Flask 和其他开源项目的贡献者和维护者。这些工具和技术使得该项目成为可能，提升了开发者和用户的体验和效率。

如果您有任何问题、建议或反馈，请随时与我们联系。感谢您的支持和使用！

---
*注意：本项目是基于 ChatGPT 生成模型的原型开发，它根据提供的输入生成输出。生成的问题模板可能不完全准确或与特定需求一致。在实际应用中，建议验证和调整生成的模板，以确保其适用性和准确性。


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
