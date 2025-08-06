# Secondhand Clothing Notifier (Work in Progress)

This is an in-progress Python project designed to monitor secondhand clothing listings across Japanese resale platforms such as Yahoo Auctions and Mercari. The goal is to automatically scrape product listings, store them in a database, and send alerts when a listing matches user-defined criteria like price caps or auction end time.

## Project Goals

- Scrape listings from Yahoo Japan Auctions, Mercari, and other secondhand platforms
- Store and filter listings using MySQL and Pandas
- Allow user-configured search terms and max price input
- Notify the user when new listings meet the criteria

## Current Status (as of August 2025)

The project is still under development. The following components are in various stages of completion:

- Scrapers for Yahoo and Mercari using BeautifulSoup and Selenium – partially complete
- SQL database connector setup using MySQL – complete
- Notification system – in progress
- Main controller script – in progress
- Frontend interface – not started
- Alert scheduling and filtering – not started

## Project Structure

secondhand-notifier/
├── scrapers/ # Contains scraping logic for each site
├── config/ # Contains database config file
├── utils/ # Notification logic (e.g. email/SMS alerts)
├── main.py # Central script to run and manage components
├── requirements.txt # Python dependencies
├── README.md # Project documentation

## Technologies Used

- Python 3.9+
- BeautifulSoup (for HTML parsing)
- Selenium (for JavaScript-rendered content)
- MySQL (data storage)
- Pandas (data filtering and manipulation)
- SQLAlchemy (planned for ORM)

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/secondhand-notifier.git
   cd secondhand-notifier

2. Create and activate a virtual environment:
    python3 -m venv venv
    source venv/bin/activate

3. Install the dependencies:
    pip install -r requirements.txt

4. Set up your database configuration in config/db_config.py.
    Running an Example (Mercari Scraper)
    python scrapers/mercari.py

## Notes:
This project is currently being developed for personal use and learning purposes.
Once completed, it will support real-time listing filters and push notifications.
Future plans include creating a lightweight user interface and scheduling system.


## Contact

Created by Zoe Simmons.

If you have questions, suggestions, or want to collaborate, feel free to open an issue or reach out.