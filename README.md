🧠 League of Legends Analytics Dashboard



A full data analytics project that collects, processes, and visualizes high-elo League of Legends ranked data using Riot Games API, SQLite, SQL, Python, and Power BI.



📌 Project Goal



The goal of this project is to build an end-to-end analytics pipeline:



Collect data from Riot Games API Store structured data in SQLite database Transform data using Python (Pandas + SQL) Build analytical dashboards in Power BI ⚙️ Tech Stack Python Riot Games API SQLite Pandas SQL Matplotlib Power BI Git / GitHub



🏗️ Architecture Riot API ↓ Python ETL (collector\_etl.py) ↓ SQLite Database (lol.db) ↓ SQL Analysis (analysis.py) ↓ CSV Export (export\_dashboard.py) ↓ Power BI Dashboard 📊 Dashboard Pages



Overview Dashboard Players distribution by LP Top champions Average match duration Winrate \& KDA overview

Champion Analytics Champion performance table Winrate vs Games scatter plot KDA analysis

Match Insights Match duration vs outcome Role-based analysis

📁 Project Structure src/ # API, database, transformations collector\_etl.py # Data collection pipeline analysis.py # SQL analytics queries export\_dashboard.py # Export data for Power BI visualization.py # Charts and reports data/ # Exported datasets reports/ # Saved visualizations database/ # SQLite database



🚀 How to Run pip install -r requirements.txt python collector\_etl.py python export\_dashboard.py python visualization.py



Then open Power BI file and refresh data.



📈 Key Features End-to-end ETL pipeline Real Riot Games data integration 10,000+ ranked players dataset 100–500+ match analytics SQL-based aggregation layer Interactive Power BI dashboards 📷 Dashboard Preview



(Add screenshots from reports/ folder here)



📌 Notes Data is collected from Riot Games API (EUW region) Rate limiting handled with delays Duplicate matches are filtered Database stored in SQLite

