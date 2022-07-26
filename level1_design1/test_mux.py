# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
   
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
 
    for i in range(31):
        Selection = i
        dut.sel.value = Selection
        await Timer(2,units = 'ns')
        if(dut.out.value != test[Selection]):
            dut._log.info(f'Sel = {Selection} model = {test[Selection]} DUT = {dut.out.value} false')
        else:
            dut._log.info(f'Sel = {Selection} model = {test[Selection]} DUT = {dut.out.value}')
        assert dut.out.value == test[Selection] ,"Multiplexer result is incorrect "+Selection

    cocotb.log.info('##### CTB: Develop your test here ########')
