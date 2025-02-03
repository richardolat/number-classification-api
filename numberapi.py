from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math
from collections import OrderedDict

app = Flask(__name__)
CORS(app)

NUMBERS_API_URL = "http://numbersapi.com/"

def is_prime(n):
    """Check if a number is prime. Negative numbers and non-integers are not prime."""
    if n < 2 or not n.is_integer():
        return False
    n = int(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number. Negative numbers and non-integers are not perfect numbers."""
    if n < 1 or not n.is_integer():
        return False
    n = int(n)
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    if not n.is_integer():
        return False
    n = abs(int(n))
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

def get_parity(n):
    """Determine whether a number is odd, even, or a floating-point number."""
    if not n.is_integer():
        return "floating-point"
    return "even" if int(n) % 2 == 0 else "odd"

def get_properties(n):
    """Return a list of mathematical properties."""
    properties = [get_parity(n)]
    if is_prime(n):
        properties.append("prime")
    if is_perfect(n):
        properties.append("perfect")
    if is_armstrong(n):
        properties.append("armstrong")
    return properties

def get_fun_fact(n):
    """Fetch a fun fact from NumbersAPI and ensure correct JSON output."""
    try:
        n = abs(int(n))  # Convert float to integer & ignore negative sign
        headers = {"Accept": "text/plain"}  # Ensure response is plain text
        response = requests.get(f"{NUMBERS_API_URL}{n}/math", headers=headers, timeout=5)

        # Ensure response is not HTML
        if response.status_code == 200 and "<html" not in response.text.lower():
            return response.text.strip()
    except requests.exceptions.RequestException:
        return "Fun fact service unavailable"

    return f"No fun fact found for {n}"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """API endpoint to classify a number."""
    number_param = request.args.get("number")

    # Validate input properly
    if not number_param:
        return jsonify(OrderedDict([
            ("number", "alphabet"),
            ("error", True)
        ])), 400, {"Content-Type": "application/json"}

    try:
        number = float(number_param)
        if number.is_integer():
            number = int(number)  # Convert to integer if it's a whole number
    except ValueError:
        return jsonify(OrderedDict([
            ("number", "alphabet"),
            ("error", True)
        ])), 400, {"Content-Type": "application/json"}

    properties = get_properties(number)

    # Ensure digit_sum is always numeric and accounts for negatives
    digit_sum = sum(int(digit) for digit in str(abs(int(number))) if digit.isdigit())

    fun_fact = get_fun_fact(number)

    # Ensure valid JSON response
    response = OrderedDict([
        ("number", number),
        ("is_prime", is_prime(number)),
        ("is_perfect", is_perfect(number)),
        ("properties", properties),
        ("digit_sum", digit_sum),  # FIXED: Now using 'digit_sum'
        ("fun_fact", fun_fact)
    ])

    return jsonify(response), 200, {"Content-Type": "application/json"}  # ✅ Always return JSON format

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
