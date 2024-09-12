#!/usr/bin/env python3

import argparse
import json

def parse_results(results_file, output_format='json'):
    """Parse results from a file and output in the specified format."""
    with open(results_file, 'r') as file:
        data = file.read()

    # Simulate parsing results (this example assumes the results are in JSON format)
    try:
        parsed_data = json.loads(data)
    except json.JSONDecodeError:
        print("Error: Could not parse results. Ensure the results file is in valid JSON format.")
        return

    if output_format == 'json':
        print(json.dumps(parsed_data, indent=4))
    elif output_format == 'text':
        for item in parsed_data:
            print(item)
    else:
        print(f"Unsupported format: {output_format}")

def main():
    parser = argparse.ArgumentParser(description='Parse results from a file.')
    parser.add_argument('results_file', type=str, help='The file containing results to parse.')
    parser.add_argument('--format', choices=['json', 'text'], default='json', help='Output format for the results.')
    args = parser.parse_args()
    
    parse_results(args.results_file, args.format)

if __name__ == '__main__':
    main()