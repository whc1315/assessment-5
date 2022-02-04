# This opens the "um-server-01.txt" file and saves it to a variable called log_file.
log_file = open("um-server-01.txt")


# This creates a function called sales_reports that takes in a variable, in this case it will be taking in a file, log_file here is just a placeholder.
def sales_reports(log_file):
    for line in log_file:  # This is a for loop that runs through the file line by line.
        # This sets a variable called line and removes any trailing characters or whitespace from each line.
        line = line.rstrip()
        # this sets a variable called day and makes it equal to the 1st and 4th item in line.
        day = line[0:3]
        # if day == "Tue":#this is an if statement with the condition that day must equal Tuesday. I commented it out
        if day == "Mon":  # This is the updated line to make day have to equal Monday
            print(line)  # This prints the lines that equal Mondays


# This runs the function through the "um-server-01.txt" file that was saved to the log_file variable.
sales_reports(log_file)
