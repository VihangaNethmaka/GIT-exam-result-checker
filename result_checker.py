# Before running this script, you must install the required libraries.
# Open your terminal or command prompt and run:
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import time

def extract_and_save_result(html_content, index_number):
    """
    Parses the HTML content to extract all result details and saves them to a file.

    Args:
        html_content (str): The HTML content of the results page.
        index_number (int): The index number associated with the result.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the main table containing all the details
        details_table = soup.find('table', width='100%', class_='table table-striped')
        
        # Helper function to find data for a given label
        def find_detail(label_text):
            label_h5 = details_table.find('h5', string=label_text)
            if label_h5:
                # Find the parent row and get the third td for the value
                value_td = label_h5.find_parent('tr').find_all('td')
                if len(value_td) > 2:
                    return value_td[2].get_text(strip=True)
            return 'N/A'

        # Extract all the required fields using the helper function
        examination = find_detail('Examination')
        year = find_detail('Year')
        name = find_detail('Name')
        school = find_detail('School/ Address')
        medium = find_detail('Medium')
        nic_number = find_detail('NIC Number')
        due_year = find_detail('Due Year')

        # Find the 'Results' table and extract the subject and grade
        results_table = soup.find('table', class_='table table-striped table-bordered')
        subject = "N/A"
        grade = "N/A"
        if results_table:
            # Find the first row in the table body that contains the subject and grade
            # The structure is now confirmed to have the data in a <tr> with <td>s.
            result_row = results_table.find_all('tr')
            if len(result_row) > 1: # The first row is the header, so we look at the second one
                data_row = result_row[1]
                data_tds = data_row.find_all('td')
                if len(data_tds) > 1:
                    # The subject and grade are inside <label> tags within the <td>s
                    subject = data_tds[0].find('label').get_text(strip=True) if data_tds[0].find('label') else 'N/A'
                    grade = data_tds[1].find('label').get_text(strip=True) if data_tds[1].find('label') else 'N/A'

        # Format the extracted data
        result_string = (
            f"==================== Result Found ====================\n"
            f"Examination: {examination}\n"
            f"Year: {year}\n"
            f"Index Number: {index_number}\n"
            f"Name: {name}\n"
            f"School/ Address: {school}\n"
            f"Medium: {medium}\n"
            f"NIC Number: {nic_number}\n"
            f"Due Year: {due_year}\n"
            f"Subject: {subject}\n"
            f"Grade: {grade}\n"
            f"======================================================\n\n"
        )
        
        # Save the formatted string to a new file named 'results.txt'
        # Use 'a' mode to append to the file if it already exists
        with open('results.txt', 'a', encoding='utf-8') as f:
            f.write(result_string)
            print(f"Result for index {index_number} successfully extracted and saved to 'results.txt'.")
            
    except Exception as e:
        print(f"An error occurred while parsing the HTML or saving the file: {e}")

def check_result(index_number):
    """
    Submits a POST request with the given index number and checks for a successful result.

    Args:
        index_number (int): The index number to check.

    Returns:
        bool: True if a result is found, False otherwise.
        str: The full HTML content of the page if a result is found, None otherwise.
    """
    url = "https://www.results.exams.gov.lk/viewresults.htm"
    # The form data from the website's HTML
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
        # Make the POST request to the server
        response = requests.post(url, data=payload)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for a specific element that indicates an invalid index.
        # We look for a 'div' with class 'alert' which contains the error message.
        error_message = soup.find('div', class_='alert')

        # If the error message is not found, it's likely a valid result.
        if not error_message:
            return True, response.text
        else:
            # If an error message is present, it means the index was not found.
            return False, None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting: {e}")
        return False, None

# Define the range of possible index numbers
start_index = 2144000
end_index = 2148999

found_result = False

for i in range(start_index, end_index + 1):
    print(f"Checking index number: {i}...")

    is_valid_result, page_content = check_result(i)

    if is_valid_result:
        # Extract the name to print to the terminal
        soup = BeautifulSoup(page_content, 'html.parser')
        name_label = soup.find('h5', string='Name')
        name = 'N/A'
        if name_label:
            name_td = name_label.find_parent('tr').find_all('td')
            if len(name_td) > 2:
                name = name_td[2].get_text(strip=True)
        
        print(f"Valid Output - {name}")
        extract_and_save_result(page_content, i)
        found_result = True
    else:
        print("Invalid Output")
        # Optional: Add a small delay between requests to avoid overwhelming the server
        time.sleep(0.5)

if not found_result:
    print("\n" + "="*50)
    print("Search complete. No result page was found in the specified range.")
    print("This could mean your index number is outside the range or the website's response has changed.")
    print("="*50 + "\n")
