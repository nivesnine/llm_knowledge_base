import json
from vendors.vendor_getter import VendorGetter


class Validator:
    def __init__(self):
        pass

    def get_validation_prompts(self, valdation_file):
        with open(valdation_file, 'r') as f:
            validation_prompts = json.load(f)
        return validation_prompts

    def validate(self, vendor, model_name, response, valdation_file, throttle):
        # create a dictionary to store the headers and results
        results_dict = {}
        # return format = {"header": "result", "header": "result"}
        # load the validation prompts
        validation_prompts = self.get_validation_prompts(valdation_file)

        # iterate through the validation prompts
        for header, prompt in validation_prompts.items():
            prompt = prompt + ":\n\n" + response
            result = vendor.run(prompt, model_name)
            results_dict[header] = result
            if throttle > 0:
                import time
                time.sleep(throttle)

        formated_validation_result = ""
        for key, value in results_dict.items():
            formated_validation_result += (f"- **{key}**: {value}\n")

        return formated_validation_result
