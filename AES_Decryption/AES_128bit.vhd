library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity AES_Decryption_FSM is
    Port (
        clk         : in STD_LOGIC;
        reset       : in STD_LOGIC;
        start       : in STD_LOGIC;
        plain_text  : out STD_LOGIC_VECTOR(127 downto 0); -- Output plaintext
        done1        : out STD_LOGIC                       -- Indicates decryption is complete
    );
end AES_Decryption_FSM;

architecture Behavioral of AES_Decryption_FSM is
    -- FSM states
    type state_type is (Idle, WaitForCipher, Init, WaitForKey, AddRoundKey, InvShiftRows, InvSubBytes,
                        InvMixColumns, FinalRound, Complete);
    signal current_state, next_state : state_type := Idle;

    -- Signals for ROM data
    signal rom_ciphertext : STD_LOGIC_VECTOR(127 downto 0);      -- Output from ciphertext ROM
    signal rom_round_keys : STD_LOGIC_VECTOR(1279 downto 0);     -- Output from round keys ROM (10 rounds)
    signal round_key      : STD_LOGIC_VECTOR(127 downto 0); -- Current round key (128 bits)
    signal done : STD_LOGIC := '0' ;
    -- Internal signals
    signal state_matrix    : STD_LOGIC_VECTOR(127 downto 0);     -- AES state matrix
    signal round           : integer range 0 to 9 := 0;          -- Round counter
    signal xor_output      : STD_LOGIC_VECTOR(127 downto 0);     -- Output from add_round_key component
    signal state_after_shift_rows : STD_LOGIC_VECTOR(127 downto 0);
    signal state_after_sub_bytes : STD_LOGIC_VECTOR(127 downto 0);
    signal state_after_mix_columns : STD_LOGIC_VECTOR(127 downto 0);
    signal checker : std_logic := '0';
    -- New signal for the current round key
--    signal round_key       : STD_LOGIC_VECTOR(127 downto 0);

    signal i: integer;
    
    -- Component declarations for AES operations and ROMs
    component add_round_key_top is
        Port (
            clk : in STD_LOGIC;
            input_data : in STD_LOGIC_VECTOR(127 downto 0);
            round_key : in STD_LOGIC_VECTOR(127 downto 0);
            output : out STD_LOGIC_VECTOR(127 downto 0)
        );
    end component;

    component inv_shift_rows_top is
        port (
            input_data  : in  STD_LOGIC_VECTOR(127 downto 0);
            output_data : out STD_LOGIC_VECTOR(127 downto 0)
        );
    end component;

    component inv_sub_bytes is
        port (
            clk         : in  STD_LOGIC;
            input_data  : in  STD_LOGIC_VECTOR(127 downto 0);
            output_data : out STD_LOGIC_VECTOR(127 downto 0)
        );
    end component;

    component inv_mix_columns_top is
        Port (
            clk    : in  STD_LOGIC;
            input  : in  STD_LOGIC_VECTOR(127 downto 0);
            output : out STD_LOGIC_VECTOR(127 downto 0)
        );
    end component;

    component ciphertext_read is
        Port (
            clk          : in  STD_LOGIC;
            ena          : in  STD_LOGIC;
            cipher_text : out STD_LOGIC_VECTOR(127 downto 0)
        );
    end component;
    
--    component roundkey_read is
--        Port (
--            clk      : in  STD_LOGIC;
--            ena      : in  STD_LOGIC;
--            round    : in  integer range 0 to 9;        -- Round number as input
--            data_out : out STD_LOGIC_VECTOR(127 downto 0)  -- 128-bit output for the current round
--        );
--    end component;
    component roundkey_read is
        Port (
            clk      : in  STD_LOGIC;
            ena      : in  STD_LOGIC;
            data_out : out STD_LOGIC_VECTOR(1279 downto 0)  -- 1280 bits for 160 bytes of data
        );
    end component;

begin
    -- ROM instantiation for loading ciphertext and round keys
    ciphertext_rom_inst: ciphertext_read
        port map (
            clk      => clk,
            ena => '1',
            cipher_text => rom_ciphertext
        );
        
    roundkey_rom_inst: roundkey_read
        port map (
            clk      => clk,
            ena => '1',
            data_out => rom_round_keys
        );
    
    -- Process to select the appropriate round key based on the round counter
    process(round, rom_round_keys)
    begin
        round_key <= rom_round_keys((round + 1) * 128 - 1 downto round * 128);
    end process;

    -- AddRoundKey component instantiation
    add_round_key_inst: add_round_key_top
        port map (
            clk => clk,
            input_data => state_matrix,
            round_key => round_key,
            output => xor_output
        );

    -- AES operation components
    inv_shift_rows_inst: inv_shift_rows_top
        port map (
            input_data => state_matrix,
            output_data => state_after_shift_rows
        );

    inv_sub_bytes_inst: inv_sub_bytes
        port map (
            clk => clk,
            input_data => state_matrix,
            output_data => state_after_sub_bytes
        );

    inv_mix_columns_inst: inv_mix_columns_top
        port map (
            clk => clk,
            input => state_matrix,
            output => state_after_mix_columns
        );

    -- FSM process to handle AES decryption rounds
    process(clk, reset)
    begin
        if reset = '1' then
            current_state <= Idle;
        elsif rising_edge(clk) then
            current_state <= next_state;
        end if;
    end process;
    
    -- FSM logic and state transitions
    process(current_state, start)
    begin
        -- Default signals
        next_state <= current_state;

        case current_state is
            when Idle =>
                if done = '0'  then
                    next_state <= Init;
                    round <= 0; -- Initialize round counter here
                end if;
                
            when Init =>
                state_matrix <= rom_ciphertext;
                next_state <= AddRoundKey;

            when AddRoundKey =>
                state_matrix <= xor_output;
                if round = 9 then
                    next_state <= FinalRound;
                elsif round = 0 then
                    next_state <= InvShiftRows;
                else
                    next_state <= InvMixColumns;
                end if;

            when InvShiftRows =>
                state_matrix <= state_after_shift_rows;
                next_state <= InvSubBytes;

            when InvSubBytes =>
                state_matrix <= state_after_sub_bytes;
                next_state <= AddRoundKey;
                round <= round + 1;               

            when InvMixColumns =>
                state_matrix <= state_after_mix_columns;
                next_state <= InvShiftRows ;

            when FinalRound =>
                done <= '1';
                next_state <= Complete;

            when Complete =>
                plain_text <= state_matrix;
                done1 <= done;
                if start = '0' then
                    next_state <= Idle;
                end if;

            when others =>
                next_state <= Idle;
        end case;
   
    end process;

end Behavioral;