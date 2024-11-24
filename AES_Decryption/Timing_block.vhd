library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity Timing_block is
     Port (
         clk_in : in STD_LOGIC; -- 100 MHz input clock
         reset : in STD_LOGIC; -- Reset signal
         mux_select : out STD_LOGIC_VECTOR (1 downto 0); -- Signal for the mux
         anodes : out STD_LOGIC_VECTOR (3 downto 0) -- Anodes signal for display
     );
end Timing_block;

architecture Behavioral of Timing_block is
     constant N : integer := 100000; -- Adjust this value to get desired refresh rate
     signal counter: integer := 0;
     signal new_clk1 : STD_LOGIC := '0';
     signal temp : STD_LOGIC_VECTOR (1 downto 0);
begin
     -- Process 1: Clock Division from 100 MHz to 100 Hz
     NEW_CLK: process(clk_in, reset)
     begin
         if reset = '1' then
             counter <= 0;
             new_clk1 <= '0';
         elsif rising_edge(clk_in) then
             if counter = N then
                 counter <= 0;
                 new_clk1 <= not new_clk1; -- Toggle the new clock
             else
                 counter <= counter + 1;
             end if;
         end if;
     end process;

     -- Process 2: Mux Select Signal
     MUX_select1: process(new_clk1, reset)
     begin
         if reset = '1' then
             temp <= "00";
         elsif rising_edge(new_clk1) then
             temp <= temp + 1;
         end if;
     end process;

     -- Process 3: Anode Signal Control
     ANODE_select: process(temp)
     begin
         case temp is 
             when "00" => anodes <= "1110"; -- Activate the first display
             when "01" => anodes <= "1101"; -- Activate the second display
             when "10" => anodes <= "1011"; -- Activate the third display
             when "11" => anodes <= "0111"; -- Activate the fourth display
             when others => anodes <= "1111"; -- Deactivate all displays
         end case;
         mux_select <= temp;
     end process;

end Behavioral;




