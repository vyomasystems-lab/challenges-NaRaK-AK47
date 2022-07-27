# Multiplexer Design Verification

My gitPod Page 

![image](https://user-images.githubusercontent.com/90963965/181365186-f9659404-1899-40e7-b7aa-29e970ffe0d5.png)

## Verification Environment

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Multiplexer module here) which takes in 31 2-bit inputs from inp0 - inp31 nd a 5-bit selection pin input and gives 2-bit output from the given input on inp line based on the selection line.

The values are assigned to the input port using

```
           # 0  1   2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
    test = [ 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 1, 2, 1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2 ]
    dut.inp0.value = test[0]
    dut.inp1.value = test[1]
    dut.inp2.value = test[2]
    dut.inp3.value = test[3]
    dut.inp4.value = test[4]
    dut.inp5.value = test[5]
    dut.inp6.value = test[6]
    dut.inp7.value = test[7]
    dut.inp8.value = test[8]
    dut.inp9.value = test[9]
    dut.inp10.value = test[10]
    dut.inp11.value = test[11]
    dut.inp12.value = test[12]
    dut.inp13.value = test[13]
    dut.inp14.value = test[14]
    dut.inp15.value = test[15]
    dut.inp16.value = test[16]
    dut.inp17.value = test[17]
    dut.inp18.value = test[18]
    dut.inp19.value = test[19]
    dut.inp20.value = test[20]
    dut.inp21.value = test[21]
    dut.inp22.value = test[22]
    dut.inp23.value = test[23]
    dut.inp24.value = test[24]
    dut.inp25.value = test[25]
    dut.inp26.value = test[26]
    dut.inp27.value = test[27]
    dut.inp28.value = test[28]
    dut.inp29.value = test[29]
    dut.inp30.value = test[30]
```

For selection line input is given as 
```
for i in range(31):
        Selection = i
        dut.sel.value = i
```
    
The assert statement is used for comparing the Multiplexer's outut to the expected value.

The following asser statement is used:

```
 assert dut.out.value == test[Selection] ,"Multiplexer result is incorrect "+Selection
```

## Test Scenario
- Test Input for the input pint 0-30 are given as above in the input port
- For the selected lines corresponding should be expeected from the above array 
- For line 12 , 13 and 30 the output doesn't matches to the values in the array.


Output mismatches for the above inputs proving that there is a design bug as dispayed in the figure below

![image](https://user-images.githubusercontent.com/90963965/181369078-322ea2fc-9e2c-4286-943e-35876e66983c.png)

If assert not used all incorrect test cases can be viewed 

![image](https://user-images.githubusercontent.com/90963965/181369332-36fa5b69-12cc-4a34-bb7d-e63ff1e5a5eb.png)


