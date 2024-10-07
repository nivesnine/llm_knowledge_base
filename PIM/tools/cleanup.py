# run this to remove the result files created in /results
# python cleanup.py

import os

def cleanup():
    result_files = os.listdir('../results')
    for file in result_files:
        os.remove(f'../results/{file}')
    print("Results cleaned up.")

if __name__ == "__main__":
    cleanup()
