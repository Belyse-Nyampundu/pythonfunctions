def hello(*names):
    for name in names:
        print(f"Hello {name}")

def sum(*numbers):
        answer=0
        for number in numbers:
            answer+=number
            
        return answer
# write a function that accepts any number and returns the result of multiply all of them

def multiply(*numberss):
    answerr=1
    for numbers in numberss:
      answerr*=numbers
    return answerr

    # for keyword arguments

def student_attributes(**kwarys):
    for key,value in kwarys.items():
        print(f"{key} : {value}")

        # Default argumentdef 
def my_country(country="Burundi"):
    print(f"Hello from {country}")

# A function named concatenate_args that takes 
# any number of string arguments in positional arguments format 
# and concatenates them into a single string
def concatenate_args(*num):
    string=' '.join(num)
    print(string)
    


# A function named concatenate_kwargs that takes 
# any number of string arguments in keyword arguments 
#  format and concatenates them into a single string

def concatenate_kwargs(**kwargs):
    all=""
    for key,value in kwargs.items():
     all+=(f"{key},{value} ")
    print(all)



    


