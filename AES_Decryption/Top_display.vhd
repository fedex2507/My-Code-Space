library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity LED_Display1 is
    Port(
        clk_in : in STD_LOGIC; -- 100 MHz input clock
        reset : in STD_LOGIC; -- Reset signal
        input0 : in STD_LOGIC_VECTOR(3 downto 0); -- First 4-bit input
        input1 : in STD_LOGIC_VECTOR(3 downto 0); -- Second 4-bit input
        input2 : in STD_LOGIC_VECTOR(3 downto 0); -- Third 4-bit input
        input3 : in STD_LOGIC_VECTOR(3 downto 0); -- Fourth 4-bit input
        anodes : out STD_LOGIC_VECTOR(3 downto 0); -- Anode signals
        cathode : out STD_LOGIC_VECTOR ( 6 downto 0)
    );
end LED_Display1;

architecture Behavioral of LED_Display1 is
    -- Component declarations
    component Timing_block
        Port (
            clk_in : in STD_LOGIC; -- 100 MHz input clock
            reset : in STD_LOGIC; -- Reset signal
            mux_select : out STD_LOGIC_VECTOR(1 downto 0); -- Signal for the mux
            anodes : out STD_LOGIC_VECTOR(3 downto 0) -- Anodes signal for display
        );
    end component;

    component MUX4
        Port ( 
            select1 : in STD_LOGIC_VECTOR(1 downto 0);          
            input0 : in STD_LOGIC_VECTOR(3 downto 0);           
            input1 : in STD_LOGIC_VECTOR(3 downto 0);           
            input2 : in STD_LOGIC_VECTOR(3 downto 0);           
            input3 : in STD_LOGIC_VECTOR(3 downto 0);           
            output : out STD_LOGIC_VECTOR(3 downto 0)
        );
    end component;

    component AES_Display
        Port ( 
           hex_in  : in  STD_LOGIC_VECTOR(3 downto 0);  -- 4-bit hex input
           seg_out : out STD_LOGIC_VECTOR(6 downto 0) 
        );
    end component;

    -- Signals
    signal mux_select : STD_LOGIC_VECTOR(1 downto 0);
    signal mux_output : STD_LOGIC_VECTOR(3 downto 0);

begin
    -- Instantiate Timing Block
    Timing_block_inst: Timing_block
        port map (
            clk_in => clk_in,
            reset => reset,
            mux_select => mux_select,
            anodes => anodes
        );

    -- Instantiate Multiplexer
    MUX4_inst: MUX4
        port map (
            select1 => mux_select,
            input0 => input0,
            input1 => input1,
            input2 => input2,
            input3 => input3,
            output => mux_output
        );

    -- Instantiate Seven Segment Decoder
    AES_Display_value : AES_Display
        port map (
            hex_in => mux_output,
            seg_out => cathode
        );

end Behavioral;