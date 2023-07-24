
import pandas as pd

#bins_array=[{'binname': 'bin1.txt', 'lmin': '1e-005', 'lmax': '2e-005', 'wmin': '1.003e-005', 'wmax': '90.003e-05'}, {'binname': 'bin2.txt', 'lmin': '1.2e-006', 'lmax': '1.2e-006', 'wmin': '1.003e-005', 'wmax': '90.003e-05'}, {'binname': 'bin3.txt', 'lmin': '5e-007', 'lmax': '5e-007', 'wmin': '1.003e-005', 'wmax': '90.003e-05'}, {'binname': 'bin4.txt', 'lmin': '1.8e-07', 'lmax': '1.8e-07', 'wmin': '1.003e-005', 'wmax': '90.003e-05'}, {'binname': 'bin5.txt', 'lmin': '1e-005', 'lmax': '1e-005', 'wmin': '1.23e-006', 'wmax': '1.003e-005'}, {'binname': 'bin6.txt', 'lmin': '1.2e-006', 'lmax': '1.2e-006', 'wmin': '1.23e-006', 'wmax': '1.003e-005'}, {'binname': 'bin7.txt', 'lmin': '5e-007', 'lmax': '5e-007', 'wmin': '1.23e-006', 'wmax': '1.003e-005'}, {'binname': 'bin8.txt', 'lmin': '1.8e-07', 'lmax': '1.8e-07', 'wmin': '1.23e-006', 'wmax': '1.003e-005'}, {'binname': 'bin9.txt', 'lmin': '1e-005', 'lmax': '1e-005', 'wmin': '5.3e-007', 'wmax': '1.23e-006'}, {'binname': 'bin10.txt', 'lmin': '1.2e-006', 'lmax': '1.2e-006', 'wmin': '5.3e-007', 'wmax': '1.23e-006'}, {'binname': 'bin11.txt', 'lmin': '5e-007', 'lmax': '5e-007', 'wmin': '5.3e-007', 'wmax': '1.23e-006'}, {'binname': 'bin12.txt', 'lmin': '1.8e-07', 'lmax': '1.8e-07', 'wmin': '5.3e-007', 'wmax': '1.23e-006'}, {'binname': 'bin13.txt', 'lmin': '1e-005', 'lmax': '1e-005', 'wmin': '2.2e-07', 'wmax': '5.3e-007'}, {'binname': 'bin14.txt', 'lmin': '1.2e-006', 'lmax': '1.2e-006', 'wmin': '2.2e-07', 'wmax': '5.3e-007'}, {'binname': 'bin15.txt', 'lmin': '5e-007', 'lmax': '5e-007', 'wmin': '2.2e-07', 'wmax': '5.3e-007'}, {'binname': 'bin16.txt', 'lmin': '1.8e-07', 'lmax': '1.8e-07', 'wmin': '2.2e-07', 'wmax': '5.3e-007'}]

# gets input from finPointModelCardsLengthWidth and findInputBinsLminLmaxWminMax
# gives output to matching of L

