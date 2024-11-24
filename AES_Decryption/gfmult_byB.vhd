library ieee;
use ieee.std_logic_1164.all;

entity gfmult_byB is
	port (
		input_byte : in std_logic_vector(7 downto 0);
		output_byte : out std_logic_vector(7 downto 0)
	);
end gfmult_byB;

architecture behavioral of gfmult_byB is
	signal temp : std_logic_vector(7 downto 0);
	signal temp_mult_by9 : std_logic_vector(7 downto 0);
begin
	-- GF(2^8) multiply by B is multiply by 9 (input_byte * 9) and XOR with temp
	gfmult_by9_inst : entity work.gfmult_by9 port map(input_byte => input_byte, output_byte => temp_mult_by9);
	gfmult_by2_inst : entity work.gfmult_by2 port map(input_byte => input_byte, output_byte => temp);
	output_byte <= temp_mult_by9 xor temp;
end architecture behavioral;