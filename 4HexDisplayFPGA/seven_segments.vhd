------------------------------------------------------------------------------------
---- Company: 
---- Engineer: 
---- 
---- Create Date: 08/28/2024 01:47:20 PM
---- Design Name: 
---- Module Name: seven_segments - Behavioral
---- Project Name: 
---- Target Devices: 
---- Tool Versions: 
---- Description: 
---- 
---- Dependencies: 
---- 
---- Revision:
---- Revision 0.01 - File Created
---- Additional Comments:
---- 
------------------------------------------------------------------------------------

library IEEE;

use IEEE.STD_LOGIC_1164.ALL;

entity Seven_Segments_Decoder is

    Port (

    x, y, z, w: in STD_LOGIC;

    a, b, c, d, e, f, g : out STD_LOGIC
    );

end entity Seven_Segments_Decoder;

architecture Behavioral of Seven_Segments_Decoder is

begin

a <= not((not y and z) or (x and not y) or (not x and y and not z) or (z 
    and not w) or (x and w));

b <= not( (not z and not w) or (not x and y and not z) or (y and not w) 
    or (x and not y) or (x and z) );

c <= not((not y and not w) or (z and not w) or (x and z) or ( x and y));

d <= not((y and not z and w) or (not x and not y and not w) or (not y 
    and z and w) or (y and z and not w) or (x and not z));

e <= not( (not x and y) or (x and not y) or (not z and w) or (not x and 
not z) or (not x and w));

f <= not((not x and not z and not w) or (not x and z and w) or (x and 
not y and not w) or (x and not z and w)

or (not x and not y and w) or (not x and not y and z and not w));

g <= not((not y and not w) or (not x and z) or (y and w) or (x and not 
z) or (z and not w)) or (x and y and not z and w);

end architecture Behavioral;