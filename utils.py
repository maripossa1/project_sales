import numpy as np

def generate_random_sales(min_val, max_val, size):
    # randit ynahi l9ima max_val
    return np.random.randint(min_val, max_val+1, size)



def get_quarter(month_num):
    if month_num in [1, 2, 3]:
        return 'Q1'
    elif month_num in [4, 5, 6]:
        return 'Q2'
    elif month_num in [7, 8, 9] :
        return 'Q3'
    else:
        return 'Q4'


if __name__ == '__main__':
    test = generate_random_sales(10, 100, 5)
    print("les donne ",test)

test_m = [1, 4, 7, 10, 12]
for m in test_m:
    quarter = get_quarter(m)
    print(f"{m} : {quarter}")
