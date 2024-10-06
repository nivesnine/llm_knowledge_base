# llm_knowledge_base
Welcome, this repo is going to serve as a general knowledge dump of the things I'm learning with AI. It could get rough, but I'll try to smooth it out over time.

There's sort of two things here right now.

1) The start of some templates for testing AI that have worked decently for me recently. I'm slowly adding them over time, generalizing some of these is a little complex.

2) PIMP is a work in progress testing protcol, it's untested and completely AI generated in it's current state. [I haven't even read most of it]

Eventually I'd love to merge the two for some automated testing.


## latest update:
1) PIMP restructured and working but is still missing a good bit to be useful.
- create a virualenv with pyhton 3.11 `virvutalenv -p /usr/bin/python3.11 env`
- activate the virtualenv `source env/bin/activate`
- cd into PIMP
- install requirments `pip install -r requirments.txt`

make sure you create a `.env` file at the root of the PIMP dir (`/PIMP/.env`)
```
GOOGLE_API_KEY = "google api key here"
OPENAI_API_KEY = "open api key here"
```

run tests:
- `python gemini_test.py` default test will run all prompts in PIMP/test/prompts.txt
- `python gemini_test.py -i input_file_name -o output_file_name -m "model_name"` custom test, all flags optional

2) risks was moved out to the top level just because it may end up being good info, still chatgpt generated currently but I might update it eventually

3) readme's updated

4) /tools probably useless chatgpt giberish

5) will release more prompt templates and likely some red teaming prompts just so I have access on any computer, and open to sharing them, but want to test them a bit more when more.

6) contributing updated, if you want to contribute I'm unlikely to say no

7) random tips is ugh... well there's really nothing there right now but eventually there will be

8) all the tests need to be updated and reworked still and then I can update the protocol steps