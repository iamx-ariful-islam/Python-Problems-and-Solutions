from datetime import datetime


data = [
    [1, '102', 'Smith', 'USA', '12345', 120.0, '29.03.2023'],
    [2, '103', 'David', 'UK', '56789', 220.0, '27.03.2023'],    
    [3, '104', 'Mark', 'India', '98765', 350.0, '28.03.2023'],
    [4, '105', 'Jone', 'Bangladesh', '54321', 250.0, '28.03.2023'],
    [5, '101', 'Malek', 'Dhaka', '01712345678', 500.0, '22.09.2025'],
    [6, '103', 'David', 'UK', '56789', 220.0, '29.04.2023'],
    [7, '103', 'David', 'UK', '56789', 220.0, '29.03.2023'],
]

# one-liner sort: room ascending, date descending
sorted_data = sorted(data, key=lambda x: (x[1], -datetime.strptime(x[6], '%d.%m.%Y').timestamp()))

# print result
for row in sorted_data:
    print(row)