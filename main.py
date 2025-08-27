import requests
from bs4 import BeautifulSoup
import time
import argparse
import os

def extract_and_save_result(html_content, index_number):
    """
    Parses the HTML content to extract result details and appends them to a text file.

    Args:
        html_content (str): The HTML content of the results page.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        details_table = soup.find('table', width='100%', class_='table table-striped')
        
        def find_detail(label_text):
            label_h5 = details_table.find('h5', string=label_text)
            if label_h5:
                value_td = label_h5.find_parent('tr').find_all('td')
                if len(value_td) > 2:
                    return value_td[2].get_text(strip=True)
            return 'N/A'

        examination = find_detail('Examination')
        year = find_detail('Year')
        name = find_detail('Name')
        school = find_detail('School/ Address')
        medium = find_detail('Medium')
        due_year = find_detail('Due Year')

        results_table = soup.find('table', class_='table table-striped table-bordered')
        subject = "N/A"
        grade = "N/A"
        if results_table:
            result_row = results_table.find_all('tr')
            if len(result_row) > 1:
                data_row = result_row[1]
                data_tds = data_row.find_all('td')
                if len(data_tds) > 1:
                    subject = data_tds[0].find('label').get_text(strip=True) if data_tds[0].find('label') else 'N/A'
                    grade = data_tds[1].find('label').get_text(strip=True) if data_tds[1].find('label') else 'N/A'

        result_string = (
            f"==================== Result Found ====================\n"
            f"Index Number: {index_number}\n"
            f"Examination: {examination}\n"
            f"Year: {year}\n"
            f"Name: {name}\n"
            f"School/ Address: {school}\n"
            f"Medium: {medium}\n"
            f"Due Year: {due_year}\n"
            f"Subject: {subject}\n"
            f"Grade: {grade}\n"
            f"======================================================\n\n"
        )
        
        with open('results.txt', 'a', encoding='utf-8') as f:
            f.write(result_string)
            print("Result successfully extracted and saved to 'results.txt'.")
            
    except Exception as e:
        print(f"An error occurred during HTML parsing or file saving: {e}")

def check_result(index_number):
    """
    Submits a POST request to check a specific index number.

    Args:
        index_number (int): The index number to check.

    Returns:
        tuple: A tuple containing a boolean (True if a valid result is found)
               and the full HTML content of the page.
    """
    url = "https://www.results.exams.gov.lk/viewresults.htm"
    payload = {
        'examSessionId': '613',
        'year': '2024',
        'typeTitle': 'General Information Technology Examination 2023,2024(2025)',
        'isAddIndexNeeded': 'N',
        'additionalFieldName': '',
        'comment': '',
        'indexNumber': str(index_number)
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        error_message = soup.find('div', class_='alert')

        if not error_message:
            return True, response.text
        else:
            return False, None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting: {e}")
        return False, None

def main():
    """
    Main function to parse command-line arguments and iterate through the index range.
    """
    parser = argparse.ArgumentParser(description='Check G.I.T. exam results for a range of index numbers.')
    parser.add_argument('--start', type=int, required=True, help='Starting index number of the search range.')
    parser.add_argument('--end', type=int, required=True, help='Ending index number of the search range (inclusive).')
    args = parser.parse_args()

    found_result_count = 0

    for i in range(args.start, args.end + 1):
        print(f"Checking index: {i}...")
        is_valid, page_content = check_result(i)

        if is_valid:
            print("Valid result found.")
            extract_and_save_result(page_content, i)
            found_result_count += 1
        else:
            print("No result found for this index.")
            time.sleep(0.5)

    print("\n" + "="*50)
    if found_result_count > 0:
        print(f"Search complete. Found {found_result_count} results in the specified range.")
    else:
        print("Search complete. No results found in the specified range.")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
