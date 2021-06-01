from typing import List, Tuple, TextIO
import os
import easygui

#Made by Luc Ryan for Stratus Aeronatuics 

#INDEX FOR COLUMNS IN DATA
BBB_time = 0

Insturment_value = 1

Piksi_time = 2


#These are the prompt questions for the inputs
new_str = "\n 1 = BBB Time \n 2 = Insturment Value \n 3 = Seconds Value (Piksi) \n 4 = End Script"

other_str = "\n 1 =  Yes \n 2 = No"

other_str2 = "Please enter a value that you would like to find the index for: "


def input_prompt() -> int:
    #This is an input prompt to activate the script
    
    prompt1 = 'Would you like to activate this script?: '
        
    print(other_str)
    
    first_question = input(prompt1)
    
    num = int(first_question)
    
    return num



def delta_average(t: List[float]) -> List[float]:
    #This is a function that takes a list and returns a average of change.
    str1 = 'Average of change list: '
    v = [t[i+1]-t[i] for i in range(len(t)-1)]
    
    
    return str1, v



def delta_max(alist: List[float]) -> float:
    #A function that takes a list of BBB time readings and returns the 2nd max of the list
    
    largest = alist[0]
    
    second_largest = alist[0]
    
    for i in range(len(alist)):
        
        if alist[i] > second_largest:
            
            second_largest = alist[i]
            
        if alist[i] > largest:
            
            tmp = second_largest
            
            second_largest = largest
            
            largest = tmp   

    
    print('Second Largest Delta T Value:', largest)


def index(loi: List[float]) -> int:
    #A function that takes a list of floats and finds the index for the specified value.
    
    print(other_str)
    
    the_prompt = 'Please enter a number from the following options if you would like to know the index of the max: '
    
    question1 = input(the_prompt)
    
    
    answer1 = int(question1)
    
    
    found_index = -1
    
    num_elements = len(loi)
    
    cur_index = 0
    
    if answer1 == 1:
        
        question2 = input(other_str2)
        
        to_find = int(question2)
        
        while cur_index < num_elements and found_index == -1:
            
            if loi[cur_index] == to_find:
                
                found_index = cur_index
                
                cur_index+=1
                
                
    elif answer1 == 2:
        
        return None



    return print('Second Highest Index of Delta T Value:', found_index)



def make_list1(filename: str) -> List[float]:
    #This is a function that takes BBB timestamps and returns a list of the time converted into seconds
    
    BBB_time_readings = []

    file_handle = open(filename, 'r')
    
    line_range = file_handle.readlines()[1:]

    for line in line_range:
        
        
        line = line.rstrip()
        
        seperate_line = line.split(',')
        
        list1 = (seperate_line[BBB_time])
        
        time_split = list1.split(":")
        
        
        for x in time_split:
            
            float1 = float(time_split[0])
            
            float2 = float(time_split[1])    
            
            
            if float1 != 0:
                
                float1 *= 60
                
                total_seconds = float1 + float2 
                
                
            else:
                
                total_seconds = float2
                
                
                
                
        format_seconds = "{:.3f}".format(total_seconds)
        
        updated_format = float(format_seconds)
        
        BBB_time_readings.append(updated_format)

        
    file_handle.close()
    
    return BBB_time_readings




def make_list2(filename:str) -> List[float]:
    #This is a function that opens an excel file and takes the data in Column B, insturment values, and returns a list of float values for that insturment.
    
    insturment_readings = []

    file_handle = open(filename, 'r')
    
    line_range = file_handle.readlines()[1:]

    for line in line_range:
        
        line = line.rstrip()
        
        seperate_line = line.split(',')
        
        list1 = float(seperate_line[Insturment_value])
        
        format_vals = "{:.3f}".format(list1)
        
        updated_float = float(format_vals)
        
        insturment_readings.append(updated_float)

        
    file_handle.close()
    
    return insturment_readings



def make_list3(filename:str) -> List[float]:
    #This is a function that opens an excel file and takes the data in Column B, insturment values, and returns a list of float values for that insturment.
    
    piksi_readings = []

    file_handle = open(filename, 'r')
    
    line_range = file_handle.readlines()[1:]

    for line in line_range:
        
        line = line.rstrip()
        
        seperate_line = line.split(',')
        
        list1 = float(seperate_line[Piksi_time])
        
        format_vals = "{:.3f}".format(list1)
        
        updated_float = float(format_vals)
        
        piksi_readings.append(updated_float)

        
    file_handle.close()
    
    return piksi_readings






def open_file():
    #A function that has inputs to open a specified file and other options for analyzing
    
    while_loop = input_prompt()
    
    while while_loop != 2:
        
        prompt1 = 'Pick a number for the following options: '
    
        prompt2 = 'Would you like to analyze this list?: '
    
        print(new_str)
    
        first_question = input(prompt1)
    
        num = int(first_question)
    
    
        if num == 1:
            #This one is usually for the timestamp
            
            filename = easygui.fileopenbox("Select folder containing binary files to be converted")
            
            list_maker1 = make_list1(filename)
            
            print(other_str)
            
            question1 = input(prompt2)
            
            answer1 = int(question1)
    
            
            if answer1 == 1:
                print('The original values converted into seconds is : ', list_maker1)
                
                delta_max1= delta_max(list_maker1)
                
                delta_average1 = delta_average(list_maker1)
                
                print(delta_max1)
                
                index1 = index(list_maker1)
                
                print(index1)
                   


            elif answer1 == 2:
                
                print(list_maker1)
        
        
        
        elif num == 2:
            #For insturment values
            
            filename = easygui.fileopenbox("Select folder containing binary files to be converted")
            
            list_maker2 = make_list2(filename)
            
            print(other_str)
            
            question2 = input(prompt2)
            
            answer2 = int(question2)
            
    
            
            if answer2 == 1:
                
                delta_max2 = delta_max(list_maker2)
                
                delta_average2 = delta_average(list_maker2)
                
                print(delta_max2, delta_average2)
                
                index2 = index(list_maker2)
                
                print(index2)
    
            elif answer2 == 2:
                
                print(list_maker2)
                
        elif num == 3:
            #Usually for piksi
            
            filename = easygui.fileopenbox("Select folder containing binary files to be converted")
            
            list_maker3 = make_list3(filename)
            
            print(other_str)
            
            question3 = input(prompt2)
            
            answer3 = int(question3)
            
            if answer3 == 1:
                
                delta_max3 = delta_max(list_maker3)
                
                delta_average3 = delta_average(list_maker3) 
                
                print(delta_max3, delta_average3)
                
                index3 = index(list_maker3)
                
                print(index3)
                
            elif question3 == 2:
                
                print(list_maker3)
            
        elif num == 4:
            print('')
            break

open_file()


