---
title: "Module One: CPU and Memory"
categories: digwrld
layout: post
---


<h3> Bus Width, Bus Speed, and Bandwidth </h3>

A <i>bus</i> is an electronic path over which data can travel.


Bus width and speed together determine the bandwidth. The amount of data actually transfered under real life conditions is called <i> throughput</i>

<h3> Memory </h3>

Word Size: The amount of data that a CPU can manipulate at one time
    - Typically 32 or 64 bits

Cache memory: Special group of extremely fast memory chips localed on the CPU. Sometimes can be off CPU but is usually close for easy accessibility.

- Cache is split into 3 level
    - L1 being the fastest and L3 being the slowest.
    - More cache usually means more information for the CPU to process faster.
    -Cache can be dedicated to each core; may also have shared cache accessible by any core.

- RAM (Random Access Memory): is the computers main memory
    - Consists of chips arranged on a circut board called a memory module (DIMM --> Dual Inline Memory Module)
    - <b> VOLATILE</b>: All contents of RAM are lost once the computer looses power. 

- <b>Registers</b> are high speed memory localtions build into the CPU

- ROM (Read-only memory): Non-volatile memory that does not loose its contents when there is no power to the device. Hard drives with ferromagnetic material are being replaced with flash chips.

<h3> CPU </h3>

Transistors are the key element of any microprocessor, they are made of semi-conductor material that acts like a switch controlling the flow of electrons inside a chip.

- CPU Core Components
    - The <b>ALU (Arithmetic/Logic Unit)</b> performs arithmetic involving integers and logical operations.
    - <b>FPU (Floating Point Unit)</b> perfoms decimal/floating point calculations.
    - <b>The Control Unit</b> coordinates and controls activitys within a CPU core.
    - The <b>Prefetch Unit</b> attempts to retieve data and instructions before they are neede for processing to avoid delays.
    - The <b>Decode Unit</b> translates insctructions from the Prefetch Unit to that they are understood by the Control Unit, ALU or FPU.
    - Cache and Registers store data and instructions for the CPU.
    - The <b>Bus Interface Unit</b> allows the core to communicate with other CPU components.

The Machine Cycle
- Machine Cycle: The series of operations involved in the execution of a cingle machine level instruction. Can be memorized as FDES.
    - F: Fetch --> Instruction is fetched.
    - D: Decode --> The instruction is decoded.
    - E: Execute --> The instruction is executed.
    - S: The original data or the result is stored in the register.    