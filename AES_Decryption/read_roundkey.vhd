--library IEEE;
--use IEEE.STD_LOGIC_1164.ALL;
--use IEEE.NUMERIC_STD.ALL;

--entity roundkey_read is
--  Port ( 
--     round : in integer range 0 to 9;
--     enable       : in std_logic;
--     clk       : in std_logic;
--     checker:    out std_logic;
--     data_out      : out std_logic_vector(127 downto 0)
--  );
--end roundkey_read;

--architecture Behavioral of roundkey_read is
--    component roundkey_rom 
--    Port (
--        addra  : in std_logic_vector(7 downto 0);
--        clka   : in std_logic;
--        ena    : in std_logic;
--        douta  : out std_logic_vector(7 downto 0)
--    );
--    end component;

--    signal addra     : std_logic_vector(7 downto 0);
--    signal douta     : std_logic_vector(7 downto 0);  
--    signal temp_key  : std_logic_vector(127 downto 0);
--    signal i         : integer := 0; 
--    signal done_count: integer := 0;  -- Use a separate counter for done
--begin

--    read: roundkey_rom port map (
--        addra => addra,
--        clka  => clk,
--        ena   => enable,
--        douta => douta
--    );

--    process(clk)
--    begin
--        if rising_edge(clk) then
--            if enable = '1' then
--                if i < 16 then
--                    -- Update the address based on round and i
--                    addra <= std_logic_vector(to_unsigned(round * 16 + i, 8));
--                end if;

--                -- Accumulate data into the output register
--                data_out(127 - (i * 8) downto 127 - (i * 8) - 7) <= douta;

--                -- Control flow for reading all 16 bytes of key
--                if i = 15 then  -- When all 16 bytes are read
--                    i <= 0;
--                    done_count <= 0;  -- Reset done counter
--                    checker <= '1';    -- Signal that the key is read
--                else
--                    i <= i + 1;
--                end if;

--            else
--                i <= 0;  -- Reset i when not enabled
--            end if;
--        end if;
--    end process;

--end Behavioral;

--library IEEE;
--use IEEE.STD_LOGIC_1164.ALL;
--use IEEE.NUMERIC_STD.ALL;

--entity roundkey_read is
--    Port (
--        clk      : in  STD_LOGIC;
--        ena      : in  STD_LOGIC;
--        round    : in  integer range 0 to 9;             -- Round number as input
--        data_out : out STD_LOGIC_VECTOR(127 downto 0);    -- 128-bit output for the current round
--        checker  : out STD_LOGIC                          -- Checker signal to indicate completion
--    );
--end roundkey_read;

--architecture Behavioral of roundkey_read is
--    -- Component declaration for the roundkey_rom
--    component roundkey_rom
--        Port (
--            clka  : in  STD_LOGIC;
--            ena   : in  STD_LOGIC;
--            addra : in  STD_LOGIC_VECTOR(7 downto 0);    -- 8-bit address for each byte
--            douta : out STD_LOGIC_VECTOR(7 downto 0)     -- 8-bit output for each byte
--        );
--    end component;

--    signal addr     : STD_LOGIC_VECTOR(7 downto 0);     -- Signal to store the calculated address
--    signal done     : STD_LOGIC := '0';                  -- Signal to track when 128 bits are read
--    signal count    : integer range 0 to 15 := 0;        -- Counter for number of bytes read

--begin
--    -- Process block to calculate the address, instantiate ROM, and manage checker signal
--    process(clk)
--    begin
--        if rising_edge(clk) then
--            if ena = '1' then  -- Only process when enabled
--                -- Generate the address for each byte of the current round key
--                for i in 0 to 15 loop
--                    addr <= std_logic_vector(to_unsigned((9-round) * 16 + i, 8));  -- Calculate address based on round and byte index

