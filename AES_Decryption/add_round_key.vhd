library ieee;
use ieee.std_logic_1164.all;

entity add_round_key is
	port (
		input1 : in std_logic_vector(7 downto 0);
		input2 : in std_logic_vector(7 downto 0);
		output : out std_logic_vector(7 downto 0)
	);
end add_round_key;

architecture rtl of add_round_key is
	
begin
	output <= (not input1 and input2) or (not input2 and input1);
		
end architecture rtl;
