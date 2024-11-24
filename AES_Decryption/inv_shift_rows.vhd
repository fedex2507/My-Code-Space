library ieee;
use ieee.std_logic_1164.all;

entity inv_shift_rows is
    port (
        input_data  : in  std_logic_vector(31 downto 0);  -- Single row input (32 bits)
        sel         : in  std_logic_vector(1 downto 0);   -- Shift select for row
        output_data : out std_logic_vector(31 downto 0)   -- Single row output (32 bits)
    );
end entity inv_shift_rows;

architecture rtl of inv_shift_rows is
    -- Declare the mux4_to_1 component
    component mux4_to_1 is
        Port (  
            select1 : in STD_LOGIC_VECTOR(1 downto 0);          
            input0 : in STD_LOGIC_VECTOR(7 downto 0);           
            input1 : in STD_LOGIC_VECTOR(7 downto 0);           
            input2 : in STD_LOGIC_VECTOR(7 downto 0);           
            input3 : in STD_LOGIC_VECTOR(7 downto 0);           
            output : out STD_LOGIC_VECTOR(7 downto 0)
        );
    end component;

    -- Byte signals within the row
    signal row0, row1, row2, row3 : std_logic_vector(7 downto 0);
begin
    -- Process to handle shifting
        -- Extract bytes from the input row
        row0 <= input_data(31 downto 24);  -- First byte
        row1 <= input_data(23 downto 16);  -- Second byte
        row2 <= input_data(15 downto 8);   -- Third byte
        row3 <= input_data(7 downto 0);    -- Fourth byte

        -- Instantiate the mux4_to_1 for each output byte based on the sel input
        UUT_mux_row_0: mux4_to_1
            port map (
                select1 => sel,
                input0  => row0,
                input1  => row3,
                input2  => row2,
                input3  => row1,
                output  => output_data(31 downto 24)  -- Assign to output's first byte
            );

        UUT_mux_row_1: mux4_to_1
            port map (
                select1 => sel,
                input0  => row1,
                input1  => row0,
                input2  => row3,
                input3  => row2,
                output  => output_data(23 downto 16)  -- Assign to output's second byte
            );

        UUT_mux_row_2: mux4_to_1
            port map (
                select1 => sel,
                input0  => row2,
                input1  => row1,
                input2  => row0,
                input3  => row3,
                output  => output_data(15 downto 8)   -- Assign to output's third byte
            );

        UUT_mux_row_3: mux4_to_1
            port map (
                select1 => sel,
                input0  => row3,
                input1  => row2,
                input2  => row1,
                input3  => row0,
                output  => output_data(7 downto 0)    -- Assign to output's fourth byte
            );
            
end architecture rtl;

--library ieee;
--use ieee.std_logic_1164.all;

--entity inv_shift_rows is
--    port (
--        input_data  : in  std_logic_vector(31 downto 0);  -- Single row input (32 bits)
--        sel         : in  std_logic_vector(1 downto 0);   -- Shift select for row
--        output_data : out std_logic_vector(31 downto 0)   -- Single row output (32 bits)
--    );
--end entity inv_shift_rows;

--architecture rtl of inv_shift_rows is
--    -- Declare the mux4_to_1 component
--    component mux4_to_1 is
--        Port (  
--            select1 : in STD_LOGIC_VECTOR(1 downto 0);          
--            input0 : in STD_LOGIC_VECTOR(7 downto 0);           
--            input1 : in STD_LOGIC_VECTOR(7 downto 0);           
--            input2 : in STD_LOGIC_VECTOR(7 downto 0);           
--            input3 : in STD_LOGIC_VECTOR(7 downto 0);           
--            output : out STD_LOGIC_VECTOR(7 downto 0)
--        );
--    end component;

--    -- Byte signals within the row
--    signal row0, row1, row2, row3 : std_logic_vector(7 downto 0);
--begin
--    -- Process to handle shifting
--        -- Extract bytes from the input row
--        row0 <= input_data(31 downto 24);  -- First byte
--        row1 <= input_data(23 downto 16);  -- Second byte
--        row2 <= input_data(15 downto 8);   -- Third byte
--        row3 <= input_data(7 downto 0);    -- Fourth byte

--        -- Instantiate the mux4_to_1 for each output byte based on the sel input
--        UUT_mux_row_0: mux4_to_1
--            port map (
--                sel => sel,
--                a   => row0,
--                b   => row3,
--                c   => row2,
--                d   => row1,
--                y   => output_data(31 downto 24)  -- Assign to output's first byte
--            );

--        UUT_mux_row_1: mux4_to_1
--            port map (
--                sel => sel,
--                a   => row1,
--                b   => row0,
--                c   => row3,
--                d   => row2,
--                y   => output_data(23 downto 16)  -- Assign to output's second byte
--            );

--        UUT_mux_row_2: mux4_to_1
--            port map (
--                sel => sel,
--                a   => row2,
--                b   => row1,
--                c   => row0,
--                d   => row3,
--                y   => output_data(15 downto 8)   -- Assign to output's third byte
--            );

--        UUT_mux_row_3: mux4_to_1
--            port map (
--                sel => sel,
--                a   => row3,
--                b   => row2,
--                c   => row1,
--                d   => row0,
--                y   => output_data(7 downto 0)    -- Assign to output's fourth byte
--            );
            
--end architecture rtl;

