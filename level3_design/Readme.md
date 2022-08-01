# BCD ADDER DESIGN VERIFIACTION

My GitPod View Page

![image](https://user-images.githubusercontent.com/90963965/182028335-d573b3a8-6484-421c-8c0a-38affacdf35e.png)

## Verification Environment

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test ( bcd adder module here) which takes in 2 4-bit inputs a and b and a single bit input cin and gives 4 bit output sum and single bit output cout.

The values are assigned to the input port using 

```
  for i in range(9):
        dut.a.value = i
        dut.b.value = i+1
        dut.cin.value = 0b0
        
```
The assert statement is used for comparing the bcd adder's outut to the expected value.

The following assert statement is used:

```
    assert dut.cout.value == couti,"Cout result is incorrect "
    assert dut.sum.value == (2*i+1)%10, "Sum output is incorrect"
        
```
## Test Scenario
   **Test 1**
- Test Inputs : A = 5 , B = 6 , Cin = 0
- Expected Output : count = 1, sum = 1
- Dut Output : cout = 1 , sum = 0

![image](https://user-images.githubusercontent.com/90963965/182121634-1b2a8293-1c17-4e9f-9685-4ac7cd2b9262.png)

   **Test 2**
 - Test Inputs : A = 5 , B = 3 , Cin = 0
- Expected Output : count = 0, sum = 8
- Dut Output : cout = 0 , sum = 13  
   
![image](https://user-images.githubusercontent.com/90963965/182122025-44ba3b2c-5492-4d8b-af90-fbb5b601ab6e.png)

Output mismatches for the above test cases, proving that there is a design bug.

## Design Bug

Based on the above test input and analysing the design, we see the following

```
begin
        temp = a+b+cin; 
        if(temp > 7)  ==> BUG    
	begin
            temp = temp+5; //add 6, if result is more than 9. ==> BUG
            cout = 1;  //set the carry output
            sum = temp[3:0];   
   	end
    
 ```
For the bcd adder design, the logic in the `if condition` should be `temp > 9` and another correction is `temp = temp + 6` 

