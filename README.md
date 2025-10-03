# College Enquiry Chatbot Project 🤖

A simple chatbot built using **Python**, **Flask**, and machine learning.  
The chatbot uses `intents.json` for training and provides a clean web interface with `index.html` and `style.css`.

---

## 📂 Project Structure

```
├── app.py              # Flask application (entry point)
├── chatbot_response.py # Handles chatbot replies
├── train_chatbot.py    # Train the chatbot model
├── intents.json        # Training data (intents and responses)
├── requirements.txt    # Project dependencies
├── style.css       # Frontend styling
├── index.html      # Chatbot UI

```

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/chatbot-project.git
   cd chatbot-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧠 Training the Chatbot

Run the training script to build/update the model:

```bash
python train_chatbot.py
```

The trained model will be saved inside the `models/` folder.

---

## 🚀 Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

to chat with your bot.

---

## 📊 Customizing Intents

- Edit `intents.json` to add or modify intents and responses.
- Retrain the chatbot by running:
  ```bash
  python train_chatbot.py
  ```

---

## 🤝 Contributing

Contributions are welcome!  
1. Fork this repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the branch (`git push origin feature-name`)  
5. Create a Pull Request  

--

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
