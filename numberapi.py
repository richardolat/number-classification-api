from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

app = Flask(__name__)
CORS(app)  # Enable CORS

NUMBERS_API_URL = "http://numbersapi.com/"

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number (sum of divisors equals the number)."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

def get_properties(n):
    """Return a list of mathematical properties for the given number."""
    properties = []
    if is_prime(n):
        properties.append("prime")
    if is_perfect(n):
        properties.append("perfect")
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

def get_fun_fact(n):
    """Fetch a fun fact about the number from NumbersAPI."""
    try:
        response = requests.get(f"{NUMBERS_API_URL}{n}/math?json=true")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact available")
    except requests.exceptions.RequestException:
        return "Fun fact service unavailable"
    return "No fun fact available"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """API endpoint to classify a number and return its mathematical properties."""
    number_param = request.args.get("number")

    # Validate input
    if not number_param or not number_param.isdigit():
        return jsonify({"number": number_param, "error": True}), 400

    number = int(number_param)
    properties = get_properties(number)
    class_sum = sum(int(digit) for digit in str(number))
    fun_fact = get_fun_fact(number)

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "class_sum": class_sum,
        "fun_fact": fun_fact
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
