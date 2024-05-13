num=int(input("enter a num: "))
def comma_sep(n):
    #new_num="{:,}".format(n)
    #return new_num
    return (f"{num:,}")
print(comma_sep(num))

#print(f"{num:,}")