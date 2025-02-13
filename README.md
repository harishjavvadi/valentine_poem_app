💖 Valentine Poem Generator

A fun Flask-based web app that generates romantic Valentine’s Day poems using the Gemini API. Inspired by the interactive “Will you be my Valentine?” concept, this app allows users to engage in a playful way while also receiving personalized AI-generated poems.

🚀 Features
	•	🏹 Playful Valentine Request Page – A fun “Yes or No” Valentine proposal interaction.
	•	💕 Customizable Responses – Personalize the phrases and images displayed.
	•	📜 AI-Generated Poems – Uses Google Gemini API to create personalized Valentine poems.
	•	🎨 Customizable Design – Modify text, colors, and images to match your style.
	•	🌐 Deployable Anywhere – Easily deployable on Render, Railway, or Google Cloud Run.

🛠️ Installation & Setup

Follow these steps to run the project locally:

1️⃣ Clone the Repository

git clone https://github.com/harishjavvadi/valentine_poem_app.git
cd valentine_poem_app

2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Your API Key
	1.	Create a .env file in the project directory:

GEMINI_API_KEY=your-actual-gemini-api-key


	2.	Replace your-actual-gemini-api-key with your Gemini API key.

5️⃣ Run the Flask App

python app.py

The app should now be running at:
👉 http://127.0.0.1:5000/

🌍 Deployment

You can deploy this app using Render, Railway, or Google Cloud Run.

🔹 Deploy to Render
	1.	Push your code to GitHub.
	2.	Go to Render.
	3.	Click New Web Service → Select GitHub Repository.
	4.	Set the Start Command:

gunicorn app:app


	5.	Add an Environment Variable:

GEMINI_API_KEY=your-actual-gemini-api-key


	6.	Click Deploy and get your public link.

🎨 Tech Stack
	•	Backend: Flask (Python)
	•	Frontend: HTML, CSS, JavaScript
	•	API: Google Gemini API
	•	Deployment: Render/Railway/Google Cloud Run

🔗 Credits & Acknowledgments

This project was inspired by the interactive Valentine app created by mewtru. Their work on a fun and customizable Valentine request page served as a creative base for this project.

Special thanks to the Val Town community for sharing ideas and making such interactive projects open-source!

🤝 Contributing

Want to improve this project? Contributions are welcome!
	1.	Fork the repo
	2.	Create a new branch (git checkout -b feature-branch)
	3.	Make your changes
	4.	Commit & push (git push origin feature-branch)
	5.	Submit a Pull Request 🎉

📜 License

This project is open-source under the MIT License.

📬 Contact

📧 Email: harishmo@ualberta.ca
🔗 GitHub: harishjavvadi
🚀 Project Link: https://github.com/harishjavvadi/valentine_poem_app

❤️ Enjoy the app and Happy Valentine’s Day! ❤️
