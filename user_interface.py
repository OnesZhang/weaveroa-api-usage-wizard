from api_list import APIList
from prompt_generator import PromptGenerator

class UserInterface:
    def __init__(self):
        self.api_list = APIList()  # 实例化API列表
        self.prompt_generator = PromptGenerator()  # 实例化Prompt生成器

    def display_api_selection(self):
        print("Available APIs:")
        apis = self.api_list.get_apis()
        for i, api in enumerate(apis):
            print(f"{i + 1}. {api['name']} - {api['description']}")

    def get_selected_apis(self):
        selected_apis = []
        while True:
            self.display_api_selection()
            choice = input("Enter the number of the API you want to select (or 'done' to finish): ")
            if choice.lower() == 'done':
                break
            try:
                choice = int(choice)
                apis = self.api_list.get_apis()
                if 1 <= choice <= len(apis):
                    selected_apis.append(apis[choice - 1])
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid choice. Please try again.")
        return selected_apis

    def get_user_requirements(self):
        requirements = input("Please describe your requirements: ")
        return requirements

    def display_prompt_template(self, prompt_template):
        print("Generated Prompt Template:")
        print(prompt_template)

    def run(self):
        selected_apis = self.get_selected_apis()
        requirements = self.get_user_requirements()
        prompt_template = self.prompt_generator.generate_prompt_template(selected_apis, requirements)
        self.display_prompt_template(prompt_template)

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
