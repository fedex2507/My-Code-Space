library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity inv_sub_bytes is
    port (
        clk         : in  std_logic;                  -- Clock input
        input_data  : in  std_logic_vector(127 downto 0); -- 128-bit input data (AES state)
        output_data : out std_logic_vector(127 downto 0) -- 128-bit output data
    );
end inv_sub_bytes;

architecture Behavioral of inv_sub_bytes is
    -- Component declaration for the memory IP (S-box)
    component inv_sbox
        port (
            a   : in std_logic_vector(7 downto 0); -- Address input (for 8-bit S-box)
            spo : out std_logic_vector(7 downto 0)  -- Data output (for 8-bit output)
        );
    end component;

    -- Signals to connect internal data
    signal sbox_addr   : std_logic_vector(7 downto 0);  -- Address for S-box lookup
    signal sbox_output : std_logic_vector(7 downto 0);  -- Output from S-box

begin
    -- Generate block to instantiate the inv_sbox component for each byte of input_data
    gen_sbox : for i in 0 to 15 generate
        -- Instantiation of inv_sbox for each byte
        sbox_inst : inv_sbox
            port map (
                a   => input_data((i * 8) + 7 downto i * 8),  -- Slice the input_data for each byte
                spo => output_data((i * 8) + 7 downto i * 8)   -- Store the output in temp_data
            );
    end generate;

end Behavioral;
