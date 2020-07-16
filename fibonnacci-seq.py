def fibonnaci_seq(month):
    if(month == 0 or month == 1):
        return 2;
    else:
        return fibonnaci_seq(month-1)+fibonnaci_seq(month-2)

total_rabbits = fibonnaci_seq(6)
print(f'Rabbits in 6 months {total_rabbits}')