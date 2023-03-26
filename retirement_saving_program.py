import inquirer

print("This program helps you know how much you need to save each month given your retirement expenses and age.")
print("Please enter the following information in US dollars.")
def get_general_info():
    global country
    global monthly_salary
    global retirement_age
    global life_expectancy
    country = input("Country:")
    monthly_salary = input("Monthly salary: ")
    retirement_age = input("At what age do you want to retire?: ")
    life_expectancy = input("How many years do you expect to live?: ")

def calculate_retirement_savings():
    global retirement_years
    global monthly_expenses
    global retirement_expenses
    global saving_time
    global monthly_retirement_saving_amount
    global saving_percentage
    global saved_retirement
    retirement_years = int(life_expectancy) - int(retirement_age)
    monthly_expenses = input("Monthly expenses for when you retire: ")
    retirement_expenses = int(monthly_expenses) * 12 * int(retirement_years)
    saving_time = input("How many years do you want to save?: ")
    saved_retirement = input("How much have you saved for retirement?: ")
    monthly_retirement_saving_amount = (int(retirement_expenses) - int(saved_retirement) ) / (int(saving_time) * 12)
    saving_percentage = int(monthly_retirement_saving_amount) / int(monthly_salary) * 100
    if int(monthly_retirement_saving_amount) > int(monthly_salary):
        print("You need to save more than you earn. You need to earn more or retire later.")
    else:
        print("You can retire from", retirement_age, "if you save", monthly_retirement_saving_amount, "per month.", "The results are not adjusted for inflation.")
        print("You need to save", saving_percentage, "percent of your monthly salary.")

def calculate_sinking_fund():
    global sinking_fund_name
    global sinking_fund_amount
    global sinking_fund_time
    global sinking_fund_monthly_saving_amount
    sinking_funds_prompt = input("Do you want to save for a sinking fund? (y/n): ")
    if sinking_funds_prompt == "y":
        sinking_fund_name = input("What is the name of the sinking fund?: ")
        sinking_fund_amount = input("How much do you want to save for the sinking fund?: ")
        sinking_fund_time = input("How many years do you want to save for the sinking fund?: ")
        sinking_fund_monthly_saving_amount = int(sinking_fund_amount) / (int(sinking_fund_time) * 12)
        print("You need to save", sinking_fund_monthly_saving_amount, "per month for the", sinking_fund_name, "sinking fund.")
    else:
        sinking_fund_monthly_saving_amount = 0

def calculate_health_emergencies():
    global health_emergency_yearly_amount
    global health_emergency_time
    global health_emergency_total_amount
    global health_emergency_monthly_saving_amount
    global health_emergencies_percentage
    global saved_health_emergencies
    health_emgergencies_prompt = input("Do you want to save for health emergencies for when you retire? (y/n): ")
    if health_emgergencies_prompt == "y":
        print("Health consumption expenditures per capita, U.S. dollars, PPP adjusted, 2020 or nearest year is $5,736 per person on average in developed countries.")
        healthcare_emergency_yearly_amount_prompt = input("Do you want to calculate your health emergencies savings based on this number? (y/n):")
        if healthcare_emergency_yearly_amount_prompt == "y":
            health_emergency_yearly_amount = 5736
        else:
            health_emergency_yearly_amount = input("How much do you plan to spend on health per year after retirement?: ")
            health_emergency_time = input("How many years do you want to save for health emergencies?: ")
            health_emergency_total_amount = int(health_emergency_yearly_amount) * int(retirement_years)
            saved_health_emergencies = input("How much have you saved for health emergencies?: ")
            health_emergency_monthly_saving_amount = (int(health_emergency_total_amount) - int(saved_health_emergencies)) / (int(health_emergency_time) * 12)
            health_emergencies_percentage = int(health_emergency_monthly_saving_amount) / int(monthly_salary) * 100
            print("You need to save", health_emergency_monthly_saving_amount, "per month for health emergencies.")
            print("That's", health_emergencies_percentage, "percent of your monthly salary for health emergencies.")

def calculate_total_monthly_saving():
    global total_monthly_saving
    total_monthly_saving = int(monthly_retirement_saving_amount) + int(sinking_fund_monthly_saving_amount) + int(health_emergency_monthly_saving_amount)

def calculate_remaining_income():
    global remaining_income
    global remaining_income_percentage
    remaining_income = int(monthly_salary) - int(total_monthly_saving)
    print("You have", remaining_income, "left after saving for retirement, sinking funds, and health emergencies.")

    def calculate_remaining_income_percentage():
        remaining_income_percentage = int(remaining_income) / int(monthly_salary) * 100
        return remaining_income_percentage
        print("That's", remaining_income_percentage, "percent of your monthly salary left after saving for retirement, sinking funds, and health emergencies.")
    calculate_remaining_income_percentage()

def calculate_remaining_income_after_tax():
    global remaining_income_after_tax
    global remaining_income_after_tax_percentage
    tax_rate = input("What is your tax rate? (in decimal form): ")
    remaining_income_after_tax = int(remaining_income) * (1 - float(tax_rate))
    print("You have", remaining_income_after_tax, "left after saving for retirement, sinking funds, and health emergencies after tax.")
    
    def calculate_remaining_income_after_tax_percentage():
        remaining_income_after_tax_percentage = int(remaining_income_after_tax) / int(monthly_salary) * 100
        return remaining_income_after_tax_percentage
        print("That's", remaining_income_after_tax_percentage, "percent of your monthly salary left after saving for retirement, sinking funds, and health emergencies after tax.")
    calculate_remaining_income_after_tax_percentage()

def main ():
    get_general_info()
    calculate_retirement_savings()
    calculate_sinking_fund()
    calculate_health_emergencies()
    calculate_total_monthly_saving()
    calculate_remaining_income()
    calculate_remaining_income_after_tax()
    print("Do you want to recalulate your results? (y/n):")
    recalculate = input()
    if recalculate == "y":
        print("what do you want to recalculate (retirement, sinking fund, health emergencies, all):")
        recalculate = input().strip()
        if recalculate == "retirement":
            calculate_retirement_savings()
        elif recalculate == "sinking fund":
            calculate_sinking_fund()
        elif recalculate == "health emergencies":
            calculate_health_emergencies()
        elif recalculate == "all":
            calculate_retirement_savings()
            calculate_sinking_fund()
            calculate_health_emergencies()
        else:
            print("Please enter a valid input.")
    else:
        print("Thank you for using the saving planner calculator.")
main()
