#open input file to read input
i_file =open("sample_input.txt","r")
#open output file to write output
o_file = open("output.txt","w+")
goodies={}
o_list=[]
#reading input file
for f in i_file:
    idx_toRead_price=f.index(":")
    print(f[idx_toRead_price+1:].strip())
    print(f[:idx_toRead_price])
    goodies[f[:idx_toRead_price]]=f[idx_toRead_price+1:].strip()
#to print goodies    
print(goodies)
#list of prices 
prices_alone=list(goodies.values())


prices_alone=[int(i)for i in prices_alone]

#sorted list in descending order to get prices to be distributed in order
prices_alone.sort(reverse=True)
print(prices_alone)

#taking the inputs
num_of_emp=int(input("Enter number of employees: "))

len_considered=(len(prices_alone)-num_of_emp)

print(len_considered)

#finding minimum diff btwn highest and lowest
for i in range(len_considered):
    max_price=prices_alone[i]
    min_price=prices_alone[num_of_emp+i]
    if i == 0:
        diff=max_price-min_price
        idx_choosen=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        idx_choosen=i

choosen_prices=prices_alone[idx_choosen:num_of_emp+idx_choosen]

#difference btwn high and low price
diff=max(choosen_prices)-min(choosen_prices)
print("diff",diff)

cnt=0
for key,value in goodies.items():
    prices_alone[cnt]
    print(value)
    if int(value)in choosen_prices and cnt<num_of_emp:
        str1=key+": "+value
        #list for output
        o_list.append(str1)
        cnt+=1
        print(str1)
        
#writing to output file
o_file.write("The goodies selected for distribution: \n")

o_file.write("\n")

for i in o_list:
    o_file.write(i)
    o_file.write("\n")
o_file.write("\n")
o_file.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(diff))

i_file.close()
o_file.close()