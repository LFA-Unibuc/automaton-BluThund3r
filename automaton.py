class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        print("Hi, I'm an automaton!")

    def validate(self):
        """Return a Boolean

        Returns true if the config file is valid,
        and raises a ValidationException if the config is invalid.
        """
        with open("input.txt") as fin:
            lines = [line for line in fin if not line.startswith('#') and line != '\n']

        start_state = ''
        final_states = []
        states = []
        transitions = []
        words = []
        isStates = False
        isTransitions = False
        isWords = False
        no_start = 0

        for line in lines:
            if line.strip().startswith('End'):
                if isWords:
                    isWords = False
                elif isStates:
                    isStates = False
                elif isTransitions:
                    isTransitions = False
            elif line.strip().startswith("Sigma"):
                isWords = True
            elif line.strip().startswith("Transitions"):
                isTransitions = True
            elif line.strip().startswith("States"):
                isStates = True
            else:
                if isStates:
                    temp = [el.strip() for el in line.split(',')]
                    state = temp[0]
                    type1 = type2 = ''
                    if len(temp) == 2:
                        type1 = temp[1]
                    elif len(temp) == 3:
                        type1 = temp[1]
                        type2 = temp[2]
                    if type1.upper() == 'S' or type2.upper() == 'S':
                        no_start += 1
                        start_state = state
                    if no_start > 1:
                        raise Exception('ValidationException')
                    if type1.upper() == 'F' or type2.upper() == 'F':
                        final_states.append(state)
                    states.append(state)
                if isTransitions:
                    state1, word, state2 = [el.strip() for el in line.split(',')]
                    transitions.append((state1, word, state2))
                if isWords:
                    words.append(line.strip())

        if no_start == 0:
            raise Exception('ValidationException')

        for elem in transitions:
            if elem[0] not in states or elem[2] not in states or elem[1] not in words:
                raise Exception('ValidationException')

        return True


    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        """Return the automaton's final configuration
        
        If the input is rejected, the method raises a
        RejectionException.
        """
        pass
    

if __name__ == "__main__":
    a = Automaton('your_config_file')
    print(a.validate())
