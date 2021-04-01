from timeit import default_timer as timer

start = timer()

string = "Mr John Smith    "
length = 13

def URLify(stringArg, intArg):
    if isinstance(stringArg, str):
        if isinstance(intArg, int):
            URLified = ""
            for x in range(intArg):
                if stringArg[x] == ' ':
                    URLified += "%20"
                else:
                    URLified += stringArg[x]
            return URLified

print(str(URLify(string, length)))

end = timer()
print(end - start)