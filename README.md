# Chess ETL Project

## Overview

This is a small personal project aimed at exploring the capabilities of the [dlt](https://pypi.org/project/dlt/) Python package for ETL (Extract, Transform, Load) processes. The project connects to the Chess.com API to fetch player statistics and displays the data in a user-friendly Streamlit interface. Users can query the data using SQL through the Streamlit interface.

## Features

- Connects to the Chess.com API to retrieve player statistics.
- Utilizes the dlt package for efficient ETL processes.
- Displays data in a Streamlit interface for easy access and visualization.
- Allows users to query data using SQL.
- Implements code quality checks using Pylint, integrated with GitHub Actions.

## Getting Started

### Prerequisites

- Python 3.x
- dlt package
- Streamlit
- GitHub account (for Actions)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chess-etl-project.git
   cd chess-etl-project
   ```
   
2. Install the required packages:
  ```bash
  pip install -r requirements.txt
  ```

4. Run the script via your terminal:
   ```bash
   python chess_pipeline.py
   ```

6. Display the streamlit interface via your terminal:
  ```bash
   dlt pipeline chess_pipeline show
  ```



## Code Quality
To ensure code quality, this project uses Pylint. A GitHub Action is set up to run Pylint on each new code push. You can check the results in the Actions tab of the repository.


## Acknowledgments
dlt for the ETL framework.
Streamlit for the interactive web application framework.
Chess.com API for providing player statistics.
