
library ieee;
use ieee.std_logic_1164.all;

entity gfmult_by9 is
	port (
		input_byte : in std_logic_vector(7 downto 0);
		output_byte : out std_logic_vector(7 downto 0)
	);
end gfmult_by9;
    -- Intermediate signals for successive multiplications by 2
architecture behavioral of gfmult_by9 is
    signal temp1, temp2, temp3 : std_logic_vector(7 downto 0);
begin
	-- GF(2^8) multiply by 9 is equivalent to multiply by 2 three times and XOR the input
    stage1: entity work.gfmult_by2 port map(input_byte => input_byte, output_byte => temp1);
    stage2: entity work.gfmult_by2 port map(input_byte => temp1, output_byte => temp2);
    stage3: entity work.gfmult_by2 port map(input_byte => temp2, output_byte => temp3);
	output_byte <= temp3 xor input_byte;
end architecture behavioral;