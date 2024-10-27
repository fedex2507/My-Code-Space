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

entity MUX2 is
  Port ( x : in STD_LOGIC;
         y : in STD_LOGIC;
         s : in STD_LOGIC;
         z : out STD_LOGIC);
end MUX2;

architecture Behavioral of MUX2 is
  component AND_gate
   Port ( a : in STD_LOGIC;
            b : in STD_LOGIC;
            c : out STD_LOGIC); 
   end component;
   component OR_gate
    Port ( a : in STD_LOGIC;
           b : in STD_LOGIC;
           c : out STD_LOGIC); 
    end component;
    component NOT_gate
        Port ( a : in STD_LOGIC;
           c : out STD_LOGIC);
     end component;  
     signal m,n,o : std_logic;  
 begin  
 DUT1 : NOT_gate port map (a => s, c => m);
 DUT2 : AND_gate port map (a => x, b => m , c => n );
 DUT3 : AND_gate port map (a => y, b => s , c => o );
 DUT4 : OR_gate port map (a => n, b => o, c => z);
 
end Behavioral;
