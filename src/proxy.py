from mitmproxy import http
import joblib
import re

from src import links

# Load your trained ML model
model = joblib.load('C:\Users\Dell\PycharmProjects\malicious\src\random_nodel.pkl')


def preprocess_url(url):
    process = links.numeric_value(url)
    return process  # Replace with actual preprocessing logic


def request(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url
    print(f"Intercepted URL: {url}")
    features = preprocess_url(url)
    prediction = model.predict([features])
    is_malicious = prediction[0] == 1

    if is_malicious:
        flow.response = http.Response.make(
            403,  # HTTP status code
            b"Blocked by URL Filter",  # Response body
            {"Content-Type": "text/html"}  # Headers
        )


if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump

    mitmdump(["-s", __file__])
