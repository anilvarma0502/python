def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("Yes")
            
# driver code
string = "python"
sub_str ="thon"
check(string, sub_str)
