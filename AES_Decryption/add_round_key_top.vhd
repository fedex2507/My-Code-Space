library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity add_round_key_top is
    Port (
        input1 : in std_logic_vector(127 downto 0);
        input2 : in std_logic_vector(127 downto 0);
        output : out std_logic_vector(127 downto 0)
    );
end add_round_key_top;

architecture Behavioral of add_round_key_top is
begin
    -- Generate loop for instantiating add_round_key instances
    gen_add_round_key : for i in 0 to 15 generate
        -- Instantiate `add_round_key` for each 8-bit segment
        add_round_key_inst : entity work.add_round_key
            port map (
                input1 => input1(8*i + 7 downto 8*i),
                input2 => input2(8*i + 7 downto 8*i),
                output => output(8*i + 7 downto 8*i)
            );
    end generate gen_add_round_key;

end Behavioral;
