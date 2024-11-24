library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity MUX4 is      
    Port (  
        select1 : in STD_LOGIC_VECTOR(1 downto 0);          
        input0 : in STD_LOGIC_VECTOR(3 downto 0);           
        input1 : in STD_LOGIC_VECTOR(3 downto 0);           
        input2 : in STD_LOGIC_VECTOR(3 downto 0);           
        input3 : in STD_LOGIC_VECTOR(3 downto 0);           
        output : out STD_LOGIC_VECTOR(3 downto 0)
    );
end MUX4;

architecture Behavioral of MUX4 is
begin    
    process(select1, input0, input1, input2, input3)
    begin
        case select1 is
            when "00" => output <= input0;
            when "01" => output <= input1;
            when "10" => output <= input2;
            when "11" => output <= input3;
            when others => output <= "0000"; -- Default case, though 'others' shouldn't typically occur
        end case;
    end process;
end Behavioral;