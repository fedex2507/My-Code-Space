----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 09/04/2024 02:06:26 PM
-- Design Name: 
-- Module Name: tb_LED_Display - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: Testbench for the LED_Display module
-- 
-- Dependencies: LED_Display
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
--use IEEE.NUMERIC_STD.ALL; -- Uncomment if needed

entity tb_LED_Display1 is
-- No ports for the testbench entity
end tb_LED_Display1;

architecture Behavioral of tb_LED_Display1 is
    -- Component declaration for the unit under test (UUT)
    component LED_Display1
        Port(
            clk_in : in STD_LOGIC; -- 100 MHz input clock
            reset : in STD_LOGIC; -- Reset signal
            input0 : in STD_LOGIC_VECTOR(3 downto 0); -- First 4-bit input
            input1 : in STD_LOGIC_VECTOR(3 downto 0); -- Second 4-bit input
            input2 : in STD_LOGIC_VECTOR(3 downto 0); -- Third 4-bit input
            input3 : in STD_LOGIC_VECTOR(3 downto 0); -- Fourth 4-bit input
            anodes : out STD_LOGIC_VECTOR(3 downto 0); -- Anode signals
            a, b, c, d, e, f, g : out STD_LOGIC   -- Cathode signals
        );
    end component;

    -- Signals to connect to the UUT
    signal clk_in : std_logic := '0';
    signal reset : std_logic := '1';
    signal input0, input1, input2, input3 : std_logic_vector(3 downto 0);
    signal anodes : std_logic_vector(3 downto 0);
    signal a, b, c, d, e, f, g : std_logic;

    -- Clock period definition
    constant clk_period : time := 10 ns; -- Adjust as needed for your clock frequency

begin
    -- Instantiate the Unit Under Test (UUT)
    UUT: LED_Display1
        port map (
            clk_in => clk_in,
            reset => reset,
            input0 => input0,
            input1 => input1,
            input2 => input2,
            input3 => input3,
            anodes => anodes,
            a => a,
            b => b,
            c => c,
            d => d,
            e => e,
            f => f,
            g => g
        );

    -- Clock generation process
    clk_gen: process
    begin
        while True loop
            clk_in <= not clk_in;
            wait for clk_period / 2;
        end loop;
    end process;

    -- Stimulus process
    stimulus: process
    begin
        -- Initialize inputs
        input0 <= "0000";
        input1 <= "0000";
        input2 <= "0000";
        input3 <= "0000";
        reset <= '1'; -- Apply reset
        wait for 20 ns;
        reset <= '0'; -- Release reset

        -- Apply test vectors
        -- Test case 1
        input0 <= "0001"; input1 <= "0010"; input2 <= "0011"; input3 <= "0100";
        wait for 100 ns;

        -- Test case 2
        input0 <= "0101"; input1 <= "0110"; input2 <= "0111"; input3 <= "1000";
        wait for 100 ns;

        -- Test case 3
        input0 <= "1001"; input1 <= "1010"; input2 <= "1011"; input3 <= "1100";
        wait for 100 ns;

        -- Test case 4
        input0 <= "1101"; input1 <= "1110"; input2 <= "1111"; input3 <= "0000";
        wait for 100 ns;

        -- Finish simulation
        wait;
    end process;

end Behavioral;
