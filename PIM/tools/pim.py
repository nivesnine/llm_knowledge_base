import sys
import uuid
from validator import Validator
from vendors.vendor_getter import VendorGetter

if __name__ == "__main__":
    if "-i" in sys.argv:
        input_file = sys.argv[sys.argv.index("-i") + 1]
    else:
        input_file = '../tests/prompts.txt'

    if "-o" in sys.argv:
        output_file = sys.argv[sys.argv.index("-o") + 1]
    else:
        unique_filename = str(uuid.uuid4())
        output_file = '../results/' + unique_filename + '.md'

    if "-v" in sys.argv:
        vendor_name = VendorGetter().get_vendor(sys.argv[sys.argv.index("-v") + 1])
    else:
        vendor = VendorGetter().get_vendor("google")

    if "-m" in sys.argv:
        model_name = sys.argv[sys.argv.index("-m") + 1]
    else:
        model_name = vendor.default_model_name

    if "--validate" in sys.argv:
        validation_needed = True
    else:
        validation_needed = False

    if "-vm" in sys.argv:
        validation_model_name = sys.argv[sys.argv.index("-vm") + 1]
    else:
        validation_model_name = vendor.default_model_name

    if "-vf" in sys.argv:
        validation_file = sys.argv[sys.argv.index("-vf") + 1]
    else:
        validation_file = '../validation/classic_check.json'

    if "-t" in sys.argv:
        throttle = int(sys.argv[sys.argv.index("-t") + 1])
    else:
        throttle = 0

    with open(input_file, 'r') as f:
        prompts = f.readlines()

    for prompt in prompts:
        result = vendor.run(prompt, model_name)
        if validation_needed:
            validation_result = Validator().validate(vendor, validation_model_name, result, validation_file, throttle)
            
            with open(output_file, 'a') as result_file:
                result_file.write(f"# Prompt: {prompt}\n## Validation:\n{validation_result}\n\n## Response:\n\n{result}\n---\n")
        else:
            with open(output_file, 'a') as result_file:
                result_file.write(f"# Prompt: {prompt}\n## Response:\n\n{result}\n---\n")
        print(f"Tested prompt: {prompt.strip()}")

        if throttle > 0:
            import time
            time.sleep(throttle)