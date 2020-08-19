def get_email_to_test():
    get_email = input("What is the email you want to validate ")
    email = str(get_email)
    return(email)

def test_for_at_sign(str):
    if "@" in str:
        return((True, None))
    else:
        return(False, "No @ sign found.")

def test_for_fullstop(str):
    if "." in str:
        return((True, None))
    else:
        return(False, "No fullstop found.")

def test_for_com(str):
    if "com" in str:
        return((True, None))
    else:
        return(False, "No com found.")


def check_list():
    clist = [test_for_at_sign,
             test_for_fullstop,
             test_for_com]
    return(clist)

def valid_email(failures):
    if len(failures) == 0:
        return("valid email")
    else:
        return("Not a vaild email address, problems are:\n" + "\n".join(failures))
    








    
def main():
    #email = get_email_to_test()
    email = "dhjashdsjhj@gmail"
    test_results = [ check(email) for check in check_list()]
    failures = [ result[1] for  result in test_results if result[0] == False]
    print(valid_email(failures))
    #print(test_for_at_sign(email))
    #print(test_for_fullstop(email))
    #print(test_for_com(email))
    
main()
