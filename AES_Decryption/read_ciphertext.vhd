library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ciphertext_read is
    Port (
        clk          : in  STD_LOGIC;
        ena          : in  STD_LOGIC;
        cipher_text : out STD_LOGIC_VECTOR(127 downto 0)  -- 128 bits for 16 bytes of data
    );
end ciphertext_read;

architecture Behavioral of ciphertext_read is
--    signal cipher_text : STD_LOGIC_VECTOR(127 downto 0);  -- Temporary signal for parallel assembly

    -- Component declaration for the register_bram_access
    component ciphertext_rom
        Port (
            clka  : in  STD_LOGIC;
            ena  : in  STD_LOGIC;
            addra : in  STD_LOGIC_VECTOR(3 downto 0);  -- 4-bit address for each byte
            douta : out STD_LOGIC_VECTOR(7 downto 0)   -- 8-bit output for each byte
        );
    end component;

begin
    -- Generate block to instantiate 16 instances of register_bram_access
    gen_brom_1 : for i in 0 to 15 generate
        brom_inst : ciphertext_rom
            port map (
                clka     => clk,
                ena     => ena,
                addra    => std_logic_vector(to_unsigned(i, 4)),  -- 4-bit address for each byte
                douta    => cipher_text(127 - i*8 downto 120 - i*8)  -- Map each byte from MSB to LSB in cipher_text
            );
    end generate;

end Behavioral;