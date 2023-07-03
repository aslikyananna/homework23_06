num = int(input("write the number"))
numbers_list =  {0: "Zero",
                 1: "One",
                 2: "Two",
                 3: "Three",
                 4: "Four",
                 5: "Five",
                 6: "Six",
                 7: "Seven",
                 8: "Eight",
                 9: "Nine",
                 10: "Ten",
                 11: "Eleven",
                 12: "Twelve",
                 13: "Thirteen",
                 14: "Fourteen",
                 15: "Fifteen",
                 16: "Sixteen",
                 17: "Seventeen",
                 18: "Eighteen",
                 19: "Nineteen",
                 20: "Twenty",
                 30: "Thirty",
                 40: "Forty",
                 50: "Fifty",
                 60: "Sixty",
                 70: "Seventy",
                 80: "Eighty",
                 90: "Ninety",
                 "00": "hundred",
                 "000": "thousand"}
def int_str():
    k_thousand = num // 1000
    k_thousand_mod = num % 1000
    # # k_hundred = (num - k_thousand * 1000)//100
    # # k_hun_mod= (num - k_thousand * 1000) % 100
    k = num // 10
    k_mod = num % 10
    k_hundred = num // 100
    k_hundred_mod = num % 100
    if num >= 0 and num < 100:
        if num in numbers_list.keys():
            return numbers_list[num]
        else:
            k_10 = k*10
            return numbers_list[k_10] + " " + numbers_list[k_mod]
    elif num < 1000  and  num > 99 :
        if k_hundred_mod == 0:
            return numbers_list[k_hundred] + " " + numbers_list["00"]
        else:
            if k_hundred_mod in numbers_list.keys():
                return numbers_list[k_hundred] + " " + numbers_list["00"] + " " + numbers_list[k_hundred_mod]
            else:
                return numbers_list[k_hundred] + " " + numbers_list["00"] + " " + numbers_list[(k_hundred_mod // 10)*10] + " " + numbers_list[k_hundred_mod % 10]
    # elif num > 1000  and  num < 1015 :
    #     if k_thousand_mod == 0:
    #         return numbers_list[k_thousand] + " " + numbers_list["000"]
    #     else:
    #         n =  k_thousand_mod // 100
    #         return numbers_list[k_thousand] + " " + numbers_list["000"] + " " + numbers_list[n] + numbers_list["00"]+" " + numbers_list[(n // 10)*10] + " " + numbers_list[n % 10]
    #         else:
    #             return numbers_list[k_hundred] + " " + numbers_list["00"] + " " + numbers_list[(k_hundred_mod // 10)*10] + " " + numbers_list[k_hundred_mod % 10]

    #         // 1000 != 0 and (number - k_hundred * 1000)//100 != 0:
    #    return numbers_list[k_thousand] and numbers_list["000"]
    # if (number - k_hundred * 1000)//100 != 0:
    #     return numbers_list[k_hundred] and numbers_list["00"] and numbers_list[k]
    # # else:
    # #     return numbers_list[k]



word = int_str()
print(word)