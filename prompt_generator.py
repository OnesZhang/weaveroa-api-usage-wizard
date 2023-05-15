class PromptGenerator:
    def __init__(self):
        self.template = "Hi，我需要你的帮助，现在为你提供以下API:\n\n"
        self.placeholder = "[DESCRIPTION]"

    def generate_prompt_template(self, selected_apis, user_requirements):
        prompt_template = self.template

        for api in selected_apis:
            prompt_template += f"- {api['name']}: {api['description']}\n"
            prompt_template += f"  - 说明: {api['parameters']}\n"

        prompt_template += f"\n我的要求如下:\n{user_requirements}\n"

        prompt_template += f"\n请使用其中一个或多个API实现以上要求，以代码块的形式解答，并添加必要的注释. 谢谢!"

        prompt_template = prompt_template.replace(self.placeholder, "")

        return prompt_template
