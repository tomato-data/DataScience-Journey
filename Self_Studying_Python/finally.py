def test():
    print("first line of test() function")
    try:
        print("first line of try")
        return
        print("after return keyword of try")
    except:
        print("except has raised")
    else:
        print("else has raised")
    finally:
        print("finally has raised")
    print("test() function's last line")

test()