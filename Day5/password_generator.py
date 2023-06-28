import random
def generate_pass_cond(count,lis):
    gen_pass = ""
    for i in range(count):
        gen_pass += random.choice(lis)
    return gen_pass  
def shuffle_pass(password):
    shuff_pass =""
    pass_nums = [i for i in range(len(password))]
    for i in range(len(password)):
        c_num = random.choice(pass_nums)
        pass_nums.remove(c_num)
        shuff_pass += password[c_num]

    return shuff_pass

lower_case_letters = [chr(i) for i in range(97,97+26)]
upper_case_letters = [chr(i) for i in range(65,65+26)]
numbers = [str(i) for i in range (0,10)]
symbols_str= "!@#$%^&*()_+~"
symbols = [i for i in symbols_str]
#print(lower_case_letters,"\n", upper_case_letters,"\n", symbols)

print("Welcome to password genrator")
letters_count = int(input("How many letters would you like to have in your password "))
up_case_count = int(input("How many upper case letters would you like to have in your password "))
num_count = int(input("How many numbers would you like to have in your password "))
sym_count = int(input("How many symbols would you like to have in your password "))
password =""
password += generate_pass_cond(up_case_count,upper_case_letters) 
password += generate_pass_cond(num_count,numbers)
password += generate_pass_cond(sym_count,symbols)
rem_letters_count = letters_count - up_case_count - num_count - sym_count
password += generate_pass_cond(rem_letters_count,lower_case_letters)
print("Easy generated password : ", password)
print("Shuffle password: " , shuffle_pass(password))
shuff_password = list(password)
random.shuffle(shuff_password)
print("random.shuffle: ", ''.join(shuff_password))

#future work
#  check if total of upper case letters , symbols, numbers excedes total letters in password
# ask user to shuffle password again 
