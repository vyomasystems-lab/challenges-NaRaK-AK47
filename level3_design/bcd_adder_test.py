# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_bcdAdder(dut):
    """Test for Bcd_adder"""
    couti = 0
    for i in range(1):
        dut.a.value = 10 #i
        dut.b.value = 10 #i+1
        dut.cin.value = 0b0
        await Timer(2,units = 'ns')
        if((2*i+1) > 9):
            couti = 1
        else :
            couti = 0
          
        dut._log.info(f'A = {int(dut.a.value)} B = {int(dut.b.value)} cout = {dut.cout.value} sum = {int(dut.sum.value)} expected sum = {(2*i+1)%10} expected cout = {couti} ') 
        # assert dut.cout.value == couti,"Cout result is incorrect "
        # assert dut.sum.value == (2*i+1)%10, "Sum output is incorrect"

    cocotb.log.info('##### CTB: Develop your test here ########')
