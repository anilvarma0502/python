def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
            
string = "python"
sub_str ="py"
check(string, sub_str)
