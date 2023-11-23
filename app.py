'''http://foxworld.online:25662/
http://foxworld.online:25662/eureka/'''
from flask import Flask, request

your_rest_server_port = 9090

# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
# eureka_client.init(eureka_server="http://localhost:8081/eureka/",
#                    app_name="your_app_name",
#                    instance_port=your_rest_server_port)

import py_eureka_client.eureka_client as eureka_client

eureka_client.init(eureka_server="http://localhost:8081/eureka/",
                   app_name="ZALUPUPS 2: return",
                   instance_port=your_rest_server_port)

app = Flask(__name__)


@app.route("/test", methods=["GET"])
def test():
    print("zalupa")
    return "test"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=your_rest_server_port)
