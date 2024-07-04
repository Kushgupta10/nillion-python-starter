// Program to display the Fibonacci sequence up to n-th term

output("How many terms? ")
var nterms = input()


nterms = to_int(nterms)


var n1 = 0
var n2 = 1
var count = 0


if nterms <= 0 {
    output("Please enter a positive integer")
} else if nterms == 1 {
    output("Fibonacci sequence upto " + to_string(nterms) + " : ")
    output(to_string(n1))
} else {
    output("Fibonacci sequence:")
    while count < nterms {
        output(to_string(n1))
        var nth = n1 + n2
        // Update values
        n1 = n2
        n2 = nth
        count = count + 1
    }
}
