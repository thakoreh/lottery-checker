
## Getting Started with Lottery Checker

This project is a Python application that extracts lottery data for analysis.

### Prerequisites

Ensure that you have the following installed on your local development machine:

- Python (v3.6 or above)

### Installation

1. Clone the repository to your local machine.
2. Navigate to the backend directory.
3. Run the extract_data.py script to start data extraction.

### Usage

Run the extract_data.py script. This will scrape lottery data and store it in a CSV file for further analysis.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License.

### Data Analysis

Once the `extract_data.py` script has been executed, a CSV file containing the lottery data will be generated. This data can be utilized for further analysis. 

Here is an example of the data you can expect:

```csv
Date, Number1, Number2, Number3, Number4, Number5, Number6, Bonus
Saturday30th December 1995, 6, 32, 39, 42, 43, 45, 36
Saturday23rd December 1995, 6, 11, 34, 40, 47, 49, 16
...
```

Each row represents a lottery draw, with the date of the draw and the numbers drawn. The last number is the bonus number.

You can use any data analysis tools you prefer to analyze this data. For example, you can use Python libraries like pandas or numpy for data manipulation and analysis.
