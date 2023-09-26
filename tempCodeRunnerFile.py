def extract_landmark(address):
    # Implement a function to extract the landmark from the hospital address
    # You may use regular expressions or other techniques based on your data structure
    # For example, if the landmark is always after the last comma, you can use:
    parts = address.split(',')
    if len(parts) >= 2:
        return parts[-2].strip()  # Assuming landmark is the second-to-last part
    else:
        return ""