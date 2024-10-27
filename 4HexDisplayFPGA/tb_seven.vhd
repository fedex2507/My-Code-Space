----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 08/28/2024 02:37:19 PM
-- Design Name: 
-- Module Name: tb_seven - Behavioral
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

entity tb_seven is
--  Port ( );
end tb_seven;

architecture Behavioral of tb_seven is
    component pseudo_code_to_vhdl
        Port ( x,y,z,w : in STD_LOGIC;
            a,b,c,d,e,f,g : out STD_LOGIC);
            end component;
            signal x,y,z,w : std_logic; -- inputs
            signal a,b,c,d,e,f,g : std_logic; -- signal 
begin
    UUT : pseudo_code_to_vhdl port map(x=>x,y=>y,z=>z,w=>w,a=>a,b=>b,c=>c,d=>d,e=>e,f=>f,g=>g);
    x <= '0', '1' after 40 ns;
    y <= '0', '1' after 20 ns,'0' after 40 ns, '1' after 60 ns;
    z <= '0', '1' after 10 ns,'0' after 20 ns, '1' after 30 ns, '0' after 40 ns, '1' after 50 ns, '0' after 60ns, '1' after 70 ns;
    w <= '0', '1' after 5 ns,'0' after 10 ns, '1' after 15 ns, '0' after 20 ns, '1' after 25 ns, '0' after 30ns, '1' after 35 ns,'0' after 40ns,'1' after 45ns,'0' after 50ns, '1' after 55ns,'0' after 60ns,'1' after 65ns,'0' after 70ns,'1' after 75ns;
end Behavioral;
