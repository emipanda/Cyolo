# Cyolo Words Histogram
## Install 
<pre>pip install -r requirements.txt</pre>

## Run
<pre>python3 main_server.py </pre>

Running the server will start both endpoints: 
1. **The word receiver (websocket)**: <pre>ws://localhost:7890</pre>
2. **The frequency distribution rank result (RESTAPI)**:   <pre> GET http://localhost:5000/getHistogram</pre>

I used a websocket client to test my service: <pre>https://www.piesocket.com/websocket-tester#</pre>
And Postman for the GET Request

## Simulation

![image](https://user-images.githubusercontent.com/9104818/189212980-6e168a2f-3eca-46a1-9c45-ce4d06b2d812.png)

![image](https://user-images.githubusercontent.com/9104818/189213196-c41e11f0-0130-4f91-95ac-a2ca2a0867a9.png)
