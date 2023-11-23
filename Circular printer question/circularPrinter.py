def printByCircularPrinter (s : str) -> int:
    if len(s)==0: 
        return 0
    cur = ord('A')
    time=0
    for char in s:
        print("prev "+chr(cur)+ ": " + str(cur))
        print(char + ": ", ord(char))
        time += min(abs(ord(char)-cur),26-(abs(ord(char)-cur)))
        cur = ord(char)
        print("time: "+ str(time))
    return time

def test_printByCircularPrinter():
    # Test Case 1: Basic Test
    s = "ABC"
    assert printByCircularPrinter(s) == 2

    # Test Case 2: Edge Case - Empty String
    s = ""
    assert printByCircularPrinter(s) == 0

    # Test Case 3: Edge Case - Single Capital Letter
    s = "A"
    assert printByCircularPrinter(s) == 0

    # # Test Case 4: General Test - Random String
    s = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    assert printByCircularPrinter(s) == 26

    # Test Case 5: General Test - Random String with Repetition
    s = "ABCA"
    assert printByCircularPrinter(s) == 4

    # Test Case 6: General Test - Random String with Alternating Characters
    s = "ABA"
    assert printByCircularPrinter(s) == 2

    # Test Case 7: General Test - Random String with Random Characters
    s = "FJKDLAS"
    assert printByCircularPrinter(s) == 44


# Run the test cases
test_printByCircularPrinter()
