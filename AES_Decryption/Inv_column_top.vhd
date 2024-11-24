library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity inv_mix_columns_top is
    Port (
        clk : in std_logic;
        input : in STD_LOGIC_VECTOR(127 downto 0); -- 128-bit input state matrix (row-wise)
        output : out STD_LOGIC_VECTOR(127 downto 0) -- 128-bit output state matrix after inverse MixColumns
    );
end inv_mix_columns_top;

architecture Behavioral of inv_mix_columns_top is

    -- Declare the inv_column_calculator component
    component inv_column_calculator is
        port (
            input_data : in std_logic_vector(31 downto 0);  -- 32-bit input column
            output_data : out std_logic_vector(31 downto 0) -- 32-bit output column
        );
    end component;

    -- Signals to hold each column of the input state matrix
    signal col0, col1, col2, col3 : std_logic_vector(31 downto 0);
    
    -- Signals to hold the transformed columns
    signal out_col0, out_col1, out_col2, out_col3 : std_logic_vector(31 downto 0);

begin

    -- Extract each column from the 128-bit input, stored row-wise
    col0 <= input(127 downto 120) & input(119 downto 112) & input(111 downto 104) & input(103 downto 96);
    col1 <= input(95 downto 88) & input(87 downto 80) & input(79 downto 72) & input(71 downto 64);
    col2 <= input(63 downto 56) & input(55 downto 48) & input(47 downto 40) & input(39 downto 32);
    col3 <= input(31 downto 24) & input(23 downto 16) & input(15 downto 8) & input(7 downto 0);

    -- Instantiate inv_column_calculator for each column
    inv_col0 : inv_column_calculator port map(input_data => col0, output_data => out_col0);
    inv_col1 : inv_column_calculator port map(input_data => col1, output_data => out_col1);
    inv_col2 : inv_column_calculator port map(input_data => col2, output_data => out_col2);
    inv_col3 : inv_column_calculator port map(input_data => col3, output_data => out_col3);

    -- Reassemble the transformed columns into the 128-bit output state matrix (row-major)
    output(127 downto 96) <= out_col0;
    output(95 downto 64) <= out_col1;
    output(63 downto 32) <= out_col2;
    output(31 downto 0) <= out_col3;

end Behavioral;
