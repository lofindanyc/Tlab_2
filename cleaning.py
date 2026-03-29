def clean_heartrate_data(data: list) -> tuple:
    cleaned = []
    for line in data :
        if line.replace('\n', '') != '' and line.replace('\n', '') != 'NO DATA':
        
            cleaned.append(int(line.replace('\n','')))
    print(cleaned)
    return cleaned