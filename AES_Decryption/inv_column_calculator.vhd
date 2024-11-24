library ieee;
use ieee.std_logic_1164.all;

entity inv_column_calculator is
	port (
		input_data : in std_logic_vector(31 downto 0);
		output_data : out std_logic_vector(31 downto 0)
	);
end inv_column_calculator;

architecture rtl of inv_column_calculator is
	signal byte0, byte1, byte2, byte3 : std_logic_vector(7 downto 0);
	signal byte0x9, byte0xB, byte0xD, byte0xE : std_logic_vector(7 downto 0);
	signal byte1x9, byte1xB, byte1xD, byte1xE : std_logic_vector(7 downto 0);
	signal byte2x9, byte2xB, byte2xD, byte2xE : std_logic_vector(7 downto 0);
	signal byte3x9, byte3xB, byte3xD, byte3xE : std_logic_vector(7 downto 0);
begin
	-- Split input_data into bytes
	byte3 <= input_data(7 downto 0);
	byte2 <= input_data(15 downto 8);
	byte1 <= input_data(23 downto 16);
	byte0 <= input_data(31 downto 24);

	-- Perform GF(2^8) multiplications by constants 0x09, 0x0B, 0x0D, 0x0E
	gfmult_by9_inst0 : entity work.gfmult_by9 port map(input_byte => byte0, output_byte => byte0x9);
	gfmult_byB_inst0 : entity work.gfmult_byB port map(input_byte => byte0, output_byte => byte0xB);
	gfmult_byD_inst0 : entity work.gfmult_byD port map(input_byte => byte0, output_byte => byte0xD);
	gfmult_byE_inst0 : entity work.gfmult_byE port map(input_byte => byte0, output_byte => byte0xE);

	gfmult_by9_inst1 : entity work.gfmult_by9 port map(input_byte => byte1, output_byte => byte1x9);
	gfmult_byB_inst1 : entity work.gfmult_byB port map(input_byte => byte1, output_byte => byte1xB);
	gfmult_byD_inst1 : entity work.gfmult_byD port map(input_byte => byte1, output_byte => byte1xD);
	gfmult_byE_inst1 : entity work.gfmult_byE port map(input_byte => byte1, output_byte => byte1xE);

	gfmult_by9_inst2 : entity work.gfmult_by9 port map(input_byte => byte2, output_byte => byte2x9);
	gfmult_byB_inst2 : entity work.gfmult_byB port map(input_byte => byte2, output_byte => byte2xB);
	gfmult_byD_inst2 : entity work.gfmult_byD port map(input_byte => byte2, output_byte => byte2xD);
	gfmult_byE_inst2 : entity work.gfmult_byE port map(input_byte => byte2, output_byte => byte2xE);

	gfmult_by9_inst3 : entity work.gfmult_by9 port map(input_byte => byte3, output_byte => byte3x9);
	gfmult_byB_inst3 : entity work.gfmult_byB port map(input_byte => byte3, output_byte => byte3xB);
	gfmult_byD_inst3 : entity work.gfmult_byD port map(input_byte => byte3, output_byte => byte3xD);
	gfmult_byE_inst3 : entity work.gfmult_byE port map(input_byte => byte3, output_byte => byte3xE);

	-- Combine results using XOR to produce final output (as per AES inverse MixColumns)
	output_data(7 downto 0)   <= byte0xB xor byte1xD xor byte2x9 xor byte3xE;
	output_data(15 downto 8)  <= byte0xD xor byte1x9 xor byte2xE xor byte3xB;
	output_data(23 downto 16) <= byte0x9 xor byte1xE xor byte2xB xor byte3xD;
	output_data(31 downto 24) <= byte0xE xor byte1xB xor byte2xD xor byte3x9;
end architecture rtl;