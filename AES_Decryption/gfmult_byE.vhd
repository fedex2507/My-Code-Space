
library ieee;
use ieee.std_logic_1164.all;

entity gfmult_byE is
    port (
        input_byte : in std_logic_vector(7 downto 0);
        output_byte : out std_logic_vector(7 downto 0)
    );
end gfmult_byE;

architecture behavioral of gfmult_byE is
    signal temp1, temp2, temp3: std_logic_vector(7 downto 0);
begin
    -- Multiply input_byte by 2 (first instance)
    gfmult_by2_inst1 : entity work.gfmult_by2 port map(input_byte => input_byte, output_byte => temp1);

    -- Multiply temp1 by 2 (second instance)
    gfmult_by2_inst2 : entity work.gfmult_by2 port map(input_byte => temp1, output_byte => temp2);

    -- Multiply temp2 by 2 (third instance)
    gfmult_by2_inst3 : entity work.gfmult_by2 port map(input_byte => temp2, output_byte => temp3);

    -- XOR all three results: (input_byte * 2) ^ (input_byte * 4) ^ (input_byte * 8)
    output_byte <= temp1 xor temp2 xor temp3;

end architecture behavioral;