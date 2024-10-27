----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 06.08.2024 14:39:56
-- Design Name: 
-- Module Name: MUX2 - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity MUX4 is
  Port ( I1 : in STD_LOGIC;
         I2 : in STD_LOGIC;
         I3 : in STD_LOGIC;
         I4 : in STD_LOGIC;
         S1  : in STD_LOGIC;
         S2  : in STD_LOGIC;
         outp : out STD_LOGIC);
end MUX4;

architecture Behavioral of MUX4 is
  component MUX2
    Port ( x : in STD_LOGIC;
          y : in STD_LOGIC;
          s : in STD_LOGIC;
          z : out STD_LOGIC); 
   end component;
     signal m,n,o : STD_LOGIC;  
 begin  
 DUT1 : MUX2 port map (x => I1, y => I2, s => S1, z => m);
 DUT2 : MUX2 port map (x => I3, y => I4, s => S1, z => n);
 DUT3 : MUX2 port map (x => m, y => n, s => S2, z => outp);
 
end Behavioral;
