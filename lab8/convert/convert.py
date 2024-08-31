def float_default(string, fail):
    try:
        return float(string)
    except:
        return fail
