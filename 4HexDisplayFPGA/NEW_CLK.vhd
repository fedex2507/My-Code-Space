----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 08/28/2024 12:59:57 PM
-- Design Name: 
-- Module Name: NEW_CLK - Behavioral
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
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity NEW_CLK is
    Port (
        clk_in : in STD_LOGIC;
        Output : out STD_LOGIC_VECTOR (1 downto 0);
     );
end NEW_CLK;

architecture Behavioral of NEW_CLK is
    signal count : STD_LOGIC_VECTOR (1 downto 0) := "00";
begin
    Sample_process: process(clk_in)
    begin
        if rising_edge(clk_in) then
        count <= count + 1;
        endif
   end process;
   Output <= count;

end Behavioral;
