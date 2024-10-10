from datetime import datetime, timedelta

def generate_date_ranges(start_date, end_date):
    date_ranges = []
    current_start = start_date

    while current_start < end_date:
        current_end = current_start + timedelta(days=num_days)
        if current_end > end_date:
            current_end = end_date
        
        date_ranges.append(f"ARRIVE_DATE >= DEP_DATE('{current_start.strftime('%d-%b-%y')}', 'dd-MON-yy') AND "
                           f"ARRIVE_DATE < DEP_DATE('{current_end.strftime('%d-%b-%y')}', 'dd-MON-yy')")
        
        current_start = current_end

    return date_ranges

def create_scripts(start_date, end_date):
    date_ranges = generate_date_ranges(start_date, end_date)
    
    template_script = """
    set markup csv on;

    spool {filename};

    SELECT * FROM TEST_TABLE_OF_PROJECT WHERE {date_range};

    spool off;
    """
    
    script_filenames = []

    for date_range in date_ranges:
        from_date = date_range.split('>= DEP_DATE(\'')[1].split('\',')[0]
        filename = f"{from_date}.csv"
        script_content = template_script.format(filename=filename, date_range=date_range)
        script_filename = f"script_{from_date}.sql"
        script_filenames.append(script_filename)
        
        with open(script_filename, 'w') as file:
            file.write(script_content)

    # Create master script to run all single scripts
    with open('run_all_scripts.sql', 'w') as master_script:
        for script_filename in script_filenames:
            master_script.write(f"@{script_filename}\n")

# User input for dates
start_date_input = input("Enter start date (YYYY-MM-DD): ")
end_date_input = input("Enter end date (YYYY-MM-DD): ")
num_days = int(input("Enter number of days to create range: "))

start_date = datetime.strptime(start_date_input, '%Y-%m-%d')
end_date = datetime.strptime(end_date_input, '%Y-%m-%d')


create_scripts(start_date, end_date)
