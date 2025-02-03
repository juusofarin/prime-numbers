# Prime Factors Finder

This script calculates the prime factors of a given number, ensuring that no duplicate factors are included. It also stores results in an SQLite database to optimize repeated queries.

## Usage

### Running the script
To execute the script, provide a number as a command-line argument:
```sh
python3 prime-numbers.py 26541
```

### Example Output
```
Prime factor found: 3
Prime factor found: 983
It took 0.00 seconds to find those
Results saved to prime_factors_26541.txt
```

### Output File
The script creates a text file in the following format:
```
Prime Factors of number 26541 are
3, 983
It took 0.00 seconds to find those
```

## Features
- Computes unique prime factors of a number.
- Stores results in an SQLite database to prevent redundant calculations.
- Saves results in a text file.
- Measures computation time.
- Includes a unit test suite.

## Running Tests
To run the unit tests, execute:
```sh
python3 -m unittest prime-numbers.py
```

## Dependencies
- Python 3
- SQLite3 (built-in with Python)

## Notes
Ensure that you are running the script in the same directory where `prime-numbers.py` is located to avoid file path issues.