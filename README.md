🎯 Project Goal

To create an interactive Power BI report that provides a detailed analysis of Premier League clubs' expenditures, including:

- 💰 Transfer spending

- 🏟️ Player salaries

- 📊 Operational costs
The data is collected, processed, and stored using Python and web scraping techniques.

Scope of Work

1️⃣ Web Scraping

🔍 Identify and collect data from reliable sources (e.g., transfer and financial websites).

💻 Automate data collection with Python libraries:

- BeautifulSoup
- Requests
  
✅ Validate and process data to ensure accuracy.

2️⃣ Database Development

- 🛠️ Design and build a database with structured tables (e.g., expenditures, revenues, transfers).

- 📂 Tools used: SQLAlchemy, Pandas.

- 🔄 Enable regular database updates to reflect new data.

3️⃣ Power BI Reporting

📊 Develop visualizations for:

- Player salary analysis across clubs.

- Transfer spendings

- What are a costs of 1 league point

🎛️ Add interactive filters for:

Season segmentation.


Prerequisites

To run this project, you need to have Python 3.7+ installed. You also need to install the following libraries:

- requests: For making HTTP requests.
 
- beautifulsoup4: For parsing and scraping HTML content.

- python-dotenv: For managing environment variables (e.g., database credentials).

- sqlalchemy: For database integration and ORM functionality.

To install the dependencies, use the following command:

```pip install -r requirements.txt```

<pre>
requests==2.28.1
beautifulsoup4==4.12.0
python-dotenv==0.20.0
sqlalchemy==2.0.19
</pre>


Project Structure

<pre>
.
├── .env               # Environment variables (e.g., database credentials)
├── main.py            # Main script to execute web scraping, data manipulation, and saving to DB
├── models.py          # SQLAlchemy models for database tables
├── requirements.txt   # List of dependencies
└── README.md          # This file
</pre>
