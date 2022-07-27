# Sequence Detector Desgin Verification

My Gitpod page 

![image](https://user-images.githubusercontent.com/90963965/181357811-d014f56f-1cd4-4e7f-a80a-5c96bf5f6363.png)

## Verification Environment

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Sequence Detector module here) which takes a sequence of single bit input and drivers the output signal high if the seqence is found sucessfully.

The values are assigned to the input port using

```
inputSeq = [0b0,0b1,0b0,0b1,0b1,0b0,0b1,0b0,0b1,0b1,0b0,0b1,0b1,0b0,0b1,0b1,0b0,0b1,0b1,0b1]
```
The assert statement is used for comparing the sequence detector's outut to the expected value.

The following assert statemet is used:

```
    assert seqCount ==5 , "All sequence are not detected "
```

The seqCount variable contains the number of sequence detected in the given sequence and is compared to the number of sequence actually present.

## Test Scenario 

- Test input sequence = 01011010110110110111
- Expected Output of sequecnce detected should be 5.
- Observed Dut output is 2 i.e. output driven high only twice.

![image](https://user-images.githubusercontent.com/90963965/181361166-342db53c-90fe-4b08-b811-9452f420a711.png)

Output mismatches for the above inputs proving that there is a design bug. This problem states that it is not able to check for the overlapping sequences.

## Design Bug

<img src ="https://user-images.githubusercontent.com/90963965/181361434-a2b08dee-d434-40d0-b4ca-67c3ad5de30c.png" width = "400" height = "400"/>


Based on the above test input and analysing the design using the correct FSM diagram for the sequence detector as above , we see the following

![image](https://user-images.githubusercontent.com/90963965/181361914-cd8a7ffd-d327-4923-b756-ef2f367e583e.png)

For correct output the necessay changes which needs to be made are 

![image](https://user-images.githubusercontent.com/90963965/181362776-b1d11b86-61e7-4315-9c59-7b4095cc7390.png)


## Design Fix After Corrections

Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/90963965/181362916-687519ed-0dbc-4375-bb02-097f2539155d.png)