def RebinMatchingBinsToPointModelCard(bins_array,point_model_cards):


    #bins_array=[{'binname': 'bin1.txt', 'lmin': '1e-005', 'lmax': '2e-05', 'wmin': '1.003e-005', 'wmax': '90.003e-05'}, {'binname': 'bin2.txt', 'lmin': '1.2e-006', 'lmax': '1e-005', 'wmin': '1.003e-005', 'wmax': '90.003e-05'}, {'binname': 'bin3.txt', 'lmin': '5e-007', 'lmax': '1.2e-006', 'wmin': '1.003e-005', 'wmax': '90.003e-05'}, {'binname': 'bin4.txt', 'lmin': '1.8e-07', 'lmax': '5e-007', 'wmin': '1.003e-005', 'wmax': '90.003e-05'}, {'binname': 'bin5.txt', 'lmin': '1e-005', 'lmax': '2e-05', 'wmin': '1.23e-006', 'wmax': '1.003e-005'}, {'binname': 'bin6.txt', 'lmin': '1.2e-006', 'lmax': '1e-005', 'wmin': '1.23e-006', 'wmax': '1.003e-005'}, {'binname': 'bin7.txt', 'lmin': '5e-007', 'lmax': '1.2e-006', 'wmin': '1.23e-006', 'wmax': '1.003e-005'}, {'binname': 'bin8.txt', 'lmin': '1.8e-07', 'lmax': '5e-007', 'wmin': '1.23e-006', 'wmax': '1.003e-005'}, {'binname': 'bin9.txt', 'lmin': '1e-005', 'lmax': '2e-05', 'wmin': '5.3e-007', 'wmax': '1.23e-006'}, {'binname': 'bin10.txt', 'lmin': '1.2e-006', 'lmax': '1e-005', 'wmin': '5.3e-007', 'wmax': '1.23e-006'}, {'binname': 'bin11.txt', 'lmin': '5e-007', 'lmax': '1.2e-006', 'wmin': '5.3e-007', 'wmax': '1.23e-006'}, {'binname': 'bin12.txt', 'lmin': '1.8e-07', 'lmax': '5e-007', 'wmin': '5.3e-007', 'wmax': '1.23e-006'}, {'binname': 'bin13.txt', 'lmin': '1e-005', 'lmax': '2e-05', 'wmin': '2.2e-07', 'wmax': '5.3e-007'}, {'binname': 'bin14.txt', 'lmin': '1.2e-006', 'lmax': '1e-005', 'wmin': '2.2e-07', 'wmax': '5.3e-007'}, {'binname': 'bin15.txt', 'lmin': '5e-007', 'lmax': '1.2e-006', 'wmin': '2.2e-07', 'wmax': '5.3e-007'}, {'binname': 'bin16.txt', 'lmin': '1.8e-07', 'lmax': '5e-007', 'wmin': '2.2e-07', 'wmax': '5.3e-007'}]

    #point_model_cards=[{'point_filename': 'Width_0.22_length_0.18_after_bins_joined.txt', 'length': '1.8e-07', 'width': '2.2e-07'}, {'point_filename': 'Width_0.22_length_0.5_after_bins_joined.txt', 'length': '5e-07', 'width': '2.2e-07'}, {'point_filename': 'Width_0.22_length_1.2_after_bins_joined.txt', 'length': '1.2e-06', 'width': '2.2e-07'}, {'point_filename': 'Width_0.22_length_10.0_after_bins_joined.txt', 'length': '1e-05', 'width': '2.2e-07'}, {'point_filename': 'Width_0.22_length_20.0_after_bins_joined.txt', 'length': '2e-05', 'width': '2.2e-07'}, {'point_filename': 'Width_0.53_length_0.18_after_bins_joined.txt', 'length': '1.8e-07', 'width': '5.3e-07'}, {'point_filename': 'Width_0.53_length_0.5_after_bins_joined.txt', 'length': '5e-07', 'width': '5.3e-07'}, {'point_filename': 'Width_0.53_length_1.2_after_bins_joined.txt', 'length': '1.2e-06', 'width': '5.3e-07'}, {'point_filename': 'Width_0.53_length_10.0_after_bins_joined.txt', 'length': '1e-05', 'width': '5.3e-07'}, {'point_filename': 'Width_0.53_length_20.0_after_bins_joined.txt', 'length': '2e-05', 'width': '5.3e-07'}, {'point_filename': 'Width_1.23_length_0.18_after_bins_joined.txt', 'length': '1.8e-07', 'width': '1.23e-06'}, {'point_filename': 'Width_1.23_length_0.5_after_bins_joined.txt', 'length': '5e-07', 'width': '1.23e-06'}, {'point_filename': 'Width_1.23_length_1.2_after_bins_joined.txt', 'length': '1.2e-06', 'width': '1.23e-06'}, {'point_filename': 'Width_1.23_length_10.0_after_bins_joined.txt', 'length': '1e-05', 'width': '1.23e-06'}, {'point_filename': 'Width_1.23_length_20.0_after_bins_joined.txt', 'length': '2e-05', 'width': '1.23e-06'}, {'point_filename': 'Width_10.03_length_0.18_after_bins_joined.txt', 'length': '1.8e-07', 'width': '1.003e-05'}, {'point_filename': 'Width_10.03_length_0.5_after_bins_joined.txt', 'length': '5e-07', 'width': '1.003e-05'}, {'point_filename': 'Width_10.03_length_1.2_after_bins_joined.txt', 'length': '1.2e-06', 'width': '1.003e-05'}, {'point_filename': 'Width_10.03_length_10.0_after_bins_joined.txt', 'length': '1e-05', 'width': '1.003e-05'}, {'point_filename': 'Width_10.03_length_20.0_after_bins_joined.txt', 'length': '2e-05', 'width': '1.003e-05'}, {'point_filename': 'Width_900.03_length_0.18_after_bins_joined.txt', 'length': '1.8e-07', 'width': '0.00090003'}, {'point_filename': 'Width_900.03_length_0.5_after_bins_joined.txt', 'length': '5e-07', 'width': '0.00090003'}, {'point_filename': 'Width_900.03_length_1.2_after_bins_joined.txt', 'length': '1.2e-06', 'width': '0.00090003'}, {'point_filename': 'Width_900.03_length_10.0_after_bins_joined.txt', 'length': '1e-05', 'width': '0.00090003'}, {'point_filename': 'Width_900.03_length_20.0_after_bins_joined.txt', 'length': '2e-05', 'width': '0.00090003'}]

    new_bins_array=[]



    df = pd.DataFrame(bins_array)

    print(df)


    df2 = pd.DataFrame(point_model_cards)

    print(df2)




        #print(name)

    new_dic_all=[]
    new_dic={}
    i=0
    for index, row in df.iterrows():
        print(row['binname'])
        i=i+1
        print(i)
        print(row['lmin'])
        print(row['wmin'])
        print(type(row['lmin']))
        print(type(row['wmin']))
        print((float(row['lmin'])))
        print((float(row['wmin'])))
        samebin=[]


        for index2, row2 in df2.iterrows():
            #print(row2['point_filename'])
            print(row2['length'])
            print(row2['width'])
            print((float(row2['length'])))
            print((float(row2['width'])))
            print((float(row['lmin'])))
            print((float(row['wmin'])))
            if float(row2['length']) <= float(row['lmax']) and float(row2['length']) >= float(row['lmin']) and float(row2['width']) <= float(row['wmax']) and float(row2['width']) >= float(row['wmin']):
                print("hi")
                print(row2['length'])
                print(row['lmax'])
                print(row['lmin'])
                print(row2['width'])
                print(row['wmax'])
                print(row['wmin'])
                print("point_model_card {} is in bin {}".format(row2['point_filename'],row['binname']))
                samebin.append(row2['point_filename'])

        new_dic = {row['binname']:samebin}
        new_dic_all.append(new_dic)



    print(new_dic_all)
    return(new_dic_all)


'''
    bint={'binname':item}
    new_bins_array
    
                print("point_model_card {row2['point_filename']} is in bin {row['binname'])}".format(row['binname']) )

'''

'''
'''