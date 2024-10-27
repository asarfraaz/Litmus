'''
    Find the total amount with GST
'''

# Your code goes in here

def main():
    cost    = 250
    gstrate = 10
    gst_amt = find_gst(cost, gstrate)
    total   = cost + gst_amt
    print(total)

