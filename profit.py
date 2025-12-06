sp=int(input("give the selling price "))
cp=int(input("give the cost of the product "))

if sp>cp:
    profit=sp-cp
    print("profit is:", profit)

else:
    loss=cp-sp
    print("loss is: ", loss)