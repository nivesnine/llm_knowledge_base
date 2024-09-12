#!/usr/bin/env python3

import argparse

def generate_prompt(base_prompt, variations):
    """Generate multiple variations of a base prompt."""
    prompts = []
    for variation in variations:
        prompts.append(f"{base_prompt} {variation}")
    return prompts

def main():
    parser = argparse.ArgumentParser(description='Generate variations of a base prompt.')
    parser.add_argument('base_prompt', type=str, help='The base prompt to generate variations from.')
    parser.add_argument('variations', nargs='+', help='Variations to append to the base prompt.')
    args = parser.parse_args()
    
    prompts = generate_prompt(args.base_prompt, args.variations)
    for prompt in prompts:
        print(prompt)

if __name__ == '__main__':
    main()