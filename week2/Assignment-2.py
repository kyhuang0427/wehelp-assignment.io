print("=== Task 1 ===")
def find_and_print(messages):

    older_than_17 = []

    for name, message in messages.items():
        if "18 years old" in message or "college student" in message or "legal age" in message or "vote" in message:
            older_than_17.append(name)  
    
    for name in older_than_17:
        print(name)

find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})
print("=== Task 2 ===")
def calculate_sum_of_bonus(data):
    exchange_rate = 30
    bonus_sum = 0
    
    for employee in data["employees"]:
        salary = employee["salary"]
        performance = employee["performance"]
        role = employee["role"]
        
        if isinstance(salary, str) and salary.endswith("USD"):
            salary = int(salary[:-3]) * exchange_rate
        elif isinstance(salary, str):
            salary = int(salary.replace(",", ""))
        
        bonus = 0
        
        if salary >= 50000:
            if performance == "above average":
                bonus = 2000
            elif performance == "average":
                bonus = 1500
            elif performance == "below average":
                bonus = 1000
        else:
            if performance == "above average":
                bonus = 1000
            elif performance == "average":
                bonus = 800
            elif performance == "below average":
                bonus = 500
        
        if role == "CEO":
            bonus *= 2
        elif role == "Engineer":
            bonus *= 1.5
        elif role == "Sales":
            bonus *= 1.7
        
        bonus_sum += bonus
        
    print("{:.0f}".format(bonus_sum))

calculate_sum_of_bonus({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        },
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"
        },
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }
    ]
})
print("=== Task 3 ===")
def func(*data):
    middle_names = []
    unique_middle_name = "沒有"
    
    for name in data:
        
        middle_names.append(name[1])
    
    for name in data:
        if middle_names.count(name[1])==1:
            unique_middle_name = name
            break

    print(unique_middle_name)

func("彭⼤牆", "王明雅", "吳明"); 
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); 
print("=== Task 4 ===")
def getNumber(index):

    if index % 2 == 0:
        answer = 3 * (index / 2)
        print("{:.0f}".format(answer))
    else:
        answer = 1 + 3 * ((index + 1) / 2)
        print("{:.0f}".format(answer))

getNumber(1); 
getNumber(5); 
getNumber(10); 
print("=== Task 5 ===")
def find_index_of_car(seats, status, number):
    
    initial_fit_index = -1
    fit_index = []
    fit_value = []

    for i in range(len(seats)):
        if status[i] == 1 and seats[i] >= number:
            
            fit_index.append(i)
            fit_value.append(seats[i]-number)

    for j in range(len(fit_index)):

        min_fit_value = min(fit_value)

        if fit_value[j] == min_fit_value:
            initial_fit_index = fit_index[j] 

    print(initial_fit_index)

find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) 
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) 
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) 


