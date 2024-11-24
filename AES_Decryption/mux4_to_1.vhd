library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4_to_1 is      
    Port (  
        select1 : in STD_LOGIC_VECTOR(1 downto 0);          
        input0 : in STD_LOGIC_VECTOR(7 downto 0);           
        input1 : in STD_LOGIC_VECTOR(7 downto 0);           
        input2 : in STD_LOGIC_VECTOR(7 downto 0);           
        input3 : in STD_LOGIC_VECTOR(7 downto 0);           
        output : out STD_LOGIC_VECTOR(7 downto 0)
    );
end mux4_to_1;

architecture Behavioral of mux4_to_1 is
begin    
    process(select1, input0, input1, input2, input3)
    begin
        case select1 is
            when "00" => output <= input0;
            when "01" => output <= input1;
            when "10" => output <= input2;
            when "11" => output <= input3;
            when others => output <= "00000000"; -- Default case, though 'others' shouldn't typically occur
        end case;
    end process;
end Behavioral;