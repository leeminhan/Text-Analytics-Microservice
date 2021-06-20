import requests
import json 

sample_data = {
    "body": {
        "data": ["Turin's theory deuterated acetophenone smells different (from non- deuterated from), it deuterated benzaldehyde smells different (from non- deuterated form), structures of deuterated acetophenone and benzaldehyde given.", 
        "Molecules have very different shapes so the lock and key theory suggests they would smell different but in fact they smell similar. By contrast, diols like ethylere glycol smell completely different to dithols despite very similar shapes.", "Ethylene glycol and ethane clithicl have very dimilar structure but very different smellsin the lock and key theory, these two molecules would have very similar smells as both molecules could fit in the same lock. When atoms were replaced with their ixtopeom moleculea there was a subtle change in smell in the lock and key theory. This would indicate that the massed the banded atoms does affect smell, as predicted by Turin Timber."
        ]
    }
}

sample_data_prod = {
    "data": ["Turin's theory deuterated acetophenone smells different (from non- deuterated from), it deuterated benzaldehyde smells different (from non- deuterated form), structures of deuterated acetophenone and benzaldehyde given.", 
    "Molecules have very different shapes so the lock and key theory suggests they would smell different but in fact they smell similar. By contrast, diols like ethylere glycol smell completely different to dithols despite very similar shapes.", "Ethylene glycol and ethane clithicl have very dimilar structure but very different smellsin the lock and key theory, these two molecules would have very similar smells as both molecules could fit in the same lock. When atoms were replaced with their ixtopeom moleculea there was a subtle change in smell in the lock and key theory. This would indicate that the massed the banded atoms does affect smell, as predicted by Turin Timber."
    ]
}

# To run locally ======
obj = json.dumps(sample_data)
response = requests.post('http://localhost:8080/2015-03-31/functions/function/invocations', data = obj)
print(json.dumps(response.json(), indent=1))

# obj = json.dumps(sample_data_prod)
# response = requests.post('https://cmuzbmhg3e.execute-api.ap-southeast-1.amazonaws.com/dev/qa', data = obj)
# print(json.dumps(response.json(), indent=1))