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

# **🔧 Provisioning AWS EC2 and Setting Up the Environment**

## **📌 Step 1: Create an AWS EC2 Instance**

1. **Log in to AWS Console** and go to **EC2 Dashboard**.
2. Click **Launch Instance**.
3. Choose **Ubuntu 22.04 LTS (recommended)**.
4. Select **Instance Type** (e.g., `t2.micro` for free tier).
5. Click **Next: Configure Security Group**.

---

## **📌 Step 2: Configure Security Group (Allow Port 5000)**
1. In the **Security Group** settings, click **Edit inbound rules**.
2. Add a new rule:
   - **Type:** Custom TCP Rule
   - **Port Range:** `5000`
   - **Source:** `Anywhere (0.0.0.0/0, ::/0)`
3. Click **Save Rules**.

This allows external access to Flask API running on port 5000.

---

## **📌 Step 3: Connect to EC2 Instance**
Once your EC2 instance is running, connect to it using SSH:

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

- Replace `your-key.pem` with your actual key file.
- Replace `your-ec2-public-ip` with your actual EC2 Public IP.

---

## **📌 Step 4: Prepare the EC2 Environment for Python**

Run the following commands to install **Python and dependencies**:

```bash
# Update and install Python
sudo apt update -y
sudo apt install python3 python3-pip python3-venv git -y

# Verify Python installation
python3 --version
pip3 --version
```

---

## **📌 Step 5: Clone the Project into EC2**

Clone the GitHub repository where the project is stored:

```bash
git clone https://github.com/your-username/number-classification-api.git
cd number-classification-api
```

---

## **📌 Step 6: Set Up a Virtual Environment and Install Dependencies**

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt
```

Verify installation:

```bash
pip list | grep flask
```

---

## **📌 Step 7: Run the Flask API**

Run the API with:

```bash
python numberapi.py
```

If everything is correct, you should see:

```
 * Running on http://0.0.0.0:5000/
```

---

## **📌 Step 8: Allow External Traffic on Port 5000**

If the API is not accessible, disable the firewall:

```bash
sudo ufw disable
```

Test your API:

```bash
curl -X GET "http://your-ec2-public-ip:5000/api/classify-number?number=371"
```

---

## **📌 Step 9: Keep API Running in Background**

To keep the Flask app running after logout:

```bash
nohup python3 numberapi.py > output.log 2>&1 &
```

Or use **tmux**:

```bash
tmux
python3 numberapi.py
```

Press **`CTRL + B`, then `D`** to detach.

---

## **📌 Step 10: Automate API Restart on Server Reboot**

Create a systemd service:

```bash
sudo nano /etc/systemd/system/numberapi.service
```

Paste this:

```
[Unit]
Description=Number API
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/ubuntu/number-classification-api/numberapi.py
WorkingDirectory=/home/ubuntu/number-classification-api
Restart=always
User=ubuntu

[Install]
WantedBy=multi-user.target
```

Save (`CTRL + X`, then `Y`, then `ENTER`).

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable numberapi
sudo systemctl start numberapi
```

Check status:

```bash
sudo systemctl status numberapi
```

---

## **✅ Final Checklist Before Submission**
✔ **API is running & accessible via public URL**  
✔ **Tested with different inputs**  
✔ **GitHub repository is public**  
✔ **README.md updated with setup instructions**  
  

🚀 **API is now LIVE on AWS EC2!** 🎯 