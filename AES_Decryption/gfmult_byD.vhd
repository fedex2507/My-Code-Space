library ieee;
use ieee.std_logic_1164.all;

entity gfmult_byD is
    port (
        input_byte : in std_logic_vector(7 downto 0);
        output_byte : out std_logic_vector(7 downto 0)
    );
end gfmult_byD;

architecture behavioral of gfmult_byD is
    signal temp_mult_by2 : std_logic_vector(7 downto 0);  -- For multiplication by 2
    signal temp_mult_by4 : std_logic_vector(7 downto 0);  -- For multiplication by 4
    signal temp_mult_by9 : std_logic_vector(7 downto 0);  -- For multiplication by 9
begin
    -- Multiply input_byte by 2 to get temp_mult_by2
    gfmult_by2_inst1 : entity work.gfmult_by2 port map(input_byte => input_byte, output_byte => temp_mult_by2);
    
    -- Multiply temp_mult_by2 by 2 to get temp_mult_by4 (which is input_byte * 4)
    gfmult_by2_inst2 : entity work.gfmult_by2 port map(input_byte => temp_mult_by2, output_byte => temp_mult_by4);
    
    -- Multiply input_byte by 9 using gfmult_by9
    gfmult_by9_inst : entity work.gfmult_by9 port map(input_byte => input_byte, output_byte => temp_mult_by9);
    
    -- Compute output_byte = (input_byte * 9) XOR (input_byte * 4)
    output_byte <= temp_mult_by9 xor temp_mult_by4;

end architecture behavioral;