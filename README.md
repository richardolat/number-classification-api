# Number Classification API (HNG TECH Internship - Stage 1)

This API classifies numbers based on their mathematical properties and provides a fun fact.  
It is part of the **HNG TECH Internship - Stage 1** DevOps project.

---

## 🚀 Features
- Accepts **GET requests** with a number parameter.
- Returns **JSON response** with number properties.
- Uses **Parity (mathematics) from Wikipedia** for odd/even classification.
- Uses **NumbersAPI for mathematical fun facts**.
- Handles **edge cases gracefully** (non-numeric inputs, negative numbers, numbers with multiple properties).
- Provides **appropriate HTTP status codes**.
- **CORS enabled** for cross-origin requests.

---

## 📌 API Specification

### **Endpoint:**  
**GET** `/api/classify-number?number=371`  

### **Response Format (200 OK)**:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "class_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **Response Format (400 Bad Request)**:
```json
{
    "number": "alphabet",
    "error": true
}
```

---

## 📌 Installation & Running Locally

### **Step 1: Install Dependencies**
```bash
pip install flask flask-cors requests
```

### **Step 2: Run the API**
```bash
python numberapi.py
```

### **Step 3: Test the API**
Use **Postman** or **Curl** to test the API:

```bash
curl -X GET "http://127.0.0.1:5000/api/classify-number?number=371"
```

---

## 🚀 Deploying to AWS EC2

### **Step 1: Connect to Your EC2 Instance**
```bash
ssh -i your-key.pem ubuntu@your-ec2-instance-ip
```

### **Step 2: Install Python & Dependencies**
```bash
sudo apt update -y
sudo apt install python3 python3-pip -y
pip3 install flask flask-cors requests
```

### **Step 3: Upload & Run API**
```bash
scp -i your-key.pem numberapi.py ubuntu@your-ec2-instance-ip:~/
ssh -i your-key.pem ubuntu@your-ec2-instance-ip
python3 numberapi.py
```

### **Step 4: Allow External Access to Port 5000**
```bash
sudo ufw allow 5000
```

### **Step 5: Keep API Running in Background**
```bash
nohup python3 numberapi.py > output.log 2>&1 &
```

### **Step 6: Test Public API**
```bash
curl -X GET "http://your-ec2-instance-ip:5000/api/classify-number?number=371"
```

---

## 📌 Example Screenshots
*(Add your API screenshots here)*

---

## ✅ Final Checklist Before Submission
✔ **API is running & accessible via public URL**  
✔ **Tested with different inputs**  
✔ **GitHub repository is public**  
✔ **README.md updated with setup instructions**  
✔ **Submitted in `#stage-one-devops`**  

🚀 **Your API is now LIVE on AWS EC2!** 🎯  
