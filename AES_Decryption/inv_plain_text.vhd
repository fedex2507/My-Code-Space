library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;


entity inv_plain_text is
    Port (
        clk        : in std_logic;
        reset      : in std_logic;
        aes_output : in std_logic_vector(127 downto 0); -- 128-bit AES output
        seg        : out std_logic_vector(6 downto 0);  -- 7-segment display (active low)
        an         : out std_logic_vector(3 downto 0)   -- 4-digit select (active low)
    );
end inv_plain_text;

architecture Behavioral of inv_plain_text is
    signal display_data : std_logic_vector(15 downto 0); -- 4 nibbles to display
    signal hex_digit    : std_logic_vector(3 downto 0);  -- Current nibble
    signal digit_sel    : std_logic_vector(1 downto 0);  -- Select 7-segment display
    signal clk_div      : integer := 0;

begin

    -- Clock Divider for Display Refresh (Adjust as needed for visibility)
    process(clk)
    begin
        if rising_edge(clk) then
            if reset = '1' then
                clk_div <= 0;
            else
                clk_div <= clk_div + 1;
            end if;
        end if;
    end process;

    -- Cycle through display data every clock tick
    process(clk_div)
    begin
        case clk_div mod 4 is
            when 0 =>
                hex_digit <= aes_output(127 downto 124); -- First nibble
                digit_sel <= "00";
            when 1 =>
                hex_digit <= aes_output(123 downto 120); -- Second nibble
                digit_sel <= "01";
            when 2 =>
                hex_digit <= aes_output(119 downto 116); -- Third nibble
                digit_sel <= "10";
            when 3 =>
                hex_digit <= aes_output(115 downto 112); -- Fourth nibble
                digit_sel <= "11";
            when others =>
                hex_digit <= (others => '0');
                digit_sel <= "00";
        end case;
    end process;

    -- 7-segment Decoder
    process(hex_digit)
    begin
        case hex_digit is
            when "0000" => seg <= "1000000"; -- 0
            when "0001" => seg <= "1111001"; -- 1
            when "0010" => seg <= "0100100"; -- 2
            when "0011" => seg <= "0110000"; -- 3
            when "0100" => seg <= "0011001"; -- 4
            when "0101" => seg <= "0010010"; -- 5
            when "0110" => seg <= "0000010"; -- 6
            when "0111" => seg <= "1111000"; -- 7
            when "1000" => seg <= "0000000"; -- 8
            when "1001" => seg <= "0010000"; -- 9
            when "1010" => seg <= "0001000"; -- A
            when "1011" => seg <= "0000011"; -- B
            when "1100" => seg <= "1000110"; -- C
            when "1101" => seg <= "0100001"; -- D
            when "1110" => seg <= "0000110"; -- E
            when "1111" => seg <= "0001110"; -- F
            when others => seg <= "1111111"; -- Blank
        end case;
    end process;

    -- Assign 7-segment display select
    an <= "1111"; -- All off by default
    an(to_integer(unsigned(digit_sel))) <= '0'; -- Enable current display

end Behavioral;