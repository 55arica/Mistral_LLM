# Synchronous Example
from mistralai import Mistral
import os

with Mistral(
    api_key=os.getenv("MISTRAL_API_KEY", ""),
) as mistral:

    res = mistral.chat.complete(model="mistral-small-latest", messages=[
        {
            "content": "which operative system is best? Answer in one short sentence.",
            "role": "user",
        },
    ])

    assert res is not None

    print(res)
