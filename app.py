'''http://foxworld.online:25662/
http://foxworld.online:25662/eureka/'''
import py_eureka_client.eureka_client as eureka_client
from flask import Flask, request
import tensorflow as tf

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/docs'
API_URL = '/swagger'

swagger_ui_blueprint = get_swaggerui_blueprint(
   SWAGGER_URL,
   API_URL,
   config={
       'app_name': 'My App'
   }
)
your_rest_server_port = 9090

# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
# eureka_client.init(eureka_server="http://localhost:8081/eureka/",
#                    app_name="your_app_name",
#                    instance_port=your_rest_server_port)


#eureka_client.init(eureka_server="http://root:8081/eureka/",
#                   app_name="NeuroServicePy",
#                   instance_port=your_rest_server_port)

app = Flask(__name__)

#model, _ = t_model.get_model()
#model.load_weights("./distilbert_t")



@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]
    return {"response": text}


if __name__ == "__main__":
    app.run(port=your_rest_server_port,host="0.0.0.0")
