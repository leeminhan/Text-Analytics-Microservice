# Rolljak - Correctness Evaluation Microservice

## Setup venv
1. Create venv
```bash
python3 -m venv text-analytics-env
```

2. Activate venv
https://docs.python.org/3/tutorial/venv.html
```bash
source text-analytics-env/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Getting Started
1. Start Server
```bash
uvicorn main:app --reload
```

#### Data Type
idea_id: id student's response to that qn <br>
challenge_id: 1 unique Question/Activity
#### Data Format From Rails Backend
```
[
    {
        "challenge_id": int,
        "challenge_ans": [ans_1, ans_2, ans_3],
        <!-- "challenge_title": str, -->
        "responses": [
            {
                "pc_id_1":{
                    "idea_id1": "idea_body1",
                },
                "pc_id_2":{
                    "idea_id4": "idea_body1",
                    "idea_id5": "idea_body2",
                    "idea_id6": "idea_body2",
                }
            }
        ]
    }
]
```

##### Response Payload
```
{
    "idea_id1": {
        "score": score_value
    },
    "idea_id2": {
        "score": score_value
    },
    "idea_id3": {
        "score": score_value
    }
}
```