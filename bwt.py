def cmp_func(x, y):
    return (x[1] > y[1]) - (x[1] < y[1]) 
 
def compute_suffix_array(input_text, len_text):
    suff = [(i, input_text[i:]) for i in range(len_text)]

    suff.sort(key=lambda x: x[1])

    suffix_arr = [i for i, _ in suff]

    return suffix_arr
 
 
def find_last_char(input_text, suffix_arr, n):
    bwt_arr = ""
    for i in range(n):
        j = suffix_arr[i] - 1
        if j < 0:
            j = j + n
        bwt_arr += input_text[j]
 
    return bwt_arr

        
 
def bwt(input_text):
    input_text += "Ⴓ"

    len_text = len(input_text)
  
    suffix_arr = compute_suffix_array(input_text, len_text)
    
    return find_last_char(input_text, suffix_arr, len_text)

def ibwt(input_text):
    first_col = sorted(input_text)

    table = [i for i in first_col]      

    for i in first_col:
        table = [input_text[j] + table[j] for j in range(len(input_text))]

        table.sort()

    for word in table:
        if word[-1] == "Ⴓ":
            return word.replace("Ⴓ", "")
        
def rl_encode(inp_str):
    red_count = 1 # redundance count. starts at one so to check next letter
    digit_reps = "ႠႡႢႣႤႥႦႧႨႩ" # Georgian text just in case that digits 0-9 are in original text
    i = 0
    return_str = ""

    while True:
        red_count = 1

        if i == len(inp_str):
            break

        try:
            while inp_str[i + red_count] == inp_str[i]:
                red_count += 1 
        except IndexError:
            pass

        digit_rep = "".join([digit_reps[int(i)] for i in str(red_count)])

        if red_count > 2:
            return_str += digit_rep + inp_str[i]
        elif red_count == 2:
            return_str += inp_str[i] + inp_str[i]
        elif red_count == 1:
            return_str += inp_str[i]

        i += red_count

    return return_str
        
def rl_decode(inp_str):
    digit_reps = "ႠႡႢႣႤႥႦႧႨႩ" # Georgian text just in case that digits 0-9 are in original text
    return_str = ""
    digit_str = ""
    i = 0
    while True:
        j = 1
        digit_str = ""
        if inp_str[i] in digit_reps:
            digit_str += str(digit_reps.index(inp_str[i]))
            while inp_str[i + j] in digit_reps:
                digit_str += str(digit_reps.index(inp_str[i + j]))
                j += 1
            
            return_str += "".join([inp_str[i + j] for _ in range(int(digit_str))])

            i += j + 1
        else:
            return_str += inp_str[i]
            i += 1

        if i == len(inp_str):
            break

    return return_str

def compress(inp_str):
    bwt_str = bwt(inp_str)
    rle_str = rl_encode(bwt_str)

    return rle_str

def decompress(inp_str):
    rld_str = rl_decode(inp_str)
    ibwt_str = ibwt(rld_str)

    return ibwt_str
