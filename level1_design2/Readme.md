# Sequence Detector Desgin Verification

My Gitpod page 

![image](https://user-images.githubusercontent.com/90963965/181357811-d014f56f-1cd4-4e7f-a80a-5c96bf5f6363.png)

## Verification Environment

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Sequence Detector module here) which takes a sequence of single bit input and drivers the output signal high if the seqence is found sucessfully.

The values are assigned to the input port using

```
inputSeq = [0b0,0b1,0b0,0b1,0b1,0b0,0b1,0b0,0b1,0b1,0b0,0b1,0b1,0b0,0b1,0b1,0b0,0b1,0b1,0b1]
```
