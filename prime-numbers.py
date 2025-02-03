import time
import sqlite3
import os
import unittest

def get_prime_factors(n):
    factors = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    return sorted(factors)

def create_database():
    conn = sqlite3.connect("prime_factors.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS factors (
            number INTEGER PRIMARY KEY,
            factors TEXT,
            time_taken REAL
        )
    """)
    conn.commit()
    conn.close()

def get_from_database(n):
    conn = sqlite3.connect("prime_factors.db")
    cursor = conn.cursor()
    cursor.execute("SELECT factors, time_taken FROM factors WHERE number = ?", (n,))
    result = cursor.fetchone()
    conn.close()
    if result:
        factors, time_taken = result
        return list(map(int, factors.split(","))), time_taken
    return None, None

def save_to_database(n, factors, time_taken):
    conn = sqlite3.connect("prime_factors.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO factors (number, factors, time_taken) VALUES (?, ?, ?)",
                   (n, ",".join(map(str, factors)), time_taken))
    conn.commit()
    conn.close()

def write_output_file(n, factors, time_taken):
    filename = f"prime_factors_{n}.txt"
    with open(filename, "w") as file:
        file.write(f"Prime Factors of number {n} are\n")
        file.write(", ".join(map(str, factors)) + "\n")
        file.write(f"It took {time_taken:.2f} seconds to find those\n")
    print(f"Results saved to {filename}")

def main(number):
    create_database()

    try:
        if number < 2:
            print("Please enter a natural number greater than 1.")
            return

        start_time = time.time()
        stored_factors, stored_time = get_from_database(number)

        if stored_factors:
            factors, elapsed_time = stored_factors, stored_time
            print("Fetched from database!")
        else:
            factors = get_prime_factors(number)
            elapsed_time = time.time() - start_time
            save_to_database(number, factors, elapsed_time)

        for factor in factors:
            print(f"Prime factor found: {factor}")
        print(f"It took {elapsed_time:.2f} seconds to find those")

        write_output_file(number, factors, elapsed_time)

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
            main(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    else:
        print("Please provide a number as a command-line argument.")

# Unit Tests
class TestPrimeFactors(unittest.TestCase):
    def test_get_prime_factors(self):
        self.assertEqual(get_prime_factors(26541), [3, 983])
        self.assertEqual(get_prime_factors(28), [2, 7])
        self.assertEqual(get_prime_factors(37), [37])
        self.assertEqual(get_prime_factors(100), [2, 5])

    def test_database_operations(self):
        create_database()
        save_to_database(50, [2, 5], 0.01)
        factors, time_taken = get_from_database(50)
        self.assertEqual(factors, [2, 5])

if __name__ == "__main__":
    unittest.main()
