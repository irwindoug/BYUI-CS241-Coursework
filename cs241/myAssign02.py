def main():
    file = get_file()
    print()

    results = calc_numbers(file[1:],get_header(file))

    print("The average commercial rate is: " + str(results[0]) + "\n")

    print("The highest rate is:\n" + company_info(file[results[1]])+"\n")

    print("The lowest rate is:\n" + company_info(file[results[2]]))


def get_file():
    return open(input("Please enter the data file: "),"r").readlines()

def get_header(file):
    column = 0
    headers = file[0].split(",")
    for index, header in enumerate(headers):
        if header == "comm_rate":
            column = index
    return column

def calc_numbers(file, column_number):
    low_number = 0
    low_index = 0
    high_number = 0
    high_index = 0
    total = 0

    for index, line in enumerate(file):
        company = line.split(",")
        comm_rate = float(company[column_number])
        if index == 0:
            low_number = comm_rate
        elif comm_rate < low_number:
            low_number = comm_rate
            low_index = index+1
        elif comm_rate > high_number:
            high_number = comm_rate
            high_index = index+1
        total += comm_rate
    
    total = total/len(file)
    return[total, high_index, low_index]

def company_info(info):

    company = info.split(",")
    return (("%s (%d, %s) - $%s")%(company[2], int(company[0]), company[3], float(company[6])))
    

if __name__ == "__main__":
    main()