# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    seqCount = 0
    inputSeq = [0b0,0b1,0b0,0b1,0b1,0b0,0b1,0b0,0b1,0b1,0b0,0b1,0b1,0b0,0b1,0b1,0b0,0b1,0b1,0b1]
    for i in inputSeq:
        dut.inp_bit.value = i
        await FallingEdge(dut.clk)
        if(dut.seq_seen.value == 1):
            seqCount+=1
        dut._log.info(f'Input Sequnce = {dut.inp_bit.value} Sequence Count = {seqCount} DUT = {dut.seq_seen.value}')
    assert seqCount ==5 , "All sequence are not detected "
    cocotb.log.info('#### CTB: Develop your test here! ######')

