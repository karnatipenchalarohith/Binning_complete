

from return_point_filename_lmin_lmax import return_point_filename_lmin_lmax as return_point_filename_lmin_lmax
# find point model cards
import os

def findPointModelCardsLengthWidth():
    current_location=os.getcwd()
    print(current_location)
    path = current_location
    files = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)) and 'ZZ' in i:
            files.append(i)


    all_point_cards_values=[]


    for item in files:
        point_cards_values=return_point_filename_lmin_lmax(item)
        all_point_cards_values.append(point_cards_values)

    print(files)
    print(len(files))
    print(all_point_cards_values)
    print(len(all_point_cards_values))
    return(all_point_cards_values)

