# Django Full Stack BI Dashboard

Analyze Netflix data from Kaggle [Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows) and create a dashboard for the application. [View Web Dashboard](https://djangofullstackbideveloper.vercel.app)

## Features
This responsive web application is built using the Django framework to analyze Netflix data from Kaggle. The process involves:
1. **Data Cleaning** – Initial data processing using Jupyter Notebook (available in the `data` folder).
2. **Data Pipeline** – Storing cleaned data in PostgreSQL (hosted on [Aiven.io](https://aiven.io/)) using SQLAlchemy.
3. **Dashboard Creation** – Implementing interactive visuals using HTML, CSS, JavaScript, and Chart.js.

## Technologies Used
- **Backend:** Python, Django, SQLAlchemy, PostgreSQL
- **Frontend:** HTML5, CSS, Tailwind CSS, JavaScript, Chart.js
- **Data Analysis:** NumPy, Pandas, Matplotlib, Seaborn
- **Deployment & Development:** Vercel, GitHub, VS Code



## Installation and Usage

- Install Python on your machine.
- Create an account on [aiven.io](https://aiven.io/) to set up a free PostgreSQL server.
#### Setup Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nanhpauyu/django_fullstack_bi_developer.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd django_fullstack_bi_developer
   ```
3. **Create a Virtual Environment:**
   ```bash
   python -m venv env_name
   ```
   - **Activate the Virtual Environment:**
     - Windows (Command Prompt): `path\to\venv\Scripts\activate`
     - Windows (PowerShell): `./path/to/venv/Scripts/Activate`
     - macOS/Linux: `source path/to/venv/bin/activate`

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure the Database:**
   - Create a **PostgreSQL service** on Aiven.io (free version).
   - Create a `.env` file and add the following:
     ```python
     DB_USER='your_db_user'
     DB_PASSWORD='your_db_password'
     DB_HOST='your_db_host'
     DB_PORT='your_db_port'
     DB_NAME = 'defaultdb'
     ```
6. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
7. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the instructions to create an admin account.

8. **Run the Application:**
   ```bash
   python manage.py runserver
   ```
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
   - Log in with the username and password you created.


---

### Method 2: Deploying on Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&demo-title=Django%20%2B%20Vercel&demo-description=Use%20Django%204%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994241/random/django.png)

#### Steps to Deploy
1. **Fork the Repository** to your GitHub or upload the project to your GitHub repo.
2. **Create an Account on Vercel** if you don’t have one.
3. **Go to Vercel Dashboard** → Click **Add New Project**.
4. **Connect Vercel with GitHub** and select your repository.
5. **Add Environment Variables**
   - Copy the contents of your `.env` file and add them to Vercel’s **Environment Variables** section.
6. **Deploy the Application** by clicking **Deploy**.

---

![Login](/images/a.png)

![Overview](/images/b.png)

![Movies](/images/c.png)

![Movies](/images/d.png)

![TV Shows](/images/e.png)

![TV Shows](/images/f.png)

![Videos](/images/recording.mp4)