--                    -- Instantiate the roundkey_rom with the calculated address
--                    roundkey_rom_inst : roundkey_rom
--                        port map (
--                            clka  => clk,
--                            ena   => ena,
--                            addra => addr,  -- Use the calculated address here
--                            douta => data_out(i*8 + 7 downto i*8 )  -- Map each 8-bit chunk into data_out
--                        );
--                end loop;

--                -- After reading all 16 bytes, set the checker signal to '1'
--                if count = 15 then
--                    done <= '1';  -- Indicate that all 128 bits are read
--                    count <= 0;   -- Reset the count for next round
--                else
--                    count <= count + 1;  -- Increment the count as bytes are read
--                    done <= '0';  -- Reset checker signal while reading
--                end if;
--            else
--                done <= '0';  -- Reset checker signal if `ena` is not active
--                count <= 0;   -- Reset the count when not enabled
--            end if;
--        end if;
--    end process;

--    -- Map the done signal to the checker output port
--    checker <= done;

--end Behavioral;

--library IEEE;
--use IEEE.STD_LOGIC_1164.ALL;
--use IEEE.NUMERIC_STD.ALL;

--entity roundkey_read is
--    Port (
--        clk      : in  STD_LOGIC;
--        ena      : in  STD_LOGIC;
--        round    : in  integer range 0 to 9;             -- Round number as input
--        data_out : out STD_LOGIC_VECTOR(127 downto 0)    -- 128-bit output for the current round
--    );
--end roundkey_read;

--architecture Behavioral of roundkey_read is
--    -- Component declaration for the roundkey_rom
--    component roundkey_rom
--        Port (
--            clka  : in  STD_LOGIC;
--            ena   : in  STD_LOGIC;
--            addra : in  STD_LOGIC_VECTOR(7 downto 0);    -- 8-bit address for each byte
--            douta : out STD_LOGIC_VECTOR(7 downto 0)     -- 8-bit output for each byte
--        );
--    end component;

--    signal addr : STD_LOGIC_VECTOR(7 downto 0);     -- Signal to store the calculated address

--begin
--    -- Generate statement to create 16 instances of roundkey_rom for each 8-bit segment
--    gen_roundkey : for i in 0 to 15 generate

--        -- Process to calculate the address for each instance
--        process(clk)
--        begin
--            if rising_edge(clk) then
--                addr <= std_logic_vector(to_unsigned((9-round) * 16 + i, 8));  -- Calculate address based on round and byte index
--            end if;
--        end process;

--        -- Instantiate the roundkey_rom with the calculated address
--        roundkey_rom_inst : roundkey_rom
--            port map (
--                clka  => clk,
--                ena   => ena,
--                addra => addr,  -- Use the calculated address here
--                douta => data_out(i*8 + 7 downto i*8 )  -- Map each 8-bit chunk into data_out
--            );
--    end generate;

--end Behavioral;


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity roundkey_read is
    Port (
        clk      : in  STD_LOGIC;
        ena      : in  STD_LOGIC;
        data_out : out STD_LOGIC_VECTOR(1279 downto 0)  -- 1280 bits for 160 bytes of data
    );
end roundkey_read;

architecture Behavioral of roundkey_read is
    -- Component declaration for the roundkey_rom
    component roundkey_rom
        Port (
            clka  : in  STD_LOGIC;
            ena   : in  STD_LOGIC;
            addra : in  STD_LOGIC_VECTOR(7 downto 0);  -- 8-bit address for each byte
            douta : out STD_LOGIC_VECTOR(7 downto 0)   -- 8-bit output for each byte
        );
    end component;

begin
    -- Generate block to instantiate 160 instances of roundkey_rom
    gen_brom_1 : for i in 0 to 159 generate
        brom_inst : roundkey_rom
            port map (
                clka     => clk,
                ena      => ena,
                addra    => std_logic_vector(to_unsigned(i, 8)),  -- 8-bit address for each byte
                douta    => data_out(1279 - i*8 downto 1272 - i*8)  -- Map each byte from MSB to LSB in data_out
            );
    end generate;

end Behavioral;