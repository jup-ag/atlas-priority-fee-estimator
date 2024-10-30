from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import requests

while True:
    response = requests.post(
        "http://localhost:4141",
        json={
            "jsonrpc": "2.0",
            "id": "1",
            "method": "getPriorityFeeEstimateV2",
            "params": [
                {"options": {"includeAllPriorityFeeLevels": True, "lookbackSlots": 20}}
            ],
        },
    )
    if response.status_code != 200:
        raise Exception(f"{response.text}")

    response_json = response.json()
    data = response_json["result"]["priorityFeeLevels"]["accountToFees"]["global"]

    # print(f"max: {max(data)}, min {min(data)}")
    print(np.percentile(data, [25, 50, 75, 95]))
    sleep(0.5)

# plt.hist(
#     data
# )
# plt.show()
