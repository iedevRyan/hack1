#!flask/bin/python
from flask import Flask, jsonify
from random import randint, random, shuffle
import numpy as np, numpy.random
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/data')
def index():
    campaign_proportions = list(np.random.dirichlet(np.ones(randint(3, 10)), size=1)[0])  # get clayton

    campaign_proportions = [round(item, 2) for item in campaign_proportions]
    notifications_left = randint(400, 200000)
    campaign_ids = [randint(0, 400) for _ in range(len(campaign_proportions))]
    campaign_names = [f"Campaign {item}" for item in campaign_ids]
    notification_allotments = [int(notifications_left * proportion) for proportion in campaign_proportions]

    response_obj_ls = []
    for idx, id_num in enumerate(campaign_ids):
        # response_obj_ls.append(
        #     {
        #         "campaign_ids": campaign_ids[idx],
        #         "campaign_names": campaign_names[idx],
        #         "campaign_proportions": campaign_proportions[idx],
        #         # "campaign_ids": campaign_ids[idx],
        #
        #     }
        # )

        response_obj_ls.append(
            [
                # "campaign_ids":
                    campaign_ids[idx],
                # "campaign_names":
                    campaign_names[idx],
                # "campaign_proportions":
                    campaign_proportions[idx],
                # "campaign_ids": campaign_ids[idx],

            ]
        )

    response = [
        {
          "notifications_remaining": notifications_left,
          "campaign_ids": campaign_ids,
          "campaign_names":campaign_names,
          "campaign_proportions": campaign_proportions,
          "campaign_notification_allotments": notification_allotments
        }
    ]
    # return f"{campaign_list},\n {campaign_proportions},\n {notification_allotments}"


    # temp!!
    # response = Flask.jsonify({'some': 'data'})
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return jsonify(response_obj_ls)

if __name__ == '__main__':
    app.run(host='localhost', port=8088, debug=True)  # tried 0.0.0.0 127.0.0.0