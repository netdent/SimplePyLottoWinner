#PyLottoWinner.py
import random

LOTTO_FILE_DATA = "./lres/alllottery_numbers_1_778.txt"

bat_count = input("How many times will you challenge ? ")


#function for load a lottery file and make list
def load_win_list(file_name):
    flott = open(file_name, 'r')    #open the lotto won list file
    all_nums = []

    while True:
        numbers = flott.readline()
        if not numbers: break
        all_nums += numbers.split()
           
    flott.close()                   #close file
    all_nums = list(map(int, all_nums)) #convert string list to int list
    #print(all_nums)
    return all_nums

#function for getting N numbers randomly in list 
def get_random_numbers(num_list, size):
    #rand_smpl = [num_list[ii] for ii in sorted(random.sample(range(len(num_list)), size))]
    rand_smpl = [num_list[ii] for ii in random.sample(num_list, size)]
    #rand_smpl = random.sample(num_list, size)
    set_nums = set(rand_smpl)
    if(len(set_nums) != size): #if duplicated num is exist, it will try again..
        rand_smpl = get_random_numbers(num_list, size)

    rand_smpl.sort()
    
    return rand_smpl


#load won numbers from lotto file
load_num = load_win_list(LOTTO_FILE_DATA)

for ii in range(int(bat_count)):
    today_num = get_random_numbers(load_num, 6)
    print(today_num)

