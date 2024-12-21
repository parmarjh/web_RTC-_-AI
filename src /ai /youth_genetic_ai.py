class YouthGeneticAI:
    def __init__(self):
        self.prompts = [
            "What are the potential genetic traits of youth?",
            "How does genetics influence youth behavior?",
            "What role do genes play in youth development?",
            "How can genetic information impact youth health?",
            "What are the ethical considerations of genetic testing in youth?"
        ]

    def generate_prompt(self):
        import random
        return random.choice(self.prompts)

    def add_prompt(self, prompt):
        if prompt not in self.prompts:
            self.prompts.append(prompt)

    def remove_prompt(self, prompt):
        if prompt in self.prompts:
            self.prompts.remove(prompt)

    def list_prompts(self):
        return self.prompts.copy()
