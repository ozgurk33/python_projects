import re

def find_tel_nums(text):
    pattern =r"\+?\d{1,3}[-.\s]\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}"
 
    numbers = re.findall(pattern,text)
    return numbers

def find_emails(text):
    pattern =r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
 
    emails = re.findall(pattern,text)
    return emails

def check_if_email_valid(email):
    pattern =r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return bool(re.match(pattern,email))

def find_dates(text):
    pattern =r"\d{4}-\d{2}-\d{2}"
 
    dates = re.findall(pattern,text)
    return dates

if __name__ == "__main__":
    print(find_tel_nums("Please contact me at +1 (123) 456-7890 or via emial at john@example.com"))
    emails = find_emails("Please contact me at +1 (123) 456-7890 or via emial at john@example.com")
    print(emails)
    print(check_if_email_valid(emails[0]))
    print(find_dates("Date: 2023-06-08 1990-01-02"))
          

